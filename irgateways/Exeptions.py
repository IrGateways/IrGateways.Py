from typing import Any


class IrGatewaysError(Exception):

    def __init__(self, code: int, message: str, class_attributes: Any) -> None:
        """
            :param code: int
            :param message: str
        """

        self.code = code
        self.message = message
        self.attributes = class_attributes
