import mapper
import typing


class Log(mapper.LogMapper):
    def __init__(
        self,
        log_type: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        timestamp: typing.Optional[float] = None,
    ):
        super().__init__(log_type, message, timestamp)

    def error(self, message: str) -> "Log":
        self._log_type = "error"
        self._message = message
        self._print()
        return self

    def warning(self, message: str) -> "Log":
        self._log_type = "warning"
        self._message = message
        self._print()
        return self

    def success(self, message: str) -> "Log":
        self._log_type = "success"
        self._message = message
        self._print()
        return self

    def info(self, message: str) -> "Log":
        self._log_type = "info"
        self._message = message
        self._print()
        return self

    def _print(self):
        print(f"{self._log_type} - {self._message}")
