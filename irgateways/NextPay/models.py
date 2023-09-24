from pydantic import BaseModel
from typing import Union
from enum import StrEnum


class Currency(StrEnum):
    TOMAN = "IRT"
    RIAL = "IRR"


class AutoVerify(StrEnum):
    YES = "yes"
    NO = "no"


class CreateUrlRequest(BaseModel):
    api_key: str
    order_id: str
    amount: int
    callback_uri: str
    currency: Union[Currency.TOMAN, Currency.RIAL] = Currency.TOMAN
    customer_phone: Union[int, None] = None
    custom_json_fields: Union[dict, None] = None
    payer_name: Union[str, None] = None
    payer_desc: Union[str, None] = None
    auto_verify: Union[AutoVerify, None] = None
    allowed_card: Union[str, None] = None


class CreateUrlResponse(BaseModel):
    code: int
    trans_id: str
    redirect_url: Union[str, None] = None


class VerifyRequest(BaseModel):
    api_key: str
    trans_id: str
    amount: str
    currency: Union[Currency.TOMAN, Currency.RIAL] = Currency.TOMAN


class VerifyResponse(BaseModel):

    code: int
    amount: int
    order_id: str
    card_holder: str
    customer_phone: int
    shaparak_ref_id: str
    custom: dict
    created_at: str  # time -> yyyy-mm-dd hh:mm:ss


class CancelSucseccPayRequest(BaseModel):
    api_key: str
    trans_id: str
    amount: int
    # * مهم : برای لغو تراکنش موفق ، پارامتر refund_request اجباراً فقط و فقط باید دارای مقدار yes_money_back باشد.
    refund_request: str


class CancelSucseccPayResponse(BaseModel):
    code: int
    amount: int
    order_id: str
    card_holder: str
    customer_phone: int
    custom: dict
