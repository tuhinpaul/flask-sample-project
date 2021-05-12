from flask import Flask, Response

from flaskr import create_app
from flaskr.controllers.main import MainController

app: Flask = create_app()

class TestMainController():
    def test_home(self):
        with app.test_client() as client:
            resp: Response = client.get('/')
            assert resp.status_code == 200

    def test_test_without_login(self):
        with app.test_client() as client:
            resp: Response = client.get('/test')
            assert resp.status_code == 200
            assert b'401 Unauthorized' in resp.data
            assert b'Failed authorization for /test' in resp.data

    def test_test_with_login(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['username'] = 'any_username'

            resp: Response = client.get('/test')
            assert resp.status_code == 200
            assert b'401 Unauthorized' in resp.data
            assert b'Failed authorization for /test' in resp.data
