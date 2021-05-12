from flask import request, session, render_template, redirect, url_for, abort
from http import HTTPStatus
from werkzeug.security import check_password_hash

from flaskr.viewmodels import LoginForm
from .base import BaseController
from flaskr.models import User

class AuthController(BaseController):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def login(self):
        if 'username' in session:
            return render_template(
                'auth/login.html',
                errors=[{'loginform': 'You are already logged in'}],
                disable_form=True)

        # GET
        if request.method.upper() == 'GET':
            return render_template('auth/login.html')

        # POST
        elif request.method.upper() == 'POST':
            loginform = LoginForm(
                username=request.form['username'],
                password=request.form['password'],
                loginform_id='loginform')
            
            if not loginform.validate():
                return render_template('auth/login.html', errors=loginform.errors())

            matching_users = User.query.filter(User.username == loginform.username)
            user = matching_users.first()

            if user and check_password_hash(user.password, loginform.password):
                # successful
                session['username'] = request.form['username']
                return redirect(url_for('home'))
            else:
                return render_template(
                    'auth/login.html',
                    errors=[{'loginform': 'Authentication failed'}])


        # invalid method
        else:
            return abort(HTTPStatus.METHOD_NOT_ALLOWED)

    def logout(self):
        if 'username' in session:
            session.pop('username')

        return redirect(url_for('home'))
