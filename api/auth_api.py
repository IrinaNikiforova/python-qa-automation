from models.login_response import LoginResponse
from helpers.response_validator import ResponseValidator
from exceptions.api_error import ApiError


class AuthApi:

    def __init__(self, client):
        self.client = client

    def login(self, email, password):
        response = self.client.post(
            "/users/login",
            json={
                "email": email,
                "password": password
            }
        )

        if response.status_code == 200:
            return ResponseValidator.parse_response(
                response,
                LoginResponse
            )

        raise ApiError(response.status_code, response.json())