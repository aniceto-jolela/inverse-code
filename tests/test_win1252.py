import unittest
from inverse_code.ascii.win1252 import Win1252


class TestWin1252(unittest.TestCase):
   

    def test_dec_0_31(self):
        self.assertEqual(Win1252.Control_Characters.dec_0_31(self), Win1252.Control_Characters().dec_0_31())


    def test_dec_32_127(self):
        self.assertEqual(Win1252.Printable_Characters.dec_32_127(self), Win1252.Printable_Characters().dec_32_127())

    def test_dec_128_255(self):
        self.assertEqual(Win1252.Extended_Ascii_codes.dec_128_255(self), Win1252.Extended_Ascii_codes().dec_128_255())

if __name__ == "__main__":
    unittest.main()
    