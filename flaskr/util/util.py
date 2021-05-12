import pydash
from flaskr.configs import config_envvar_mapping

def is_empty_string(s):
    return isinstance(s, str) and (not s or s.isspace())

def get_config_value(app, config_key):
    return app.config.get(pydash.get(config_envvar_mapping, config_key))