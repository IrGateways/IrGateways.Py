from pydantic import BaseModel
from typing import Union, Optional, List, Any
from enum import StrEnum


class Currency(StrEnum):
    TOMAN = "IRT"
    RIAL = "IRR"


class FeeType(StrEnum):
    PAYER = "Payer"
    MERCHANT = "Merchant"


class CreateUrlRequestMetaData(BaseModel):
    mobile: str
    email: str


class CreateUrlRequest(BaseModel):
    merchant_id: str
    amount: int
    currency: str
    description: Optional[str] = "created by IrGateWays.Py"
    callback_url: str
    metadata: Union[CreateUrlRequestMetaData, None] = None
    order_id: Union[str, None] = None


class CreateUrlResponseData(BaseModel):
    code: int
    message: str
    authority: str
    fee_type: str
    fee: int
    redirect_url: Union[str, None] = None


class ValidationsError(BaseModel):
    merchant_id: Union[Any, None] = None
    amount: Union[Any, None] = None
    currency: Union[Any, None] = None
    description: Union[Any, None] = None
    callback_url: Union[Any, None] = None
    metadata: Union[Any, None] = None
    order_id: Union[Any, None] = None


class Error(BaseModel):
    code: int
    message: str
    validations: List[ValidationsError]


class CreateUrlResponse(BaseModel):
    data: Union[CreateUrlResponseData, list]
    errors: Union[Error, list]


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
    data: Union[VerifyResponseData, list]
    errors: Union[Error, list]


class UnVeryfidRequest(BaseModel):
    merchant_id: str


class UnVeryfidResponseDataAuthorities(BaseModel):
    authority: str
    amount: int
    callback_url: str
    referer: str
    date: str


class UnVeryfidResponseData(BaseModel):
    code: int
    message: str
    authorities: List[UnVeryfidResponseDataAuthorities]


class UnVeryfidResponse:
    data: Union[UnVeryfidResponseData, list]
    error: Union[Error, list]
