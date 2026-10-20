from api.api_client import ApiClient
from utils.logger import get_logger


class BrandsApi:

    logger = get_logger(__name__)

    def __init__(self, client: ApiClient):
            self.client = client

    def get_list_of_brands(self):
        
        response = self.client.get("/brands")
    
        return response.json()