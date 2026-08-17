import requests


class ApiClient:

    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def _get_headers(self, headers=None):
        headers = headers or {}

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def get(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        return requests.get(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

    def post(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        return requests.post(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

    def put(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        return requests.put(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

    def patch(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        return requests.patch(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        return requests.delete(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

    def set_token(self, token):
        self.token = token