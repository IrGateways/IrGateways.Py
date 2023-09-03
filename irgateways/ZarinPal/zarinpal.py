from ..utils import check_status_code
from requests import post, get
from . import models
from ..Exeptions import IrGatewaysError
from enum import StrEnum, IntEnum, unique
from typing import Optional, Union


@unique
class Urls(StrEnum):
    BASE = "https://api.zarinpal.com"
    CREATE_URL = f"{BASE}/pg/v4/payment/request.json"
    VERIFY = f"{BASE}/verify"
    UN_VERYFID = f"{BASE}/un-verifid"
    REDIRECT = "https://www.zarinpal.com/pg/StartPay/"


@unique
class Cods(IntEnum):
    SUCCESS = 100


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
    def __check_response_result(response: object) -> models.CheckResponseResult:
        if response.data:
            error_code, error_message, error_object = (
                response.data.code,
                response.data.message,
                response.data
            )
        else:
            error_code, error_message, error_object = (
                response.errors.code,
                response.errors.message,
                response.errors
            )
        result = models.CheckResponseResult(
            error_code=error_code,
            error_message=error_message,
            error_object=error_object
        )
        return result

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
            raise ValueError("currency must be string type and must be between 2 values of IRT and IRR")

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

            if check_status_code(response.status_code) and response_data.data and response_data.code == Cods.SUCCESS:
                response_data.data.redirect_url = Urls.REDIRECT + response_data.data.authority
                return response

            check_response_error = self.__check_response_result(response_data)

            raise IrGatewaysError(
                code=check_response_error.error_code,
                message=check_response_error.error_message,
                class_attributes=check_response_error.error_object
            )

        except Exception as error:
            raise error

    def verify(
            self,
            amount: int,
            authority: str
    ) -> models.VerifyResponse:
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
            if check_status_code(response.status_code) and response_data.data and response_data.code == Cods.SUCCESS:
                return response

            check_response_error = self.__check_response_result(response_data)

            raise IrGatewaysError(
                code=check_response_error.error_code,
                message=check_response_error.error_message,
                class_attributes=check_response_error.error_object
            )
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
            )

            response = get(url=Urls.VERIFY, json=data_for_send)
            response_data = models.VerifyResponse(**response.json())
            
            if check_status_code(response.status_code) and response_data.data and response_data.code == Cods.SUCCESS:
                return response

            check_response_error = self.__check_response_result(response_data)

            raise IrGatewaysError(
                code=check_response_error.error_code,
                message=check_response_error.error_message,
                class_attributes=check_response_error.error_object
            )
        
        except Exception as error:
            raise error
