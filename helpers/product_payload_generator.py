from faker import Faker
from api.product_api import ProductApi
import random


class ProductPayloadGenerator:

    fake = Faker()

    @staticmethod
    def collect_products_data(product_api):
        list_brand_id = []
        list_category_id = []
        list_co2_rating = []
        list_product_image_id = []
        price = round(random.uniform(1.00, 1000.00), 2)
        is_location_offer = random.choice([True, False])
        is_rental = random.choice([True, False])
        product_name = ProductPayloadGenerator.fake.catch_phrase()
        product_description = ProductPayloadGenerator.fake.catch_phrase()
        in_stock = random.choice([True, False])
        is_eco_friendly = random.choice([True, False])
        first_page = product_api.products()

        for page in range(1, first_page.last_page + 1):
            products = product_api.products(page=page)

            for product in products.data:
                list_brand_id.append(product.brand.id)
                list_category_id.append(product.category.id)
                list_co2_rating.append(product.co2_rating)
                list_product_image_id.append(product.product_image.id)

        brand_id = random.choice(list_brand_id)
        category_id = random.choice(list_category_id)
        co2_rating = random.choice(list_co2_rating)
        product_image_id = random.choice(list_product_image_id)

        return {
            "brand_id": brand_id,
            "category_id": category_id,
            "co2_rating": co2_rating,
            "product_description": product_description,
            "is_location_offer": is_location_offer,
            "is_rental": is_rental,
            "name": product_name,
            "price": price,
            "product_image_id": product_image_id,
            "stock": in_stock,
             "is_eco_friendly": is_eco_friendly
        }
