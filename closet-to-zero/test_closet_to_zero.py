from closet_to_zero import closet_to_zero
import unittest


class TestCloset(unittest.TestCase):

    def test_global_function(self):
        self.assertEqual(1, closet_to_zero([-1, 1, 2, 3, 4]))
        self.assertEqual(-2, closet_to_zero([10, 3, 7, -3, -2, 100]))
        self.assertEqual(100, closet_to_zero([200, 500, -1000, -200, 100, 101]))
        self.assertIsNone(None, closet_to_zero([]))
        self.assertEqual(8, closet_to_zero([8]))
        self.assertEqual(2.1, closet_to_zero([9.3, -2.1, -8, 5.5, 2.1, 9.1]))
                          



if __name__ == '__main__':
    unittest.main()  # pragma: no cover
