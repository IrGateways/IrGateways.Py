from requests import post
from typing import Optional, Union
from .models import (
    Currency,
    CreateUrlRequest,
    CreateUrlResponse,
    VerifyRequest,
    VerifyResponse,
    CancelSucseccPayRequest,
    CancelSucseccPayResponse
)
from ..exception import IrGateWaysError


class NextpayClient:

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.__error_message = (
            "nextpay gateway create is failure."
            "please visit the https://nextpay.org/nx/docs#step-7 for more information"
        )

    async def create_url(
        self,
        amount: int,
        order_id: str,
        callback_url: str,
        currency: Optional[Currency] = Currency.TOMAN,
        customer_phone: Union[int, None] = None,
        custom_json_fields: Union[dict, None] = None,
        payer_name: Union[str, None] = None,
        payer_desc: Union[str, None] = None,
        auto_verify: Union[str, None] = None,
        allowed_card: Union[str, None] = None
    ) -> CreateUrlResponse:

        CREATE_URL = "https://nextpay.org/nx/gateway/token"

        try:

            data = CreateUrlRequest(
                api_key=self.api_key,
                order_id=order_id,
                amount=amount,
                callback_uri=callback_url,
                currency=currency,
                customer_phone=customer_phone,
                custom_json_fields=custom_json_fields,
                payer_name=payer_name,
                payer_desc=payer_desc,
                auto_verify=auto_verify,
                allowed_card=allowed_card
            ).json()

            result = post(url=CREATE_URL, json=data)
            result = CreateUrlResponse(**result.json())

            if result.code != -1:
                raise IrGateWaysError(
                    code=result.code,
                    message=self.__error_message
                )

            result.redirect_url = f"https://nextpay.org/nx/gateway/payment/{result.trans_id}"
            return result

        except Exception as e:
            raise IrGateWaysError(1, str(e))

    async def verify(self, trans_id: str, amount: int, currency: Optional[Currency] = Currency.TOMAN) -> VerifyResponse:
        """
        this method for verify pay
        """

        VERIFY_URL = "https://nextpay.org/nx/gateway/verify"

        try:

            data = VerifyRequest(
                api_key=self.api_key,
                trans_id=trans_id,
                amount=amount,
                currency=currency
            ).json()

            result = post(url=VERIFY_URL, json=data)
            result = VerifyResponse(**result.json())

            if result.code != 0:
                raise IrGateWaysError(
                    code=result.code,
                    message=self.__error_message
                )

            return result

        except Exception as e:
            raise IrGateWaysError(1, str(e))

    async def cancel(self, trans_id: str, amount: int):  # -90: ok else no ok

        CANCEL_URL = "https://nextpay.org/nx/gateway/verify"

        try:

            data = CancelSucseccPayRequest(
                api_key=self.api_key,
                trans_id=trans_id,
                amount=amount,
                refund_request="yes_money_back"
            ).json()

            result = post(url=CANCEL_URL, json=data)
            result = CancelSucseccPayResponse(**result.json())

            if result.code != -90:
                raise IrGateWaysError(
                    code=result.code,
                    message=self.__error_message
                )

            return result

        except Exception as e:
            raise IrGateWaysError(1, str(e))
