from flask import Flask, jsonify

from .base import BaseController
from flaskr.models import Event

class EventController(BaseController):
    def __init__(self, app: Flask):
        super().__init__()
        self.app = app

    def get(self):
        events = map(lambda ev: ev.as_dict(), Event().get_all())

        return jsonify(list(events))

    def post(self):
        raise NotImplementedError()
