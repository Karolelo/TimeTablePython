class BadInputException(Exception):
    def __init__(self, value):
        self.value = value
        message = "Value {} is not a date".format(value)
        super().__init__(message)