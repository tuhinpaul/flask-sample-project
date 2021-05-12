import pytest
from flaskr import create_app
from flaskr.database import init_db

app = create_app()

@pytest.fixture
def setup_db():
    init_db(app)

def test_app():
    assert app is not None
