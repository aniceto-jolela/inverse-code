import unittest
from inverse_code.helpers import symbshow


class TestHelpersSymb(unittest.TestCase):
    """Test Helpers Symbol 32 to 127"""

    def test_printable_characters_32_127(self):
        """[32 to 127]"""
        self.assertEqual(
            symbshow.printable_characters_32_127(),
            [x["symb"] for x in symbshow.Symbol().code(128) if x["int"] > 32],
        )

    def test_all(self):
        """lists all symbol."""
        self.assertEqual(
            symbshow.all_symbol(), [x["symb"] for x in symbshow.Symbol().code(128)]
        )


if __name__ == "__main__":
    unittest.main()
