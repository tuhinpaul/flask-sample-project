## TODO

Follow quickstart: https://flask.palletsprojects.com/en/1.1.x/quickstart/

## Installation

Install `python3-venv`

Create `venv` folder inside project folder: `python3 -m venv venv`

Activate the environment before working on the project: `source ./venv/bin/activate`

Install Flask: `pip install flask`

## Start Flask app:

Define env var `FLASK_APP`

`flask run` OR `flask run --host=0.0.0.0` if you want to make the server externally visible.

Use `FLASK_ENV=development` to enable all development features. This also enables debugging.

To specifically enable debugging use `FLASK_DEBUG=1`


## Important Modules/Packages:

- `from flask import Flask, url_for, render_template, request, make_response, redirect, abort, session`
- `from markupsafe import escape, Markup`
- `from werkzeug.utils import secure_filename`

## Application Tips

### Storing Cookies

```
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```

## Testing

- Use `test_request_context` as follows:
    ```
    from flask import request

    with app.test_request_context('/hello', method='POST'):
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == '/hello'
        assert request.method == 'POST'
    ```

```
pip install -e .

pytest -v

coverage run -m pytest && coverage report
```


## TO Check

- app.root_path vs app.instance_path
- Flask Extension Development: https://flask.palletsprojects.com/en/1.1.x/extensiondev/
- pytest (https://docs.pytest.org/en/latest/) & pyest-cov (http://pytest-cov.readthedocs.io/en/latest/)
- flask-unittest: https://pypi.org/project/flask-unittest/
- alembic
- Flask-Login: https://flask-login.readthedocs.io/en/latest/
- Flask-Mail: https://pythonhosted.org/Flask-Mail/
- Flask-SQLAlchemy & psycopg2
- `jsonify()` for custom class/object
- meaning of `%` in `return 'Logged in as %s' % escape(session['username'])`
- Storing and verifying passwords with SQLAlchemy: https://variable-scope.com/posts/storing-and-verifying-passwords-with-sqlalchemy
- Check app context: https://stackoverflow.com/a/31444175/3422574 and https://flask.palletsprojects.com/en/2.0.x/appcontext/#creating-an-application-context
- 
