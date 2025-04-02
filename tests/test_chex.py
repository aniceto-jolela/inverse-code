import unittest
from .convert.test_convert_hex import TestConvertHexadecimal


def suite():
    """@NOTE: return all tests"""
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestConvertHexadecimal("chex_decimal"),
            TestConvertHexadecimal("chex_octal"),
            TestConvertHexadecimal("chex_binary"),
            TestConvertHexadecimal("chex_symbol"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
