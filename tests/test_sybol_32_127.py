import unittest
from inverse_code.ascii.win1252 import Win1252, Symbol


class TestSymbol(unittest.TestCase):
    def test_success(self):
        self.assertDictEqual(Win1252.symbol_32_127(self), Symbol().code(90))


if __name__ == "__main__":
    unittest.main()
