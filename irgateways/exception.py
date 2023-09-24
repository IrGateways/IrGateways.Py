from typing import Optional


class IrGateWaysError(Exception):

    def __init__(self, code: int, message: Optional[str] = "Error message") -> None:
        self.__code = code
        self.__message = message

    def __get_code(self): return self.__code
    def __get_message(self): return self.__message
    def __setter(self, value): ...
    def __deleter(self): ...

    code = property(
        fget=__get_code,
        fset=__setter,
        fdel=__deleter
    )
    message = property(
        fget=__get_message,
        fset=__setter,
        fdel=__deleter
    )

    def __str__(self):
        return f"error code is : {self.code}, error message is : {self.message}"
