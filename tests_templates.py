import unittest


def average(*args):
    if not args:
        raise ValueError
    return sum(args) / len(args)


class TestTemplate(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average(1, 3), 2)
        self.assertEqual(average(1, 2, 6), 3)
        self.assertEqual(average(-2, 2), 0)
        self.assertEqual(average(0, 1), 0.5)
        self.assertRaises(ValueError, average)


unittest.main()
