from inverse_code.error import MaximumNumber
from inverse_code.helpers import octshow


def cdec_octal(char):
    """convert decimal to octal"""

    if char > 255:
        raise MaximumNumber(255)

    result = octshow.all_octal()
    return result[char]
