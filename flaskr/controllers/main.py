from flask import request, render_template, make_response
import pydash
from .base import BaseController

class MainController(BaseController):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def home(self):
        data = {}

        return render_template('home.html', **data)

    def test(self):
        data = {
            'name': request.args.get('name') or ''
        }

        return make_response(render_template('test.html', **data))
