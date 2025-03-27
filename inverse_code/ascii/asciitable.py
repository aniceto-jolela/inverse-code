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


@dataclasses.dataclass
class Hex:
    """Hex"""

    def __init__(self):
        self.__char = ["a", "b", "c", "d", "e", "f"]
        self.__num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__index_char = 0
        self.__index_char_static = 0
        self.__index_num = 0
        self.__n = 0
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
            if self.__start < 101:  # 0 to 100 sequence 0 to 9 of [a to f]
                if self.__n > 9 and self.__n <= 15:
                    self.__result = (
                        str(self.__num[self.__index_num])
                        + self.__char[self.__index_char]
                    )
                    self.__start -= 1
                    self.__index_char += 1
                if self.__n == 17:
                    self.__n = 1
                    self.__index_num += 1
                    self.__index_char = 0
                if self.__index_num > 9:
                    self.__index_num = 0
                if self.__n <= 9 or self.__n > 15:
                    self.__result = str(self.__start)
                if (
                    self.__start == 99 and self.__n == 15
                ):  # End first sequence and restart deta
                    self.__index_char = 0
                    self.__index_num = 0
                    self.__n = 0
                    self.__start += 1
                self.__n += 1
            else:  # 100 to 200 sequence a to f of [0 to 9]
                if self.__n > 10 and self.__n < 17:
                    self.__result = (
                        self.__char[self.__index_char_static]
                        + self.__char[self.__index_char]
                    )
                    self.__index_char += 1
                if self.__n == 17:
                    self.__n = 1
                    self.__index_char = 0
                    self.__index_num = 0
                    self.__index_char_static += 1
                if self.__n < 11:
                    self.__result = self.__char[self.__index_char_static] + str(
                        self.__num[self.__index_num]
                    )
                    self.__index_num += 1
                self.__n += 1
            self.__start += 1
            yield self.__result


class Bin:
    def __init__(self):
        self.__start = 0
        (
            self.__a,
            self.__b,
            self.__c,
            self.__d,
            self.__e,
            self.__f,
            self.__g,
            self.__h,
        ) = (0, 0, 0, 0, 0, 0, 0, 0)
        self.n0, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7 = (
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        )

    def code(self, numb):
        """Code bin"""
        while self.__start < numb:
            if self.n0 < 1:  # H
                self.__h = 0
                self.n0 += 1
            else:
                self.__h = 1
                self.n0 = 0

            if self.n1 < 2:  # G
                self.__g = 0
            else:
                self.__g = 1
                if self.n1 == 3:
                    self.n1 = self.n1 - 4

            if self.n2 < 4:  # F
                self.__f = 0
            else:
                self.__f = 1
                if self.n2 == 7:
                    self.n2 = self.n2 - 8

            if self.n3 < 8:  # E
                self.__e = 0
            else:
                self.__e = 1
                if self.n3 == 15:
                    self.n3 = self.n3 - 16

            if self.n4 < 16:  # D
                self.__d = 0
            else:
                self.__d = 1
                if self.n4 == 31:
                    self.n4 = self.n4 - 32

            if self.n5 < 32:  # C
                self.__c = 0
            else:
                self.__c = 1
                if self.n5 == 63:
                    self.n5 = self.n5 - 64

            if self.n6 < 64:  # B
                self.__b = 0
            else:
                self.__b = 1
                if self.n6 == 127:
                    self.n6 = self.n6 - 128

            if self.n7 < 128:  # A
                self.__a = 0
            else:
                self.__a = 1
                if self.n7 == 255:
                    self.n7 = self.n7 - 256

            result = (
                str(self.__a)
                + str(self.__b)
                + str(self.__c)
                + str(self.__d)
                + str(self.__e)
                + str(self.__f)
                + str(self.__g)
                + str(self.__h)
            )
            self.n1 += 1
            self.n2 += 1
            self.n3 += 1
            self.n4 += 1
            self.n5 += 1
            self.n6 += 1
            self.n7 += 1
            self.__start += 1
            yield result


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
