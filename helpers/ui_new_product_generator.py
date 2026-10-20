from helpers.product_payload_generator import ProductPayloadGenerator
from faker import Faker
from typing import get_args
from api.images_api import ImagesApi
from api.brands_api import BrandsApi
from api.categories_api import CategoriesApi
import random

class UINewProductGenerator():

     fake = Faker()

     @staticmethod
     def generate_product_data_for_ui(images_api, brands_api, categories_api):
        name = UINewProductGenerator.fake.catch_phrase()
        description = UINewProductGenerator.fake.paragraph()
        price = str(round(random.uniform(1.00, 1000.00), 2))
        stock = str(round(random.uniform(1, 1000)))

        response = images_api.get_list_of_images()
        images_list = [image.get("title") for image in response]
        current_image = UINewProductGenerator.fake.random_element(elements=images_list)
        print("image: ", current_image)

        response_brands = brands_api.get_list_of_brands()
        brands_list = [brand.get("name") for brand in response_brands]
        current_brand = UINewProductGenerator.fake.random_element(elements=brands_list)

        list_of_CO2 = ["A - Most environmentally friendly",
                        "B - Low environmental impact",
                        "C - Moderate environmental impact",
                        "D - Higher environmental impact",
                        "E - High environmental impact"]
        CO2_rating = UINewProductGenerator.fake.random_element(elements=list_of_CO2)

        response_categories = categories_api.get_list_of_categories()
        list_of_categories = [category.get("name") for category in response_categories]
        current_category = UINewProductGenerator.fake.random_element(elements=list_of_categories)

        return {
                    "name": name,
                    "description": description,
                    "stock": stock,
                    "price": price,
                    "co2_rating": CO2_rating,
                    "brand": current_brand,
                    "category":current_category,
                    "image": current_image
                    }
