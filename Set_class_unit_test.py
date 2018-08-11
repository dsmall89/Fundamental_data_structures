import unittest
from set_tutorial import set_tutorial


class set_Class_test(unittest.TestCase):

    def setUp(self):
        self.test_set = set_tutorial()

    def test_add_one_element_to_set(self):
        # Test can written way better but it passes for now !
        self.test_set.add(1)


        result = '{1: 1}'
        self.assertEqual(repr(self.test_set), result )

    # def test_delete_one_elments_from_set(self):
    #     self.A


if __name__ == '__main__':
    unittest.main()
