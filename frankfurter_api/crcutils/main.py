from datetime import datetime
from typing import Optional, Iterable

import requests

DATE_PATTERN = "%Y-%m-%d"

class CurrencyValidationError(ValueError):
    ...

class CurrencyAPI:
    BASE_URL = "https://api.frankfurter.dev/v1"

    def __init__(self):
        self.supported_currencies = self.get_supported_currencies()

    def get_supported_currencies(self):
        try:
            response = requests.get(f"{self.BASE_URL}/currencies")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            raise CurrencyValidationError(f"API returned error status: {status_code}. Details: {e}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network or connection error: {e}")


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
        invalid = [c for c in currencies if c not in self.supported_currencies]
        if invalid:
            raise CurrencyValidationError(f"Unsupported currency codes: {",".join(invalid)}")

    @staticmethod
    def validate_date(date: str):
        """Check if date is in form 1999-01-04"""
        try:
            for d in date.split(".."):
                datetime.strptime(d, DATE_PATTERN)
        except ValueError:
            raise CurrencyValidationError(f"Invalid date: {", ".join(date)}")