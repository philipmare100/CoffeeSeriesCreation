from coffee.client import JsonApiClient
from coffee.resource_handlers import BaseResourceHandler


class SeriesHandler(BaseResourceHandler):
    """
    Handles CRUD operations for Series resources using the JsonApiClient.
    """
    resource_type = 'series'

    def __init__(self, client: JsonApiClient):
        super().__init__(client)
