import unittest
from LinkedList import Node,linkedList
from Hashmap import HashMap_practice

class hashmap_test(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap_practice()
        self.example_element= {'Donte' : 'Smallest',
                                'Tanice': 'Smaller',
                                'Nahleen' : 'Small'}


    def test_set_element_in_hash_map(self):
        self.hash_map['Donte'] = self.example_element['Donte']
        self.assertEqual(self.example_element['Donte'],self.hash_map['Donte'])


    #def test_element_is_not_in_hash_map(self):
        # self.assertTrue("Biggie" not in self.hash_map)
        #
        # self.hash_map['Biggie']
        # self.assertTrue("Biggie" in self.hash_map)



    def test_delete_one_elments(self):
        self.hash_map['Donte'] = self.example_element['Donte']

        self.hash_map.delete('Donte')


        self.assertIsNone(self.hash_map['Donte'])
        self.assertTrue(self.example_element['Donte'])


        # self.hash_map['Donte'] = self.example_element['Tanice']
        self.hash_map.__setitem__('Donte','smallest')
        self.assertEqual(self.hash_map['Donte'],self.example_element['Tanice'])

    # def test_delete_one_elment_not_in_hash(self):
    #     with self.assertRaises(KeyError):
    #         del self.hash_map['Chris']



    #dup shows up or dont show up

    # def test_get_one_element_in_hash_map(self):
    #     get_hash = hashcontainer_of_hashed_elements()
    #     result= get_hash.__set__(2,"val1")
    #     result2=result.get_item(2)



    def test_count_is_correct(self):
        pass

    def test_count_decreases_after_element_is_deleted(self):
        pass








if __name__ == "__main__":
    unittest.main()
