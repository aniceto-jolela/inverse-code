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


if __name__ == "__main__":
    unittest.main()
