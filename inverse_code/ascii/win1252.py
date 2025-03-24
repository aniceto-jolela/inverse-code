from .asciitable import Dec, Oct


class Win1252:
    """
    ASCII, stands for American Standard Code for Information Interchange.
    This class shows the extended ASCII table which is based on the Windows-1252 character set which is an 8 bit ASCII table with 256 characters and symbols.
    It includes all ASCII codes from standard ASCII, and it is a superset of ISO 8859-1 in terms of printable characters.
    In the range 128 to 159 (hex 80 to 9F), ISO/IEC 8859-1 has invisible control characters, while Windows-1252 has writable characters. Windows-1252 is probably the most-used 8-bit character encoding in the world.
    """

    def __init__(self):
        pass

    class ControlCharacters:
        """
        ASCII control characters (character code 0-31)
        The first 32 characters in the ASCII-table are unprintable control codes and are used to control peripherals such as printers.
        """

        def dec_0_31(self):
            result = list(Dec().characters_code(32))
            return result

        def oct_000_037(self):
            result = [x for x in Oct().code(38)]
            return result

    class PrintableCharacters:
        """
        ASCII printable characters (character code 32-127)
        Codes 32-127 are common for all the different variations of the ASCII table, they are called printable characters, represent letters, digits, punctuation marks, and a few miscellaneous symbols. You will find almost every character on your keyboard. Character 127 represents the command DEL.
        """

        def dec_32_127(self):
            result = [x + 32 for x in Dec().characters_code(96)]
            return result

        def oct_040_177(self):
            result = [x + 40 for x in Oct().code(140)]
            return result

    class ExtendedAsciiCodes:
        """
        There are several different variations of the 8-bit ASCII table.
        The table below is according to Windows-1252 (CP-1252) which is a superset of ISO 8859-1,
        also called ISO Latin-1, in terms of printable characters, but differs from the IANA's ISO-8859-1 by using displayable characters rather than control characters in the 128 to 159 range. Characters that differ from ISO-8859-1 is marked by light blue color.
        """

        def dec_128_255(self):
            result = [x + 128 for x in Dec().characters_code(128)]
            return result
