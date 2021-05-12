import pytest

from flaskr.models import Event

class TestEvent():
    def test_as_dict(self):
        event1 = Event(name='Event 1', latitude='1', longitude='2')
        dict1 = event1.as_dict()

        assert (dict1.get('name') == event1.name and
            dict1.get('latitude') == event1.latitude and
            dict1.get('longitude') == event1.longitude)

    def test___repr__(self):
        event1 = Event(name='Event 1', latitude='1', longitude='2')

        with pytest.raises(TypeError):
            str(event1)

        event1.id = 1000
        assert str(event1) == '<Event 1000: \'Event 1\'>'
