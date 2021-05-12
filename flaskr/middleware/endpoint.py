import importlib
import json
import os
import pydash
from flask import Flask

from .authorization import Authorization

class Endpoint:
    def __init__(self, app:Flask, auth: Authorization):
        self.app = app
        self.auth = auth
        self.init_app()
    
    def init_app(self):
        # TODO implement based on the guide on Flask Extension Development:
        # https://flask.palletsprojects.com/en/1.1.x/extensiondev/

        endpoints = []
        with open(os.path.join(self.app.root_path, 'endpoints.json')) as f:
            endpoints = json.load(f)

        for endpoint in endpoints:
            controllerParts = endpoint["controller"].split(".")
            # TODO validate length of controllerParts

            controller = {
                "method": controllerParts[-1],
                "class":  controllerParts[-2],
                "module": ".".join(controllerParts[0:-2])
            }

            controllerModule = importlib.import_module(controller["module"])
            controllerClass = getattr(controllerModule, controller["class"])
            controllerInstance = controllerClass(self.app)
            handler = getattr(controllerInstance, controller["method"])

            # apply authorization on the handler
            handler = self.auth.wrap_with_authorization(
                handler,
                pydash.get(endpoint, "rule", ""),
                pydash.get(endpoint, "auth.login_required", False),
                pydash.get(endpoint, "auth.roles_required", []))

            # apply route rule on the handler
            route = self.app.route(endpoint["rule"], **(endpoint["options"] or {}))
            route(handler)
