"""
ASCII Table
Reference to ASCII Table of Windows-1252
"""

class Dec:
    def __init__(self):
        self.__n = 0


    def characters_code_0_31(self, numb):
        while self.__n < numb:
            yield self.__n
            self.__n += 1



class Oct:
    pass



class Hex:
    pass



class Bin:
    pass



class Symbol:
    pass


class HtmlNumber:
    pass


class HtmlName:
    pass