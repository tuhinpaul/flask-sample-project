class ViewModel:
    def __init__(self):
        self._is_valid = None

        """
        should contain entries of form {'control_id': 'error message'}.
        entries may contain the same value for 'control_id' if there are
            muliple errors pertaining to that particular 'control_id'
        """
        self._errors = []
    
    def validate(self):
        """
        should be overriden by subclasses
        should set self._is_valid to True/False
        Returns self._is_valid
        """
        raise NotImplementedError()
    
    def is_valid(self):
        """
        self._is_valid should be True/False. But if this is None,
        that may mean that self.validate() was not called yet.
        """
        if self._is_valid is None:
            return self.validate()
        else:
            return self._is_valid
    
    def _append_error(self, err):
        self._errors.append(err)

    def errors(self):
        return self._errors
