from pydantic import BaseModel, Field

from models.product import Product


class ProductsResponse(BaseModel):
    current_page: int
    data: list[Product]
    from_: int | None = Field(default=None, alias="from")
    last_page: int
    per_page: int
    to: int | None = None
    total: int