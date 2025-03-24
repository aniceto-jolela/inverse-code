import unittest
from .test_dec_0_255 import TestDec0255


def suite():
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestDec0255("test_success"),
            TestDec0255("test_negative_number"),
            TestDec0255("test_greater"),
            TestDec0255("test_float"),
            TestDec0255("test_non_number"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
