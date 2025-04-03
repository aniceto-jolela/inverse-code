import unittest
from inverse_code import encode


class TestEncode(unittest.TestCase):
    """List test"""

    def test_encode(self):
        """success"""
        self.assertDictEqual(encode.encode("FRED"), [])


if __name__ == "__main__":
    unittest.main()
