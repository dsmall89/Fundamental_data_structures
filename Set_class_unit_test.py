import unittest
from set_tutorial import set_tutorial


class set_Class_test(unittest.TestCase):

    def setUp(self):
        self._a_Set = set_tutorial()

    def test_add_one_element_to_set(self):
        # Test can written way better but it passes for now !
        self._a_Set.add('1')
        result = {'1': '1'}
        self.assertEqual(self._a_Set,result )

    # def test_delete_one_elments_from_set(self):
    #     self.A


if __name__ == '__main__':
    unittest.main()
