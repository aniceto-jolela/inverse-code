import unittest
from .test_hex_00_ff import TestHex00ff


def suite():
    suite_ = unittest.TestSuite()
    suite_.addTests([TestHex00ff("test_success")])
    return suite_


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
