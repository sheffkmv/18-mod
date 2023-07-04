import requests
import json
from config import keys

class ConvertionEcxeption(Exception):
    pass

class ValueConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str ):

        if quote == base:
            raise ConvertionEcxeption(f"Невозможно перевести одинаковые валюты {base}.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionEcxeption(f"Не удалось обработать валюту {quote}.")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionEcxeption(f"Не удалось обработать валюту {base}.")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionEcxeption(f"Не удалось обработать количество {amount}.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")

        total_base = amount * json.loads(r.content)[keys[base]]

        return total_base