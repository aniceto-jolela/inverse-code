import unittest
from inverse_code.convert import chex


class TestConvertHexadecimal(unittest.TestCase):
    """Test Convert Hexadecimal"""

    def chex_octal(self):
        """[0 to 377]"""
        self.assertEqual(
            chex.chex_octal("ff"),
            377,
        )

    def chex_decimal(self):
        """[0 to ff]"""
        self.assertEqual(chex.chex_decimal("8c"), 140)

    def chex_binary(self):
        """[0 to 1111]"""
        self.assertEqual(chex.chex_binary("da"), "11011010")

    def chex_symbol(self):
        """[sp to del]"""
        self.assertEqual(chex.chex_symbol("4b"), "K")


if __name__ == "__main__":
    unittest.main()
