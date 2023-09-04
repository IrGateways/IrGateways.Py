from enum import IntEnum, StrEnum


class ZarinpalError(Exception):

    def __init__(self, code: int, message: str) -> None:
        """
        :code -> error code
        """
        self.code = code
        self.message = message
    
    def __str__(self) -> str:
        return f"(code={self.code}, message={self.message})"


class ValidationError(ZarinpalError):... # -9
class CheckMerchantIdOrIp(ZarinpalError):... # -10
class BadMerchantId(ZarinpalError):... # -11, -53
class ManyAttemptsError(ZarinpalError):... # -12
class SuspendGatewayError(ZarinpalError):... # -15
class LevelIsNotValid(ZarinpalError):... # -16, -17
class AcceptFloatingWages(ZarinpalError):... # -30
class BankAccountError(ZarinpalError):... # -31
class OverloadMaxAmount(ZarinpalError):... # -32
class WagesFloatingError(ZarinpalError):... # -33
class WagesError(ZarinpalError):... # -33, -34, -35, 36, 39
class CheckShabaError(ZarinpalError):... # -38, 37
class AmountsValuesError(ZarinpalError):... # -
class PaidError(ZarinpalError):... # -50, -51
class InvalidAuthorityError(ZarinpalError): ... # -54
class OopsError(ZarinpalError): ... # -40

# 101, 100
class Code(IntEnum):
    validation_error = -9


Errors = {
    "-9": ValidationError,







    
}
