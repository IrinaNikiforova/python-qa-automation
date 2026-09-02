from pydantic import BaseModel
from models.product import ProductImage, Category, Brand


class ProductCreateResponse(BaseModel):
    name: str
    price: float
    is_location_offer: bool
    is_rental: bool
    co2_rating: str
    id: str
    in_stock: bool | None
    is_eco_friendly: bool
    product_image: ProductImage
    category: Category
    brand: Brand