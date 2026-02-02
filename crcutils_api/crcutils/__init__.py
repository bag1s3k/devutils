from .main import CurrencyAPI

# Aliases
_inst = CurrencyAPI()
get_supported_currencies = _inst.get_supported_currencies
get_url = _inst.get_url