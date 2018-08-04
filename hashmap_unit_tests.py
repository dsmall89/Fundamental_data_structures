import unittest
from LinkedList import Node,linkedList
from Hashmap import hashcontainer_of_hashed_elements

class hashmap_test(unittest.TestCase):
    def setUp(self):
        self.hash_map = hashcontainer_of_hashed_elements()


    def test_set_element_in_hash_map(self):
        set_hash = hashcontainer_of_hashed_elements()
        result= set_hash.__set__("key1","val1")
        self.assertTrue("key1" and "val1" in result[0])

    def test_element_is_not_in_hash_map(self):
        self.assertTrue("Biggie" is not self.hash_map)



    def test_set_two_elments(self):
            pass

    def test_get_one_element_in_hash_map(self):
        get_hash = hashcontainer_of_hashed_elements()
        result= get_hash.__set__(2,"val1")
        result2=result.get_item(2)

        self.assertTrue(result2 == 2)


    def test_count_is_correct(self):
        pass

    def test_count_decreases_after_element_is_deleted(self):
        pass








if __name__ == "__main__":
    unittest.main()
