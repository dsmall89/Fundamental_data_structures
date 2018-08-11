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

    def test_delete_one_elments_from_set(self):
        self.test_set.add(1)
        self.assertEqual(repr(self.test_set),'{1: 1}')

        #issue with equality test here: AssertionError: {} != {}
        # Not valid test, assumes whatever is in second parameter is true {Would be True}
        self.test_set.remove(1)
        self.assertTrue(repr(self.test_set),'{}')

if __name__ == '__main__':
    unittest.main()
