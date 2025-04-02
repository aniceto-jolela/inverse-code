import unittest
from .test_convert_bin import TestConvertBinary


def suite():
    """@NOTE: return all tests"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestConvertBinary("cbin_decimal"),
            TestConvertBinary("cbin_octal"),
            TestConvertBinary("cbin_hexadecimal"),
            TestConvertBinary("cbin_symbol"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
