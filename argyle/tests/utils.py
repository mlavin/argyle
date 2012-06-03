"Test helper utility methods."

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class ArgyleTest(unittest.TestCase):
    "Common test base."
