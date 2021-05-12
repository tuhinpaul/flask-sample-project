from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash

from flaskr.util import get_config_value

def get_connection_string(app):
    dialect = get_config_value(app, 'db.dialect')
    host = get_config_value(app, 'db.host')
    port = get_config_value(app, 'db.port')
    username = get_config_value(app, 'db.username')
    password = get_config_value(app, 'db.password')
    database = get_config_value(app, 'db.database')

    return '%s://%s:%s@%s:%s/%s' % (dialect, username, password, host, port, database)

class Database:
    _engine = None
    db_session: scoped_session = None
    Base = None

    def __init__(self, app: Flask):
        self.app = app

        Database._engine = create_engine(get_connection_string(self.app), convert_unicode=False)
        Database.db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=Database._engine))

        Database.Base = declarative_base()
        Database.Base.query = Database.db_session.query_property()

def init_db(app):
    app.logger.debug('Initializing database')

    import flaskr.models
    Database.Base.metadata.create_all(bind=Database._engine)

    # create dummy user and events data:
    if get_config_value(app, 'app.create_dummy_data'):
        app.logger.debug('Creating dummy data')

        from flaskr.models import User, Event

        test_user_username = get_config_value(app, 'app.test_user_username')
        u = User.query.filter(User.username == test_user_username)
        if u.first() is None:
            test_user = User(
                username=test_user_username,
                password=generate_password_hash(get_config_value(app, 'app.test_user_password'))
            )

            Database.db_session.add(test_user)
            Database.db_session.commit()
        
        # create some dummy Events (after removing existing ones)
        Database.db_session.query(Event).delete()
        Database.db_session.add_all([
            Event(name='Event 1', latitude=50.55, longitude=-106.55),
            Event(name='Event 2', latitude=51.55, longitude=-106.85)
        ])
        Database.db_session.commit()

