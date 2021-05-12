from .view_model import ViewModel
from flaskr.util import is_empty_string

class LoginForm(ViewModel):
    def __init__(self, *, username, password, loginform_id):
        super().__init__()

        self.loginform_id = loginform_id
        self.username = username
        self.password = password

    def validate(self):
        # TODO validate againsta regular expression

        if not self.username or is_empty_string(self.username):
            self._append_error({'username': 'Invalid or absent username'});

        if not self.password or is_empty_string(self.password):
            self._append_error({'password': 'Invalid or absent password'});

        self._is_valid = len(self._errors) == 0

        return self._is_valid
