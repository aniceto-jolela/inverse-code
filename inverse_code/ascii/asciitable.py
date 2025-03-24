"""
ASCII Table
Reference to ASCII Table of Windows-1252
"""

import dataclasses


@dataclasses.dataclass
class Dec:
    """Dec 0 to 255"""

    def code(self, numb, start=0):
        """charecters_code_31"""
        while start < numb:
            yield start
            start += 1


@dataclasses.dataclass
class Oct:
    """Dec 0 to 378"""

    def __init__(self):
        self.__reset = 0

    def code(self, numb, start=0):
        """@TODO:"""
        while start < numb:
            yield start
            if self.__reset == 7:
                self.__reset = self.__reset - 8
                start += 2
            self.__reset += 1
            start += 1


class Hex: ...


class Bin: ...


class HtmlNumber: ...


class HtmlName: ...


class Symbol:
    """ "TODO"""

    def __init__(self):
        self.__symbol = (
            " ",
            "!",
            '"',
            "#",
            "$",
            "%",
            "&",
            "'",
            "(",
            ")",
            "*",
            "+",
            ",",
            "-",
            ".",
            "/",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            ":",
            ";",
            "<",
            "=",
            ">",
            "?",
            "@",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
        )

    def code(self): ...
