import requests

from main import Currency

currency = Currency()

def get_currency():
    response = requests.get(tmp := currency.specific_crcs(["CZK", "USD"]))
    print(tmp)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Invalid input")

if currency_info := get_currency():
    print(currency_info)