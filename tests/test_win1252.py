import unittest
from inverse_code.ascii.win1252 import Win1252


class TestWin1252(unittest.TestCase):

    def test_dec_0_31(self):
        self.assertCountEqual(
            Win1252.ControlCharacters.dec_0_31(self),
            Win1252.ControlCharacters().dec_0_31(),
        )

    def test_dec_32_127(self):
        self.assertListEqual(
            Win1252.PrintableCharacters.dec_32_127(self),
            Win1252.PrintableCharacters().dec_32_127(),
        )

    def test_dec_128_255(self):
        self.assertCountEqual(
            Win1252.ExtendedAsciiCodes.dec_128_255(self),
            Win1252.ExtendedAsciiCodes().dec_128_255(),
        )

    def tet_oct_000_037(self):
        self.assertTupleEqual(
            Win1252.ControlCharacters.oct_000_037(self),
            Win1252.ControlCharacters().oct_000_037(),
        )

    def tet_oct_040_177(self):
        self.assertTupleEqual(
            Win1252.PrintableCharacters.oct_040_177(self),
            Win1252.PrintableCharacters().oct_040_177(),
        )


if __name__ == "__main__":
    unittest.main()
