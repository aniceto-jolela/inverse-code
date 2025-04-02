import unittest
from inverse_code.convert import coct


class TestConvertOctal(unittest.TestCase):
    """Test Convert Octal"""

    def coct_decimal(self):
        """[0 to 377]"""
        self.assertEqual(
            coct.coct_decimal(377),
            255,
        )

    def coct_hexadeciaml(self):
        """[0 to ff]"""
        self.assertEqual(coct.coct_hexadecimal(336), "fff")

    def coct_binary(self):
        """[0 to 1111]"""
        self.assertEqual(coct.coct_binary(255), "11111111")

    def coct_symbol(self):
        """[sp to del]"""
        self.assertEqual(coct.coct_symbol(32), " ")


if __name__ == "__main__":
    unittest.main()
