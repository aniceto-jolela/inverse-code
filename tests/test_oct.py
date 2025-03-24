import unittest
from .test_oct_000_037 import TestDec0377


def suite():
    suite_ = unittest.TestSuite()
    suite_.addTests(
        [
            TestDec0377("test_success"),
        ]
    )
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
