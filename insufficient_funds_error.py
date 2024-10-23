class InsufficientFundsError(Exception):
    def __init__(self,msg='Insufficient funds for this operation'):
        self.msg=msg
        super().__init__(self.msg)