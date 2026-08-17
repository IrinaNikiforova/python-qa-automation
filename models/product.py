from pydantic import BaseModel


class ProductImage(BaseModel):
    id: int
    by_name: str
    by_url: str
    source_name: str
    source_url: str
    file_name: str
    title: str


class Category(BaseModel):
    id: int
    parent_id: int
    name: str
    slug: str


class Brand(BaseModel):
    id: int
    name: str
    slug: str


class Product(BaseModel):
    id: int
    name: str
    description: str
    stock: int
    price: float
    is_location_offer: bool
    is_rental: bool
    co2_rating: str
    brand_id: int
    category_id: int
    product_image_id: int
    is_eco_friendly: bool
    product_image: ProductImage
    category: Category
    brand: Brand