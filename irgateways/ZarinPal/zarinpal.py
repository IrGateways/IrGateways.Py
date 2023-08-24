from requests import post, get
from . import models
from ..Exeptions import IrGatewaysError
from enum import StrEnum, unique
from typing import Any, Optional, Union


@unique
class Urls(StrEnum):
    BASE = "http://zarinpal"
    CREATE_URL = f"{BASE}/create-url"
    VERIFY = f"{BASE}/verify"
    UN_VERYFID = f"{BASE}/un-verifid"


class ZarinalClient:

    def __init__(self, merchant_id: str) -> None:
        """
            :param merchant_id:
        """
        if len(merchant_id) != 36:
            raise ValueError("merchant_id parameter must be 36 character")
        self.__merchant_id = merchant_id

    def __check_status_code(self, object: Any) -> bool:
        """


            :param object: this parameter must be in models.py and this have a code attribute
            :return: if status code is 100: True else raise IrGatewaysError(code=status_code, message="string")
        """

    def create_url(
            self,
            amount: int,
            callback_url: str,
            currency: str,
            description: Union[str, None] = None,
            metadata: Union[dict, None] = None,
            order_id: Union[str, None] = None
    ) -> models.CreateUrlResponse:
        """


            :param amount:
            :param callback_url:
            :param currency:
            :param description:
            :param metadata:
            :param order_id:
            :return:
        """

    def verify(
            self,
            amount: int,
            authority: str
    ) -> models.VerifyResponse:
        """

            :param amount:
            :param authority:
            :return:
        """

    def get_un_veryfid(self) -> models.UnVeryfidResponse:
        """


            :return:
        """
