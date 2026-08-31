from pydantic import BaseModel


class SimpleProduct(BaseModel):
    id: int
    name: str
    price: float
    stock: int


def compare_pydantic_models():
    expected = [
        SimpleProduct(id=1, name="Laptop", price=1000, stock=5),
        SimpleProduct(id=2, name="Phone", price=500, stock=10)
    ]

    actual = [
        SimpleProduct(id=1, name="Laptop", price=1000, stock=5),
        SimpleProduct(id=2, name="Phone", price=700, stock=10)
    ]

    differences = []

    for index, (expected_model, actual_model) in enumerate(
        zip(expected, actual)
    ):
        expected_data = expected_model.model_dump()
        actual_data = actual_model.model_dump()

        for field in expected_data:
            if expected_data[field] != actual_data[field]:
                differences.append({
                    "index": index,
                    "field": field,
                    "expected": expected_data[field],
                    "actual": actual_data[field]
                })

    print(differences)

from models.product import Product
from helpers.response_validator import ResponseValidator


def test_compare_products():
    expected = [
        Product(id=1, name="Laptop", price=1000, stock=5),
        Product(id=2, name="Phone", price=500, stock=10)
    ]

    actual = [
        Product(id=1, name="Laptop", price=1000, stock=5),
        Product(id=2, name="Phone", price=700, stock=10)
    ]

    ResponseValidator.assert_models_equal(expected, actual)

compare_lists()
# compare_pydantic_models()