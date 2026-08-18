from api.api_client import ApiClient
from models.products_response import ProductsResponse
from exceptions.api_error import ApiError
from helpers.response_validator import ResponseValidator


class ProductApi:

    def __init__(self, client: ApiClient):
        self.client = client

    def products(
        self,
        *,
        page=None,
        brand=None,
        category=None,
        rental=None,
        between=None,
        sort=None
    ):
        params = {}

        if page is not None:
            params["page"] = page

        if brand is not None:
            params["by_brand"] = brand

        if category is not None:
            params["by_category"] = category

        if rental is not None:
            params["is_rental"] = rental

        if between is not None:
            params["between"] = between

        if sort is not None:
            params["sort"] = sort

        response = self.client.get(
            "/products",
            params=params
        )

        if response.status_code == 200:
            return ResponseValidator.parse_response(response, ProductsResponse)

        raise ApiError(response.json())