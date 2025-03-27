import unittest
from inverse_code.ascii.win1252 import Win1252, Bin


class TestBin01(unittest.TestCase):
    """Test Bin number"""

    def test_success(self):
        self.assertDictEqual(Win1252.bin_01(self), Bin().code(255))


if __name__ == "__main__":
    unittest.main()
