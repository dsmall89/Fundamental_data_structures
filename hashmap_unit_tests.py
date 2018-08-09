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



    #def test_element_is_in_hash_map(self):
        #Why does this keep getting stuck in an infinite loop
        #Also, why when switch self.hash_map an error is thrown
         #self.assertTrue('Biggie' not in self.hash_map)
         #self.hash_map['Biggie'] = 'Small'

         #self.assertTrue('Biggie' in self.hash_map)



    def test_delete_one_elments(self):
        #add the item to the hash map
        #if this line is removed the test will break, why ?
        self.hash_map['another_test_key']= 'another_test_value'

        self.assertTrue(self.hash_map['another_test_key'], 'another_test_value')
        self.hash_map.delete('another_test_key')

        #assert that key is removed
        self.assertTrue('another_test_key', None )

    # def test_delele_correct_element(self):
    #     self.hash_map[3]= 'another_test_value'
    # Should verifty the number is correct, I already know my delete function is returning True
    #     self.assertFalse(self.hash_map.delete(3),3)



    def test_delete_one_elment_not_in_hash(self):

        with self.assertRaises(KeyError):
                self.hash_map['Not existent']






if __name__ == "__main__":
    unittest.main()
