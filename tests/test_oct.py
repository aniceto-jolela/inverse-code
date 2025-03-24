import unittest
from .test_win1252 import TestWin1252


def suite():
    suite = unittest.TestSuite()
    suite.addTests([TestWin1252("tet_oct_000_037"), TestWin1252("tet_oct_040_177")])
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())