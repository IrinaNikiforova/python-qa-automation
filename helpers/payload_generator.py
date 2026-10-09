from faker import Faker
from api.product_api import ProductApi
import random
from pydantic import EmailStr
from models.create_product_request import CreateProductRequest
from models.product_by_id_response import ProductByIdResponse
from typing import get_args
from pydantic import BaseModel


class PayloadGenerator:

    fake = Faker()

    @staticmethod
    def collect_products_data_2(api_model):
        payload = {}

        for field_name, field_info in api_model.model_fields.items():

            elm_type = field_info.annotation
            args = get_args(elm_type)

            if elm_type is str or (str in get_args(elm_type) and type(None) in get_args(elm_type)):
                if field_name in ('name', 'description'):
                    generated = PayloadGenerator.fake.catch_phrase()
                elif field_name == 'price':
                    generated = round(random.uniform(1.00, 1000.00), 2)
                elif field_name == 'brand_id':
                    generated = random.choice(['01M3ACMGW5AS5B7JJKEM5HA8G2', '01M3ACMGW5AS5B7JJKEM5HA8G3'])
                elif field_name == 'category_id':
                    generated = random.choice(['01M3ACMH7GKDA8YBWFT4K5AE38', '01M3ACMH7GKDA8YBWFT4K5AE34'])
                elif field_name == 'product_image_id':
                    generated = random.choice(['01M3ACMH81ZQ8GDYE0W4QE1FAD', '01M3ACMH81ZQ8GDYE0W4QE1FAE'])
                else:
                    generated = None

            elif elm_type is float:
                generated = round(random.uniform(1.00, 1000.00), 2)

            elif elm_type is bool:
                generated = random.choice([True, False])

            elif str in args:
                generated = random.choice([
                    PayloadGenerator.fake.catch_phrase(),
                    None
                    ])
            elif bool in args:
                generated = random.choice([
                    random.choice([True, False]),
                    None
                    ])
            elif float in args:
                generated = random.choice([
                    round(random.uniform(1.00, 1000.00), 2),
                    None
                    ])
            elif isinstance(elm_type, type) and issubclass(elm_type, BaseModel):
                generated = PayloadGenerator.collect_products_data_2(elm_type)
            else:
                generated = None

            payload[field_name] = generated

        return payload     