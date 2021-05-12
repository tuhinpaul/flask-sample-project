from typing import List
from flask import Flask, session, abort

class Authorization:
    def __init__(self, app: Flask):
        self.app = app

        self.init_app()
    
    def init_app(self):
        # TODO implement based on the guide on Flask Extension Development:
        # https://flask.palletsprojects.com/en/1.1.x/extensiondev/
        pass

    def is_authorized(self, login_required: bool, roles_required: List[str]):
        if not login_required:
            return  True

        if login_required:
            if not ('username' in session):
                return False

        # TODO implement checking required roles
        # currently the code with authorize if roles_required is an empty array
        return len(roles_required) == 0

    def wrap_with_authorization(self, handler, route_rule, login_required = False, roles_required = []):
        def wrap():
            isAuthorized = self.is_authorized(login_required, roles_required)

            if isAuthorized:
                return handler()
            else:
                if self.app is not None:
                    self.app.logger.error(
                        'Failed authorization [login_required = %s and roles_required = %s] for %s' %
                        (login_required, roles_required, route_rule))

                # TODO customize response code and message
                abort(401, description = 'Failed authorization for %s' % route_rule)

        return wrap
