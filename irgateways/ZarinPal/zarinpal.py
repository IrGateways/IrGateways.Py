from ..utils import check_status_code
from requests import post, get
from . import models
from .Exeptions import errors, Code
from enum import StrEnum, unique
from typing import Optional, Union


@unique
class Urls(StrEnum):
    BASE = "https://api.zarinpal.com"
    CREATE_URL = f"{BASE}/pg/v4/payment/request.json"
    VERIFY = f"{BASE}/verify"
    UN_VERYFID = f"{BASE}/un-verifid"
    REDIRECT = "https://www.zarinpal.com/pg/StartPay/"


class ZarinalClient:

    def __init__(self, merchant_id: str) -> None:
        """
            ZarinPal Client for connection to Zarinpal for work with this gateway
            :param merchant_id: merchant id must be 36 character
        """
        if len(merchant_id) != 36:
            raise ValueError("merchant_id parameter must be 36 character")
        self.__merchant_id = merchant_id

    @staticmethod
    def __check_response_result(response: object, response_data: object) -> object:

        if check_status_code(response.status_code) and response_data.data and response_data.code in (Code.SUCCESS, Code.VERIDIED):
            return response

        error_code, error_message = response_data.errors.code, response_data.errors.message
        error = errors(error_code)
        raise error(code=error_code, message=error_message)

    def create_url(
        self,
        amount: int,
        callback_url: str,
        currency: Optional[str] = "IRT",
        description: Optional[str] = "IrGateWays",
        metadata: Union[dict, None] = None,
        order_id: Union[str, None] = None
    ) -> models.CreateUrlResponse:
        """
            This method for create url for pay money to your gateway

            :param amount:
            :param callback_url:
            :param currency:
            :param description:
            :param metadata:
            :param order_id:
            :return: CreateUrlResponse object or raise IrGateWaysError
        """

        if not (isinstance(currency, str) and currency.upper() in ("IRR", "IRT")):
            raise ValueError(
                "currency must be string type and must be between 2 values of IRT and IRR")

        try:
            data_for_send = models.CreateUrlRequest(
                merchant_id=self.__merchant_id,
                amount=amount,
                callback_url=callback_url,
                currency=currency,
                description=description,
                metadata=metadata,
                order_id=order_id
            ).json()

            response = post(url=Urls.CREATE_URL, json=data_for_send)
            response_data = models.CreateUrlResponse(**response.json())

            result = self.__check_response_result(response=response, response_data=response_data)
            result.redirect_url = Urls.REDIRECT + result.authority
            return result

        except Exception as error:
            raise error

    def verify(
        self,
        amount: int,
        authority: str
    ) -> bool:
        """
            This method for verify pay to your gateway

            :param amount: the amount must be int
            :param authority: the authority, geted in time of create url
            :return: VerifyResponse object or raise IrGateWaysError
        """

        try:
            data_for_send = models.VerifyRequest(
                merchant_id=self.__merchant_id,
                amount=amount,
                authority=authority
            ).json()
            response = get(url=Urls.VERIFY, json=data_for_send)
            response_data = models.VerifyResponse(**response.json())
            
            result = self.__check_response_result(response=response, response_data=response_data)
            if result.data.code in (Code.SUCCESS, Code.VERIDIED):
                return True
            return False

        except Exception as error:
            raise error

    def get_un_veryfid(self) -> models.UnVeryfidResponse:
        """
            This method for get all un verifid pays from your gateway

            :return: UnVeryfidResponse object or raise IrGateWaysError
        """

        try:
            data_for_send = models.UnVeryfidRequest(
                merchant_id=self.__merchant_id
            ).json()

            response = post(url=Urls.VERIFY, json=data_for_send)
            response_data = models.VerifyResponse(**response)

            result = self.__check_response_result(response=response, response_data=response_data)
            return response

        except Exception as error:
            raise error
