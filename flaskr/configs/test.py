from .config import Config

class TestConfig(Config):
    app_params = {
        'config': {
            'debug': True
        },
        'app': {
            'initialize_database': True,
            'create_dummy_data': True,
            'test_user_username': 'flask2021',
            'test_user_password': 'Flask20215*'
        },
        'db': {
            'dialect': 'postgresql',
            'host': '127.0.0.1',
            'port': 5432,
            'username': 'xxx',
            'password': 'xxx',
            'database': 'flasksampledb'
        }
    }
