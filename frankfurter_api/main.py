from datetime import datetime
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
DATE_PATTERN = "%Y-%m-%d"

class CurrencyValidationError(ValueError):
    ...

class DateValidationError(ValueError):
    ...

class CurrencyAPI:
    BASE_URL = "https://api.frankfurter.dev/v1"

    def get_url(self, base: Optional[str] = None, symbols: Optional[Iterable[str]] = None, date: Optional[str] = None) -> str:
        """Generates the API endpoint URL"""
        if date:
            self.validate_date(date)
            url = f"{self.BASE_URL}/{date}"
        else:
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

    def validate_date(self, date: str):
        """Check if date is in form 1999-01-04"""
        try:
            for d in date.split(".."):
                datetime.strptime(d, DATE_PATTERN)
        except ValueError:
            raise DateValidationError(f"Invalid date: {", ".join(date)}")