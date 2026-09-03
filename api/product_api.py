from api.api_client import ApiClient
from models.products_response import ProductsResponse
from exceptions.api_error import ApiError
from helpers.response_validator import ResponseValidator
from models.product_by_id_response import ProductByIdResponse
from models.product_create_response import ProductCreateResponse


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
    
    def product_by_id(self, product_id):

        response = self.client.get(f"/products/{product_id}")

        if response.status_code == 200:
            return ResponseValidator.parse_response(response, ProductByIdResponse)

        raise ApiError(response.json())

    def create_product(self, payload):

        response = self.client.post("/products", json=payload)

        if response.status_code == 201:
            return ResponseValidator.parse_response(response, ProductCreateResponse)
        
        raise ApiError(response.json())

    def delete_product(self, product_id):

        response = self.client.delete(f"/products/{product_id}")

        if response.status_code == 204:
            return response
            
        raise ApiError(response.json())
