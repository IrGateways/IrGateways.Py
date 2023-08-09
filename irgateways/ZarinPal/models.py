from pydantic import BaseModel
from typing import Union


class CreateLinkRequestMetaData(BaseModel):
    mobile: str
    email: str


class CreateLinkRequest(BaseModel):
    merchant_id: str
    amount: int
    callback_url: str
    description: Union[str, None] = None
    metadata: Union[CreateLinkRequestMetaData, None] = None


class CreateLinkresponseData(BaseModel):
    code: int
    message: str
    authority: str
    fee_type: str
    fee: int


class CreateLinkResponse(BaseModel):
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
