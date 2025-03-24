import unittest
from inverse_code.ascii.win1252 import Win1252, Oct


class TestWin1252(unittest.TestCase):
    """
    Perform the complex operation on the value `initial` using the `memo` value.
    @NOTE: Don't forget how complex this operation is. Detail it here!
    @TODO: We still need to handle this additional complexity, which we'll capture here.
    @FIXME: I'm using an ugly workaround in this method, which I'll detail like so.
    """

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

    def test_oct_000_037(self):
        self.assertNotIn(
            Win1252.ControlCharacters.oct_000_037(self),
            Win1252.ControlCharacters().oct_000_037(),
        )

    def test_oct_040_177(self):
        self.assertListEqual(
            Win1252.PrintableCharacters.oct_040_177(self),
            Win1252.PrintableCharacters().oct_040_177(),
        )

    def test_oct_200_377(self):
        self.assertEqual(
            Win1252.ExtendedAsciiCodes.oct_200_377(self),
            list(Oct().code(378, 200)),
        )


if __name__ == "__main__":
    unittest.main()
