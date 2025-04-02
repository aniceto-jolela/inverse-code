import unittest
from inverse_code.convert import cdec


class TestConvertDecimal(unittest.TestCase):
    """Test Convert Decimal"""

    def cdec_octal(self):
        """[0 to 377]"""
        self.assertEqual(
            cdec.cdec_octal(255),
            377,
        )

    def cdec_hexadeciaml(self):
        """[0 to ff]"""
        self.assertEqual(cdec.cdec_hexadecimal(255), "ff")

    def cdec_binary(self):
        """[0 to 1111]"""
        self.assertEqual(cdec.cdec_binary(255), "11111111")

    def cdec_symbol(self):
        """[sp to del]"""
        self.assertEqual(cdec.cdec_symbol(32), " ")


if __name__ == "__main__":
    unittest.main()
