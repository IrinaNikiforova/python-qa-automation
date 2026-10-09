class ApiError(Exception):

    def __init__(self, status_code, response_body):
        self.status_code = status_code
        self.response_body = response_body

        super().__init__(self.status_code, self.response_body)