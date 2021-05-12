from flask import Flask, Response
import json
from flask.testing import FlaskClient
from werkzeug.security import generate_password_hash

import pytest

from flaskr import create_app
from flaskr.database import Database
from flaskr.models.user import User

app: Flask = create_app()

class TestAuthController():
    def setup_user_in_db(self):
        # first insert an user (after deleting existing ones)
        Database.db_session.query(User).delete()
        Database.db_session.add(
            User(username='user1001', password=generate_password_hash('pass*1001#')))
        Database.db_session.commit()

    def test_login_first_get(self):
        with app.test_client() as client:
            resp: Response = client.get('/login')
            assert resp.status_code == 200

    def test_login_get_already_logged_in(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['username'] = 'any_username'

            resp: Response = client.get('/login')
            assert resp.status_code == 200
            assert b'You are already logged in' in resp.data

    def test_login_post_already_logged_in(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['username'] = 'any_username'

            resp: Response = client.post('/login', data=dict(
                username='some_other_username',
                password='some_password'
            ))

            assert resp.status_code == 200
            assert b'You are already logged in' in resp.data

    def test_login_blank_username_blank_password(self):
        with app.test_client() as client:
            resp: Response = client.post('/login', data=dict(
                username='',
                password=''
            ))

            assert resp.status_code == 200
            assert b'Invalid or absent username' in resp.data
            assert b'Invalid or absent password' in resp.data

    def test_login_wrong_password(self):
        with app.test_client() as client:
            resp: Response = client.post('/login', data=dict(
                username='user1001',
                password='wrong password'
            ))

            assert resp.status_code == 200
            assert b'Authentication failed' in resp.data

    def test_login_successful_login(self):
        # create a user in the database:
        self.setup_user_in_db()

        with app.test_client() as client:
            resp: Response = client.post('/login', data=dict(
                username='user1001',
                password='pass*1001#'
            ))

            assert resp.status_code == 302
            
            # the username should be available in session now:
            with client.session_transaction() as sess:
                assert sess['username'] == 'user1001'

    def test_login_invalid_method(self):
        # create a user in the database:
        self.setup_user_in_db()

        with app.test_client() as client:
            # remove any user in the session
            with client.session_transaction() as sess:
                if 'username' in sess:
                    sess.pop('username')

            c2: FlaskClient = client
            resp: Response = c2.patch('/login', as_tuple=False, data=dict(
                any_key='any_value'
            ))

            assert resp.status_code == 200
            assert b'405 Method Not Allowed' in resp.data

    def test_logout(self):
        # set username in session
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['username'] = 'any_username'

        # logout
            resp:Response = client.get('/logout')
            assert resp.status_code == 302

            # ensure username no longer exists in the session:
            with client.session_transaction() as sess:
                assert 'username' not in sess

    def test_logout_without_login(self):
        # set username in session
        with app.test_client() as client:
            with client.session_transaction() as sess:
                if 'username' in sess:
                    sess.pop('username')

            resp:Response = client.get('/logout')
            assert resp.status_code == 200
            assert b'401 Unauthorized' in resp.data
