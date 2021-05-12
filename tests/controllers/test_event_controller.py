from flask.app import Flask
from flask import Response

import pytest

from flaskr import create_app
from flaskr.database import Database
from flaskr.models.event import Event
from flaskr.controllers.event import EventController

app: Flask = create_app()
evnt_cntlr = None
with app.app_context():
    evnt_cntlr = EventController(app)

class TestEventController():
    def test_get(self):
        # first insert three records
        Database.db_session.query(Event).delete()
        Database.db_session.add_all([
            Event(name='Event 10', latitude=0.55, longitude=-106.55),
            Event(name='Event 20', latitude=1.55, longitude=-106.85),
            Event(name='Event 30', latitude=7.55, longitude=-106.95)
        ])
        Database.db_session.commit()

        with app.app_context():
            resp: Response = evnt_cntlr.get()

            assert resp.status_code == 200
            assert resp.content_type == 'application/json'

            returned_events = resp.get_json()
            assert returned_events[0]['name'] == 'Event 10'
            assert returned_events[1]['name'] == 'Event 20'
            assert returned_events[2]['name'] == 'Event 30'

    def test_post(self):
        with app.app_context():
            with pytest.raises(NotImplementedError):
                evnt_cntlr.post()
        # TODO there should be tests to check how this exception is handled by the application
        #      and what response/header is sent back
