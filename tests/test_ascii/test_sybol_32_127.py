import unittest
from inverse_code.ascii.win1252 import Win1252, Symbol


class TestSymbol(unittest.TestCase):
    """Test Symbol number"""

    def test_success(self):
        """return success"""
        self.assertEqual(Win1252.symbol_32_127(self), list(Symbol().code(95)))

    def test_non_number(self):
        """@NOTE: Expect a TypeError for non-numeric inputs"""
        with self.assertRaises(TypeError):
            list(Symbol().code("95"))

    def test_maximum_number(self):
        """@NOTE: The maximum number of this list is 95"""
        with self.assertRaises(ValueError):
            self.assertEqual(Win1252.symbol_32_127(self), list(Symbol().code(96)))


if __name__ == "__main__":
    unittest.main()
