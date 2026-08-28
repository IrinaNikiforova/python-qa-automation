from pydantic import BaseModel

from helpers.response_validator import ResponseValidator


class ProductModel(BaseModel):
    id: int
    name: str
    price: float
    stock: int


def test_compare_pydantic_models():
    expected = [
        ProductModel(id=1, name="Laptop", price=1000, stock=5),
        ProductModel(id=2, name="Phone", price=500, stock=10)
    ]

    actual = [
        ProductModel(id=1, name="Laptop", price=1000, stock=5),
        ProductModel(id=2, name="Phone", price=500, stock=10)
    ]

    ResponseValidator.assert_models_lists_equal(
        expected,
        actual
    )