import unittest
from inverse_code.helpers import hexshow


class TestHelpersHex(unittest.TestCase):
    """Test Helpers Hexadeciaml 0 to ff"""

    def test_control_characters_0_01(self):
        """[0 to 1f]"""
        self.assertEqual(
            hexshow.control_characters_0_1f(),
            [x["hex"] for x in hexshow.Hex().code(21) if x["int"] < 21],
        )

    def test_printable_characters_20_7f(self):
        """[20 to 7f]"""
        self.assertEqual(
            hexshow.printable_characters_20_7f(),
            [
                x["hex"]
                for x in list(hexshow.Hex().code(81))
                if x["int"] > 20
                if x["int"] < 81
            ],
        )

    def test_extended_ascii_80_ff(self):
        """[80 to ff]"""
        self.assertEqual(
            hexshow.extended_ascii_80_ff(),
            [x["hex"] for x in hexshow.Hex().code(197) if x["int"] > 80],
        )

    def test_all(self):
        """lists all hexadecimal numbers."""
        self.assertEqual(
            hexshow.all_hexadecimal(), [x["hex"] for x in hexshow.Hex().code(197)]
        )


if __name__ == "__main__":
    unittest.main()
