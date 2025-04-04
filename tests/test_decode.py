import unittest
from inverse_code import decode


class TestDecode(unittest.TestCase):
    """List test"""

    def test_decode(self):
        """success"""
        self.assertDictEqual(decode.decode(251792692), 251792692)


if __name__ == "__main__":
    unittest.main()
