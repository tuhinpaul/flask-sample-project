import os
from typing import Dict
import pydash
from ._mapping import config_envvar_mapping as mapping

class Config:
    app_params = {
        'config': {
            'debug': False,
            'secret_key': b'_5#y2L"F4Q8z\n\xec]/'
        },
        'app': {
            'initialize_database': True,
            'create_dummy_data': True,
            'test_user_username': 'flask2021',
            'test_user_password': 'Flask20215*'
        },
        'db': {
            'dialect': None,
            'host': None,
            'port': None,
            'username': None,
            'password': None,
            'database': None
        }
    }

    def retrieve(self, param_path):
        # enviornment variable has the highest priority
        env_var_name = pydash.get(mapping, param_path)
        if env_var_name in os.environ:
            return os.getenv(env_var_name)

        # then look for environment (production/development/test) configuration:
        env_config_value = pydash.get(self.app_params, param_path)
        if env_config_value is not None:
            return env_config_value

        # if defined nowhere else, return value from Config.app_params
        return pydash.get(Config.app_params, param_path)

    def __init__(self):
        for group_name, group in mapping.items():
            if isinstance(group, str):
                setattr(self, group, self.retrieve(group_name))
            elif isinstance(group, dict):
                for attribute, config_name in group.items():
                    setattr(self, config_name, self.retrieve('%s.%s' % (group_name, attribute)))

    @property
    def DATABASE_URI(self):
        return 'postgresql://user@{}/foo'.format(self.DB_HOST)
