class ApiError(Exception):

    def __init__(self, error_code, error_msg):
        self.error_code = error_code
        self.error_msg = error_msg

        super().__init__(...):
            return {}