from .config import Config

class ProductionConfig(Config):
    app_params = {
        'config': {
            'debug': False
        },
        'app': {
            'initialize_database': False,
            'create_dummy_data': False
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
