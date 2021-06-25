
import re

PHONE_NUMBER_FORMAT = re.compile(
    r"""(?x)
    ^\s*                        # leading whitespace
    \W?(?P<country>1?)          # NANP country code
    \W*(?P<area>[2-9]\d{2})     # area code
    \W*(?P<exchange>[2-9]\d{2}) # exchange code
    \W*(?P<subscriber>\d{4})    # subscriber number
    \s*$                        # trailing whitespace
    """
)


class PhoneNumber:

    def __init__(self, number):
        match = PHONE_NUMBER_FORMAT.fullmatch(number)
        if not match:
            raise ValueError("Invalid phone number")
        groups = match.group(2, 3, 4)
        self.number = "".join(groups)
        self.area_code, self.exchange_code, self.subscriber = groups

    def pretty(self):
        """
        Pretty print the phone number
        Returns a string of the form "(NXX)-NXX-XXXX"
        """
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber}"