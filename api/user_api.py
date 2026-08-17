from api.api_client import ApiClient
from exceptions.api_error import ApiError
from models.users_me_response import UserMeResponse
from models.users_response import UsersResponse
from helpers.response_validator import ResponseValidator

class UserApi:

    def __init__(self, client):
        self.client = client

    def users_me(self, token=None):
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        response = self.client.get(
            "/users/me",
            headers=headers
        )

        if response.status_code == 200:
            return ResponseValidator.parse_response(response, UserMeResponse)

        raise ApiError(response.model_dump_json())

    def users(self, token=None, page=None):
        headers = {}
        params = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        if page is not None:
            params["page"] = page

        response = self.client.get("/users", headers=headers, params=params)

        if response.status_code == 200:
            return ResponseValidator.parse_response(response, UsersResponse)

        raise ApiError(response.model_dump_json())

