from requests import post, get
from . import models


class ZarinalClient:

    def __init__(self, merchant_id: str) -> None:
        """
            :param merchant_id:
        """
        if len(merchant_id) != 36:
            raise ValueError("merchant_id parameter must be 36 character")
        self.merchant_id = merchant_id

    def create_url(self): ...

    def verify(self): ...

    def get_un_veryfid(self): ...
