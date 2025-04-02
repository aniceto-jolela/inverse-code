import unittest
from inverse_code.convert import csymb


class TestConvertSymbol(unittest.TestCase):
    """Test Convert Symbol"""

    def csymb_octal(self):
        """[40 to 177]"""
        self.assertEqual(
            csymb.csymb_octal("?"),
            77,
        )

    def csymb_decimal(self):
        """[32 to 127]"""
        self.assertEqual(csymb.csymb_decimal("z"), 122)

    def csymb_hexadecimal(self):
        """[20 to 7f]"""
        self.assertEqual(csymb.csymb_hexadecimal("="), "3d")

    def csymb_binary(self):
        """[00100000 to 01111111]"""
        self.assertEqual(csymb.csymb_binary("{"), "01111011")


if __name__ == "__main__":
    unittest.main()
