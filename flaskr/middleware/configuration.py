from flask import Flask
from flaskr.configs import DevelopmentConfig, ProductionConfig, TestConfig

class Configuration:
    def __init__(self, app: Flask):
        self.app = app
        
        self.init_app()
    
    def init_app(self):
        # TODO implement based on the guide on Flask Extension Development:
        # https://flask.palletsprojects.com/en/1.1.x/extensiondev/

        config_object = None

        if self.app.env == 'development':
            config_object = DevelopmentConfig()

        elif self.app.env == 'production':
            config_object = ProductionConfig()

        elif self.app.env == 'test':
            config_object = TestConfig()

        else:
            raise Exception('Bad environment value: %s' % self.app.env)

        self.app.config.from_object(config_object)
