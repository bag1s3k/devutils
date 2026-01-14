BASE_API_URL = "https://api.frankfurter.dev/v1"


class Currency:

    def __init__(self, base=None, to=None, amount=None, crc=None):
        self.base = base
        self.to = to
        self.amount = amount
        self.crc= crc

    def specific_crc(self, crc_override=None):
        """ Generates the API endpoint URL with an optional CRC override.
            :param crc_override: CRC to override
            :return: complete formatted API URL string"""
        crc = crc_override or self.crc

        if crc:
            return f"{BASE_API_URL}/latest?base={crc}"
        else:
            return f"{BASE_API_URL}/latest"

if "__main__" == __name__:
    currency = Currency()
    print(currency.specific_crc())