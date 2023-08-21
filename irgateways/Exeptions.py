class IrGatewaysError(Exception):

    def __init__(self, code: int, message: str) -> None:
        """
            :param code: int
            :param message: str
        """

        self.code = code
        self.message = message
