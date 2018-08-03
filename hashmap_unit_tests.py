import unittest
from LinkedList import Node,linkedList
from Hashmap import hashmap

class hashmap_test(unittest.TestCase):
    def setUp(self):
        hash_map = hashmap()


    def test_set_element_in_hash_map(self):
        set_hash = hashmap()
        self.assertTrue(set_hash.__set__("key1","val1"))

    def test_set_two_elments(self):
            pass

    # def test_get_one_element_in_hash_map(self):
    #     get_hash = hashmap()
    #
    #     self.assertEqual(get_hash.___get__('2'),2)


    def test_count_is_correct(self):
        pass

    def test_count_decreases_after_element_is_deleted(self):
        pass








if __name__ == "__main__":
    unittest.main()
