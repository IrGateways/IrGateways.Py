from pydantic import BaseModel
from typing import Union


class CreateUrlRequest(BaseModel):
    api_key: str
    order_id: str
    amount: int
    callback_uri: str
    currency: str
    customer_phone: Union[int, None] = None # 0912
    custom_json_fields: Union[dict, None] = None # custom
    payer_name: Union[str, None] = None # name
    payer_desc: Union[str, None] = None # desc
    auto_verify: Union[str, None] = None # yes or no
    allowed_card: Union[str, None] = None # 16 char
