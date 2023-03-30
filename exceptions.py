class CommonError(Exception):
    """Общие ошибки, не требующие отправки сообщения в Телеграм."""
    pass


class GeneralError(Exception):
    """Важные ошибки, требующие отправки в Телеграм."""
    pass


class ConnectionError(GeneralError):
    """Важные ошибки, связанные с соединением."""
    pass


class WrongStatusCodeError(GeneralError):
    """Ошибки, связанные с получением кода ответа, отличного от ожидаемого."""
    pass


class MessageNotSentError(GeneralError):
    """Ошибки, связанные с отправкой сообщения"""
    pass
