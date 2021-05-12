from flask.ctx import AppContext
import pytest
import pydash
import os
from flaskr import create_app
from flaskr.database import init_db, Database
from flaskr.util import get_config_value
from flaskr.configs import config_envvar_mapping, TestConfig

app = create_app()

# ensure that test is run with environment variable FLASK_ENV=test
def test_create_dummy_data():
    with app.app_context() as app_context:
        should_initialize_database = get_config_value(app, 'app.initialize_database')
        should_create_dummy_data = get_config_value(app, 'app.create_dummy_data')

        assert should_initialize_database is True
        assert should_create_dummy_data is True

        init_db(app)
