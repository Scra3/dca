import os
import typing

import requests

TELEGRAM_KEY_FILE = "telegram.key"


class TelegramApi:
    @staticmethod
    def send_message(message: str):
        file = TelegramApi.get_telegram_key_path()
        if os.path.isfile(file):
            chat_id, secret = TelegramApi.load_key(file)
            requests.get(
                f"https://api.telegram.org/bot{secret}/sendMessage?chat_id={chat_id}&text={message}"
            )
        else:
            print('There is no telegram file configuration')

    @staticmethod
    def get_telegram_key_path() -> str:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return f"{dir_path}/../{TELEGRAM_KEY_FILE}"

    @staticmethod
    def load_key(path: str) -> typing.Tuple[str, str]:
        with open(path, "r") as f:
            chat_id = f.readline().strip()
            secret = f.readline().strip()
        return chat_id, secret
