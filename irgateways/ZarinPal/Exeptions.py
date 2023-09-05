from enum import StrEnum
from typing import Union


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
class WagesError(ZarinpalError):... # -34, -35, -36, -39
class CheckShabaError(ZarinpalError):... # -38, 37
class PaidError(ZarinpalError):... # -50, -51
class InvalidAuthorityError(ZarinpalError): ... # -54
class OopsError(ZarinpalError): ... # -40


class Code(StrEnum):
    SUCCESS = "100"
    VERIDIED = "101"
    VALIDATION_ERROR = "-9"
    CHECK_MERCHANTID_OR_IP = "-10"
    MERCHANT_ID_NOT_ACTIVE = "-11"
    MANY_ATTEMPTS_ERROR = "-12"
    SUSPEND_GATEWAY_ERROR  = "-15"
    LEVEL_IS_NOT_VALID_SILVER = "-16"
    LEVEL_IS_NOT_VALID_BLUE = "-17"
    ACCEPT_FLOATING_WAGES = "-30"
    BANK_ACCOUNT_ERROR = "-31"
    OVERLOAD_MAX_AMOUNT = "-32"
    WAGES_FLOATING_ERROR = "-33"
    WAGES_ERROR = "-39"
    WAGES_ERROR_LIMIT_MAX_AMOUNT = "-34"
    WAGES_ERROR_LIMIT_MAX_PEOPLE = "-35"
    WAGES_ERROR_LIMIT_MIN_AMOUNT = "-36"
    CHECK_SHABA_ERROR = "-38"
    WAGES_SHABA_CHECK_ERROR = "-37"
    AMOUNTS_VALUES_ERROR = "-50"
    EXTRA_PARAMS_ERROR = "-40"
    PAID_ERROR = "-51"
    OOPS_ERROR = "-52"
    SESSION_IS_NOT_THIS_MERCHANT_ID = "-53"
    INVALID_AUTHORITY_ERROR = "-54"


__errors = {
    Code.VALIDATION_ERROR: ValidationError,
    Code.CHECK_MERCHANTID_OR_IP: CheckMerchantIdOrIp,
    Code.MERCHANT_ID_NOT_ACTIVE: BadMerchantId,
    Code.MANY_ATTEMPTS_ERROR: ManyAttemptsError,
    Code.SUSPEND_GATEWAY_ERROR: SuspendGatewayError,
    Code.LEVEL_IS_NOT_VALID_SILVER: LevelIsNotValid,
    Code.LEVEL_IS_NOT_VALID_BLUE: LevelIsNotValid,
    Code.ACCEPT_FLOATING_WAGES: AcceptFloatingWages,
    Code.BANK_ACCOUNT_ERROR: BankAccountError,
    Code.OVERLOAD_MAX_AMOUNT: OverloadMaxAmount,
    Code.WAGES_FLOATING_ERROR: WagesFloatingError,
    Code.WAGES_ERROR: WagesError,
    Code.WAGES_ERROR_LIMIT_MAX_AMOUNT: WagesError,
    Code.WAGES_ERROR_LIMIT_MAX_PEOPLE: WagesError,
    Code.WAGES_ERROR_LIMIT_MIN_AMOUNT: WagesError,
    Code.CHECK_SHABA_ERROR: CheckShabaError,
    Code.WAGES_SHABA_CHECK_ERROR: CheckShabaError,
    Code.AMOUNTS_VALUES_ERROR: PaidError,
    Code.EXTRA_PARAMS_ERROR: OopsError,
    Code.PAID_ERROR: PaidError,
    Code.OOPS_ERROR: OopsError,
    Code.SESSION_IS_NOT_THIS_MERCHANT_ID: BadMerchantId,
    Code.INVALID_AUTHORITY_ERROR: InvalidAuthorityError,    
}


def errors(code: Union[str, int]) -> ZarinpalError:
    return __errors.get(str(code), OopsError)
