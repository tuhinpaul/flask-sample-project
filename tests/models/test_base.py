import pytest

from flaskr.models import Event

class TestBase():
    def test_get_all(self):
        from flaskr import create_app
        app = create_app()

        # insert some events
        from flaskr.database import Database
        Database.db_session.query(Event).delete()
        Database.db_session.add_all([
            Event(name='Event 1', latitude=50.55, longitude=-106.55),
            Event(name='Event 2', latitude=51.55, longitude=-106.85)
        ])
        Database.db_session.commit()

        # retrieve all events
        event1 = Event()
        all_events = event1.get_all()

        assert len(all_events) == 2

        events_map = map(lambda e: e.name, all_events)
        event_names = list(events_map)
        assert len(event_names) == 2
        assert 'Event 1' in event_names
        assert 'Event 2' in event_names
