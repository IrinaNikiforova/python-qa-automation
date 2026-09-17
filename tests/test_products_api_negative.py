import pytest
import time

from helpers.response_validator import ResponseValidator
from helpers.product_payload_generator import ProductPayloadGenerator

def test_create_product_with_user_token(product_api, auth_token):

    payload = ProductPayloadGenerator.collect_products_data(product_api)

    product_api.client.set_token("")

    response = product_api.client.post(
        "/products",
        json=payload
    )

    print(f"\nStatus: {response.status_code}")
    print(f"Response: {response.json()}")