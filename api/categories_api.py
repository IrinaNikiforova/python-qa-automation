from api.api_client import ApiClient
from utils.logger import get_logger


class CategoriesApi:

    logger = get_logger(__name__)

    def __init__(self, client: ApiClient):
            self.client = client

    def get_list_of_categories(self):
        
        response = self.client.get("/categories")
    
        return response.json()