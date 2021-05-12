import pytest

from flaskr.viewmodels import LoginForm
from flaskr.viewmodels.view_model import ViewModel

class TestViewModel():
    def test_append_error(self):
        form = LoginForm(username='', password='',loginform_id='loginform_id')

        assert form.validate() is False
        assert len(form.errors()) == 2

        form._append_error({'e1': 'e1 error'})
        assert len(form.errors()) == 3

    def test_validate_should_raise(self):
        vm = ViewModel()

        with pytest.raises(NotImplementedError):
            vm.validate()

    def test_is_valid_should_raise(self):
        vm = ViewModel()

        with pytest.raises(NotImplementedError):
            vm.is_valid()
    
    def test_is_valid_if__is_valid_were_not_None(self):
        vm = ViewModel()

        vm._is_valid = False
        assert vm.is_valid() is False

        vm._is_valid = True
        assert vm.is_valid() is True

    def test__append_error(self):
        vm = ViewModel()

        vm._append_error({'e1': 'e1 error'})
        assert len(vm.errors()) == 1

        # TODO: should ignore this error
        vm._append_error({})
        assert len(vm.errors()) == 2

    def test_errors(self):
        vm = ViewModel()
        assert len(vm.errors()) == 0
