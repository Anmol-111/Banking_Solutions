class Account_no_Exception(Exception):
    """Exception for Incorrect Account Number."""
    def __init__(self, arg):
        self.arg=arg
        super().__init__()