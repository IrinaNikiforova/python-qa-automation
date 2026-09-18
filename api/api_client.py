import requests
from utils.logger import get_logger


class ApiClient:

    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token
        self.logger = get_logger(__name__)

    def _get_headers(self, headers=None):
        headers = headers or {}

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def get(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        self.logger.info(f"GET {endpoint}")

        response = requests.get(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

        if response.ok:
            self.logger.info(f"GET {endpoint} -> {response.status_code}")
        else:
            self.logger.error(f"GET {endpoint} -> {response.status_code}")

        return response

    def post(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        self.logger.info(f"POST {endpoint}")

        response = requests.post(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

        if response.ok:
            self.logger.info(f"POST {endpoint} -> {response.status_code}")
        else:
            self.logger.error(f"POST {endpoint} -> {response.status_code}")

        return response

    def put(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        self.logger.info(f"PUT {endpoint}")

        response = requests.put(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

        if response.ok:
            self.logger.info(f"PUT {endpoint} -> {response.status_code}")
        else:
            self.logger.error(f"PUT {endpoint} -> {response.status_code}")

        return response

    def patch(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        self.logger.info(f"PATCH {endpoint}")

        response = requests.patch(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

        if response.ok:
            self.logger.info(f"PATCH {endpoint} -> {response.status_code}")
        else:
            self.logger.error(f"PATCH {endpoint} -> {response.status_code}")

        return response

    def delete(self, endpoint, **kwargs):
        kwargs["headers"] = self._get_headers(kwargs.get("headers"))

        self.logger.info(f"DELETE {endpoint}")

        response = requests.delete(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

        if response.ok:
            self.logger.info(f"DELETE {endpoint} -> {response.status_code}")
        else:
            self.logger.error(f"DELETE {endpoint} -> {response.status_code}")

        return response

    def set_token(self, token):
        self.token = token