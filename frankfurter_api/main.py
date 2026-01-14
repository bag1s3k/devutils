from typing import Optional, Iterable

SUPPORTED_CURRENCIES = {
            "AUD": "Australian Dollar",
            "BRL": "Brazilian Real",
            "CAD": "Canadian Dollar",
            "CHF": "Swiss Franc",
            "CNY": "Chinese Yuan",
            "CZK": "Czech Koruna",
            "DKK": "Danish Krone",
            "EUR": "Euro",
            "GBP": "British Pound",
            "HKD": "Hong Kong Dollar",
            "HUF": "Hungarian Forint",
            "IDR": "Indonesian Rupiah",
            "ILS": "Israeli New Shekel",
            "INR": "Indian Rupee",
            "ISK": "Icelandic Króna",
            "JPY": "Japanese Yen",
            "KRW": "South Korean Won",
            "MXN": "Mexican Peso",
            "MYR": "Malaysian Ringgit",
            "NOK": "Norwegian Krone",
            "NZD": "New Zealand Dollar",
            "PHP": "Philippine Peso",
            "PLN": "Polish Zloty",
            "RON": "Romanian Leu",
            "SEK": "Swedish Krona",
            "SGD": "Singapore Dollar",
            "THB": "Thai Baht",
            "TRY": "Turkish Lira",
            "USD": "United States Dollar",
            "ZAR": "South African Rand"
        }

class CurrencyValidationError(ValueError):
    ...

class CurrencyAPI:
    BASE_URL = "https://api.frankfurter.dev/v1"

    def get_latest_url(self, base: Optional[str] = None, symbols: Optional[Iterable[str]] = None) -> str:
        """Generates the API endpoint URL"""
        url = f"{self.BASE_URL}/latest"
        params = []

        if base:
            self.validate_currencies([base])
            params.append(f"base={base}")

        if symbols:
            self.validate_currencies(symbols)
            params.append(f"symbols={",".join(symbols)}")

        if params:
            url += f"?{"&".join(params)}"

        return url

    def validate_currencies(self, currencies: Iterable[str]):
        """Check if CRC or CRCS are being supported"""
        invalid = [c for c in currencies if c not in SUPPORTED_CURRENCIES]
        if invalid:
            raise CurrencyValidationError(f"Unsupported currency codes: {",".join(invalid)}")

if "__main__" == __name__:
    api = CurrencyAPI()
    try:
        print(api.get_latest_url(base="CZK"))
        print(api.get_latest_url(symbols=["USD", "CZK"]))
        print(api.get_latest_url(base="USD", symbols=["CZK", "JPY"]))
    except CurrencyValidationError as e:
        print(f"Error: {e}")