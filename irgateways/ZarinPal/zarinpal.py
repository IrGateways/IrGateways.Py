from requests import post, get
from typing import Optional, Union
from .models import (
    CreateUrlRequest,
    CreateUrlResponse,
    VerifyRequest,
    VerifyResponse,
    UnVeryfidRequest,
    UnVeryfidResponse
)
from ..exception import IrGateWaysError


class ZarinalClient:

    def __init__(self, merchant_id: str) -> None:
        """
            ZarinPal Client for connection to Zarinpal for work with this gateway
            :param merchant_id: merchant id must be 36 character
        """
        if len(merchant_id) != 36:
            raise ValueError("merchant_id parameter must be 36 character")
        self.__merchant_id = merchant_id

    async def create(
        self,
        amount: int,
        callback_url: str,
        currency: Optional[str] = "IRT",
        description: Optional[str] = "IrGateWays",
        metadata: Union[dict, None] = None,
        order_id: Union[str, None] = None
    ) -> CreateUrlResponse:
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

        CREATE_URL = "https://api.zarinpal.com/pg/v4/payment/request.json"

        try:

            data = CreateUrlRequest(
                merchant_id=self.__merchant_id,
                amount=amount,
                callback_url=callback_url,
                currency=currency,
                description=description,
                metadata=metadata,
                order_id=order_id
            ).json()

            result = post(url=CREATE_URL, json=data)
            result = CreateUrlResponse(**result.json())

            
            result.redirect_url = f"https://www.zarinpal.com/pg/StartPay/{result.authority}"
            return result

        except Exception as error:
            raise IrGateWaysError(900, str(error))

    async def verify(self, amount: int, authority: str) -> bool:
        """
            This method for verify pay to your gateway

            :param amount: the amount must be int
            :param authority: the authority, geted in time of create url
            :return: VerifyResponse object or raise IrGateWaysError
        """

        VERIFY_URL = "https://api.zarinpal.com/verify"

        try:

            data = VerifyRequest(
                merchant_id=self.__merchant_id,
                amount=amount,
                authority=authority
            ).json()

            result = get(url=VERIFY_URL, json=data)
            result = VerifyResponse(**result.json())

            if result.data.code in (0, -1):  # TODO this
                return True
            return False

        except Exception as error:
            raise error

    async def get_un_veryfid(self) -> UnVeryfidResponse:
        """
            This method for get all un verifid pays from your gateway

            :return: UnVeryfidResponse object or raise IrGateWaysError
        """

        UN_VERIFID_URL = "https://api.zarinpal.com/un-verifid"

        try:

            data = UnVeryfidRequest(merchant_id=self.__merchant_id).json()

            result = post(url=UN_VERIFID_URL, json=data)
            result = VerifyResponse(**result)

            return result

        except Exception as error:
            raise error
