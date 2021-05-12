import pytest

from flaskr.models import User

class TestUser():
    def init_with_bad_types(self):
        u = User(username=23, password=23.23)
        str(u)

    def test___repr__(self):
        u = User(username='validUsername', password='validPassword0%')

        with pytest.raises(TypeError):
            str(u)

        # TODO: consider validating id field (need to know investigate sqlalchemy API)
        u.id = -1000
        assert str(u) == '<User -1000: \'validUsername\'>'
