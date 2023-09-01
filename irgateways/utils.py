def check_status_code(code: int) -> bool:
    """
    this is function for check status code in response, so, give status code Numerically (int)
    example : 100, 200 and ...

    :param object: this parameter must be in models.py and this have a code attribute
    :return: if status code is 100: True else raise IrGatewaysError(code=status_code, message="string")
    """
