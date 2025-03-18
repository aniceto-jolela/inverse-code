import unittest
from inverse_code.ascii.win1252 import Win1252


class TestWin1252(unittest.TestCase):

    def test_dec(self):
        self.assertEqual(Win1252.Control_Characters.dec_0_31(self), Win1252.Control_Characters().dec_0_31())


if __name__ == "__main__":
    unittest.main()
    