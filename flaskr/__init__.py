from flask import Flask, render_template
import pydash
import sys
from werkzeug.exceptions import HTTPException

from .configs import config_envvar_mapping
from .middleware import Authorization, Configuration, Endpoint

def create_app():
    app = Flask(__name__)

    # configuration
    Configuration(app)

    # setup database session, Base class for models, and init_db
    # MUST setup database before controllers because Models descend from Database.Base;
    # and controllers will access models. If database is not configured before controllers,
    # instantiating models will raise exception because Database.Base would be None.
    from flaskr.database import Database, init_db

    Database(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        Database.db_session.remove()

    # initialize database (database should exist):
    if app.config.get(pydash.get(config_envvar_mapping, 'app.initialize_database')):
        init_db(app)

    # authorization middleware:
    auth = Authorization(app)

    # setup routes from json
    Endpoint(app, auth)

    @app.errorhandler(HTTPException)
    def handle_exception(err):
        # # To send error in JSON:
        # # start with the correct headers and status code from the error
        # response = err.get_response()
        # # replace the body with JSON
        # response.data = json.dumps({
        #     "code": err.code,
        #     "name": err.name,
        #     "description": err.description,
        # })
        # response.content_type = "application/json"
        # return response
        return render_template('error/catchall.html', err=err)

    return app

print('__name__ is %s' % (__name__))
sys.stdout.flush()

if __name__ == "__main__":
    app = create_app()
    # TODO take host and port from configuration
    app.run(debug = True, host= "0.0.0.0", port = 80)
