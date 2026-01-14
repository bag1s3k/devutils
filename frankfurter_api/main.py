from typing import Optional


class Currency:

    def __init__(self, base=None, to=None, amount=None, crc=None, crcs=None):
        self.base = base
        self.to = to
        self.amount = amount
        self.crc = crc
        self.crcs = crcs
        self.BASE_API_URL = "https://api.frankfurter.dev/v1"

    def specific_crc(self, crc_override=None):
        """Generates the API endpoint URL with an optional CRC override."""
        crc = crc_override or self.crc

        if crc:
            return f"{self.BASE_API_URL}/latest?base={crc}"
        else:
            return f"{self.BASE_API_URL}/latest"


    def specific_crcs(self, crcs_override: Optional[list[str]] = None):
        """Generates the API endpoint URL with an optional CRCS override"""

        crcs = crcs_override or self.crcs
        if crcs:
            return f"{self.BASE_API_URL}/latest?symbols={",".join(crc for crc in crcs)}"
        else:
            return f"{self.BASE_API_URL}/latest"

if "__main__" == __name__:
    currency = Currency()
    print(currency.specific_crc())