import os
import typing

import requests

TELEGRAM_KEY_FILE = "telegram.key"


class TelegramApi:
    @staticmethod
    def send_message(message: str):
        if TelegramApi.available_key():
            chat_id, secret = TelegramApi.load_key()
            requests.get(
                f"https://api.telegram.org/bot{secret}/sendMessage?chat_id={chat_id}&text={message}"
            )

    @staticmethod
    def get_telegram_key_path() -> str:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return f"{dir_path}/../{TELEGRAM_KEY_FILE}"

    @staticmethod
    def available_key():
        return os.path.isfile(TelegramApi.get_telegram_key_path())

    @staticmethod
    def load_key() -> typing.Optional[typing.Tuple[str, str]]:
        with open(TelegramApi.get_telegram_key_path(), "r") as f:
            chat_id = f.readline().strip()
            secret = f.readline().strip()
        return chat_id, secret
