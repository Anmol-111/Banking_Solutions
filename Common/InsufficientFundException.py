class Insufficient_Fund_Exception(Exception):
    """Minimum fund in the account must bt 3000."""
    def __init__(self,arg):
        self.arg=arg
        super().__init__()