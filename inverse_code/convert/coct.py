from inverse_code.error import MaximumNumber, NonNumber
from inverse_code.helpers import octshow, decshow, hexshow, binshow, symbshow


def coct_decimal(char):
    """convert octal to decimal"""
    index_oct = 0

    try:
        if char > 377:
            raise MaximumNumber(377)

        result = decshow.all_decimal()
        for x in octshow.all_octal():
            if char == x:
                break
            index_oct += 1
        return result[index_oct]

    except TypeError as e:
        raise NonNumber from e


def coct_hexadecimal(char):
    """convert decimal to hexadecimal"""

    try:
        if char > 375:
            raise MaximumNumber(375)

        result = hexshow.all_hexadecimal()
        return result[char]
    except TypeError as e:
        raise NonNumber from e


def coct_binary(char):
    """convert decimal to binary"""

    try:
        if char > 377:
            raise MaximumNumber(377)

        result = binshow.all_binary()
        return result[char]
    except TypeError as e:
        raise NonNumber from e


def coct_symbol(char):
    """
    convert decimal to symbol.\n
    @NOTE: Only values is allowed from `32` to `126`.
    """

    try:
        if char > 126:
            raise MaximumNumber(126)

        if char < 32:
            raise ValueError("Only values is allowed from 32 to 126.")

        result = symbshow.all_symbol()
        return result[char]
    except TypeError as e:
        raise NonNumber from e
