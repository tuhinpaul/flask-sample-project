from .config import Config

class DevelopmentConfig(Config):
    app_params = {
        'config': {
            'debug': True
        },
        'app': {
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
