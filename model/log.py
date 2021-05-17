import typing

import mapper


class Log(mapper.LogMapper):
    def __init__(
        self,
        log_type: str,
        message: str,
        timestamp: typing.Optional[float] = None,
    ):
        super().__init__(log_type, message, timestamp)

    @staticmethod
    def error(message: str) -> "Log":
        log = Log("error", message)
        log._print()
        return log

    @staticmethod
    def warning(message: str) -> "Log":
        log = Log("warning", message)
        log._print()
        return log

    @staticmethod
    def success(message: str) -> "Log":
        log = Log("success", message)
        log._print()
        return log

    @staticmethod
    def info(message: str) -> "Log":
        log = Log("info", message)
        log._print()
        return log

    def _print(self):
        print(f"{self._log_type} - {self._message}")
