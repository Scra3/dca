import mapper
import typing


class Log(mapper.LogMapper):
    def __init__(self):
        super().__init__()
        self._log_type: typing.Optional[str] = None
        self._message: typing.Optional[str] = None
        self._timestamp: typing.Optional[float] = None

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

    def save(self) -> "Log":
        self._timestamp = self._save_log(self._log_type, self._message)
        return self
