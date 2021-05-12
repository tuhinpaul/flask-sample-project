config_envvar_mapping = {
    'config': {
        'debug': 'DEBUG',
        'secret_key': 'SECRET_KEY'
    },
    'app': {
        'initialize_database': 'FLASK_SAMPLE_INITIALIZE_DATABASE',
        'create_dummy_data': 'FLASK_SAMPLE_CREATE_DUMMY_DATA',
        'test_user_username': 'FLASK_SAMPLE_TEST_USER_USERNAME',
        'test_user_password': 'FLASK_SAMPLE_TEST_USER_PASSWORD'
    },
    'db': {
        'dialect': 'DB_DIALECT',
        'host': 'DB_HOST',
        'port': 'DB_PORT',
        'username': 'DB_USERNAME',
        'password': 'DB_PASSWORD',
        'database': 'DB_DATABASE'
    }
}
