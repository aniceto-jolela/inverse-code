import unittest
from inverse_code.convert import cbin


class TestConvertBinary(unittest.TestCase):
    """Test Convert Binary"""

    def cbin_octal(self):
        """[0 to 377]"""
        self.assertEqual(
            cbin.cbin_octal("00011110"),
            36,
        )

    def cbin_decimal(self):
        """[0 to ff]"""
        self.assertEqual(cbin.cbin_decimal("11111111"), 255)

    def cbin_hexadecimal(self):
        """[0 to 1111]"""
        self.assertEqual(cbin.cbin_hexadecimal("10111011"), "bb")

    def cbin_symbol(self):
        """[sp to del]"""
        self.assertEqual(cbin.cbin_symbol("01101111"), "o")


if __name__ == "__main__":
    unittest.main()
