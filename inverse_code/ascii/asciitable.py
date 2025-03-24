"""
ASCII Table
Reference to ASCII Table of Windows-1252
"""


class Dec:
    """Dec 0 to 31"""

    def __init__(self):
        self.__n = 0

    def characters_code_0_31(self, numb):
        """charecters_code_31"""
        while self.__n < numb:
            yield self.__n
            self.__n += 1

    def characters_code_32_127(self, numb):
        """charecters_code_31"""
        while self.__n < numb:
            yield self.__n
            self.__n += 1

    def charcters_code_128_255(self, numb):
        """charecters_code_31"""
        while self.__n < numb:
            yield self.__n
            self.__n += 1


class Oct:
    def __init__(self):
        self.__n = 0
        self.__reset = 0

    def code(self, numb):
        while self.__n < numb:
            yield self.__n
            if self.__reset == 7:
                self.__reset = self.__reset - 8
                self.__n += 2
            self.__reset += 1
            self.__n += 1


class Hex: ...


class Bin: ...


class Symbol: ...


class HtmlNumber: ...


class HtmlName: ...
