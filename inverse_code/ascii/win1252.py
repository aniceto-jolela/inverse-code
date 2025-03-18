from .asciitable import Dec


class Win1252:
    """
    ASCII, stands for American Standard Code for Information Interchange.
    This class shows the extended ASCII table which is based on the Windows-1252 character set which is an 8 bit ASCII table with 256 characters and symbols.
    It includes all ASCII codes from standard ASCII, and it is a superset of ISO 8859-1 in terms of printable characters.
    In the range 128 to 159 (hex 80 to 9F), ISO/IEC 8859-1 has invisible control characters, while Windows-1252 has writable characters. Windows-1252 is probably the most-used 8-bit character encoding in the world.
    """
    def __init__(self):
        pass
    
    class Control_Characters:
        """
        ASCII control characters (character code 0-31)
        The first 32 characters in the ASCII-table are unprintable control codes and are used to control peripherals such as printers.
        """
        def __init__(self):
            Dec.__init__(self)


        def dec_0_31(self):
            result = [x for x in Dec().characters_code_0_31(31)]
            return result




