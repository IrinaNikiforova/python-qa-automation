from pydantic import BaseModel


class ProductImage(BaseModel):
    id: str
    by_name: str
    by_url: str
    source_name: str
    source_url: str
    file_name: str
    title: str


class Category(BaseModel):
    id: str
    name: str
    slug: str


class Brand(BaseModel):
    id: str
    name: str


class Product(BaseModel):
    id: str
    name: str
    description: str
    price: float
    is_location_offer: bool
    is_rental: bool
    co2_rating: str
    in_stock: bool
    is_eco_friendly: bool
    product_image: ProductImage
    category: Category
    brand: Brand