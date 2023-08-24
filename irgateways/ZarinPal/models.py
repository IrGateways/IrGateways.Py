from pydantic import BaseModel
from typing import Union, List


class CreateUrlRequestMetaData(BaseModel):
    mobile: str
    email: str


class CreateUrlRequest(BaseModel):
    merchant_id: str
    amount: int
    currency: str
    description: Union[str, None] = None
    callback_url: str
    metadata: Union[CreateUrlRequestMetaData, None] = None
    order_id: Union[str, None] = None


class CreateUrlResponseData(BaseModel):
    code: int
    message: str
    authority: str
    fee_type: str
    fee: int


class CreateUrlResponse(BaseModel):
    data: str
    errors: list


class VerifyRequest(BaseModel):
    merchant_id: str
    amount: int
    authority: str


class VerifyResponseData(BaseModel):
    code: int
    message: str
    card_hash: str
    card_pan: str
    ref_id: int
    fee_type: str
    fee: int


class VerifyResponse(BaseModel):
    data: VerifyResponseData
    errors: list


class UnVeryfidRequest:
    merchant_id: str


class UnVeryfidResponseDataAuthorities:
    authority: str
    amount: int
    callback_url: str
    referer: str
    date: str


class UnVeryfidResponseData:
    code: int
    message: str
    authorities: List[UnVeryfidResponseDataAuthorities]


class UnVeryfidResponse:
    data: UnVeryfidResponseData
