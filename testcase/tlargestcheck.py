import unittest
from testlargest import largest


class LargestTest(unittest.TestCase):
    def testlargest1(self):
        self.assertEqual(largest(1, 2, 0), 2)

    def testlargest2(self):
        self.assertEqual(largest(15, 21, 50), 50)

    def testlargest3(self):
        self.assertEqual(largest(12.1, 12.2, 12.3), 12.3)

    def testlargest4(self):
        self.assertEqual(largest(24.6, 24.2, 23.9), 24.6)

    def testlargest5(self):
        self.assertEqual(largest("a", "b", 23.9), "Error")
