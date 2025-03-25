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


class Hex:
    """Hex"""

    def __init__(self):
        self.__index_char = ["a", "b", "c", "d", "e", "f"]
        self.__index_num = 0
        self.__n = 0
        self.__reset = 0
        self.__start = 0
        self.__result = "0"

    def code(self, numb):
        """
        @NOTE: This generator returns a list of each `hexadecimal character` to its implementation
            is a little complex.\n
        `numb`: number of times that will be repeated.\n
        `self.__start`: it is the loop accountant.\n
        `self.__char` : it is the list of characters that will be implemented if you attach this\n
            condition (`if self.__n > 9 and self.__n <= 15`).\n
        `self.__n` : is the variable of hexadecimal control from `0 to 9` and from `a to f`
            that total `15 characters`. \n
        `self.__reset` : is the `index` that controls the `self.__char`'s list
            that goes from 0 to 5.\n
        `self.__result`: returns the result of each `character in string`.

        """
        while self.__start < numb:
            if self.__n > 9 and self.__n <= 15:
                self.__result = str(self.__index_num) + self.__index_char[self.__reset]
                self.__start -= 1
                self.__reset += 1
            if self.__n == 17:
                self.__n = 1
                self.__reset = 0
                self.__index_num += 1
            if self.__n <= 9 or self.__n > 15:
                self.__result = str(self.__start)
            self.__start += 1
            self.__n += 1
            yield self.__result


class Bin: ...


class HtmlNumber: ...


class HtmlName: ...


class Symbol:
    """ "TODO"""

    def __init__(self):
        self.__symbol = [
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
        ]

    def code(self): ...
