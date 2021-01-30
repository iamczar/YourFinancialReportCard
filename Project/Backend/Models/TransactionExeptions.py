class TransactionException(Exception):
    def __init__(self, exception_message):
        self.exception_message = exception_message
