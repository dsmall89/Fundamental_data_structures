import unittest
from LinkedList import Node,linkedList
from Hashmap import hashmap

class hashmap_test(unittest.TestCase):
    def setUp(self):
        hash_map = hashmap(4)


    def test_set_element_in_hash_map(self):
        set_hash= hashmap(4)
        self.assertTrue(set_hash.set("key1","val1"))







if __name__ == "__main__":
    unittest.main()
