import pytest

from flaskr.viewmodels import LoginForm

class TestLoginForm():
    def test_blank_username_blank_password(self):
        form = LoginForm(username='', password='',loginform_id='loginform_id')
        
        assert form.validate() is False
        assert len(form.errors()) == 2

    def test_None_username_None_password(self):
        form = LoginForm(username=None, password=None,loginform_id='loginform_id')
        
        assert form.validate() is False
        assert len(form.errors()) == 2

        # TODO validate contents of form.errors()

    def test_blank_username_valid_password(self):
        form = LoginForm(username='', password='aaa',loginform_id='loginform_id')
        
        assert form.validate() is False
        assert len(form.errors()) == 1

    def test_valid_username_blank_password(self):
        form = LoginForm(username='zzz', password='',loginform_id='loginform_id')
        
        assert form.validate() is False
        assert len(form.errors()) == 1

    # There should be more tests to validate weak password
    # test username against RE
    # test password against RE
