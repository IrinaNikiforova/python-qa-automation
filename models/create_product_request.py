from pydantic import BaseModel


class CreateProductRequest(BaseModel):
    id: str = ""
    name: str
    description: str
    stock: str = ""
    price: str
    brand_id: str
    category_id: str
    product_image_id: str
    is_location_offer: bool
    is_rental: bool
    co2_rating: str | None