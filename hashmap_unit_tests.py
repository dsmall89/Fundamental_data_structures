import unittest
from LinkedList import Node,linkedList
from Hashmap import HashMap,HashSet,HashTable


class hashmap_test(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap()
        self.example_element= {'Donte' : 'Smallest',
                                'Tanice': 'Smaller',
                                'Nahleen' : 'Small'}


    def test_set_element_in_hash_map(self):
        self.hash_map['Donte'] = self.example_element['Donte']
        self.assertEqual(self.example_element['Donte'],self.hash_map['Donte'])



    def test_element_is_in_hash_map(self):
        # Why does this keep getting stuck in an infinite loop
        # Also, why when switch self.hash_map an error is thrown
         self.assertTrue('Biggie' not in self.hash_map)
         self.hash_map['Biggie'] = 'Small'

         self.assertTrue('Biggie' in self.hash_map)



    def test_delete_one_elments(self):
        #add the item to the hash map
        #if this line is removed the test will break, why ?
        self.hash_map['another_test_key']= 'another_test_value'

        self.assertEqual(self.hash_map['another_test_key'], 'another_test_value')
        self.hash_map.delete('another_test_key')

        #assert that key is removed
        self.assertNotIn('another_test_key', self.hash_map )

    # def test_delele_correct_element(self):
    #     self.hash_map[3]= 'another_test_value'
    # Should verifty the number is correct, I already know my delete function is returning True
    #     self.assertFalse(self.hash_map.delete(3),3)



    def test_delete_one_elment_not_in_hash(self):


        with self.assertRaises(KeyError):
                self.hash_map['Not existent']

class HashTableTest(unittest.TestCase):
    def test_next_with_one_item_returns_key_and_value(self):
        t = HashTable()
        t["Donte"] = "Small"
        i = iter(t)
        pair = next(i)
        self.assertEqual(["Donte", "Small"], pair)


class HashSetTest(unittest.TestCase):
    def setUp(self):
        self.set = HashSet()

    def test_added_item_is_in_set(self):
        s = HashSet()
        s.add("Donte")
        self.assertIn("Donte", s)

    def test_union_of_sets(self):

        sx = HashSet()
        sx.add("1")
        sx.add("2")
        sx.add("4")
        sx.add("6")

        dx = HashSet()
        dx.add("1")
        dx.add("3")
        dx.add("5")
        dx.add("7")
        result = [1,2,3,4,5,7]
        self.assertEqual(sx.union(dx), result)

    def test_if_subset(self):
        s = HashSet()
        s.add("{1,2,3}")
        d = {1,2,3,4,5,6,7}

        self.assertIn(s.isSubset(d),d)

    # def test_if_difference(self):
    #     s = HashSet()
    #     s.add({'a', 'b', 'c', 'd'})
    #     d = {'c', 'f', 'g'}
    #     result = {'b', 'a', 'd'}
    #     self.assertEqual(s.my_difference(d), result)
    def test_len_is_zero(self):
        s= HashSet()
        self.assertEqual(len(s),0)

    def test_len_method(self):
        s = HashSet()
        s.add("One")
        self.assertEqual(len(s),1)

    def test_len_with_multiple_items(self):
        s = HashSet()
        s.add("One")
        s.add("two")
        s.add("three")

        self.assertEqual(len(s),3)

    def test_if_two_in_same_bucket(self):
        s= HashSet()
        s.add("one")
        self.assertIn("one", s)
        s.add("two")
        self.assertIn("one", s)
        self.assertIn("two", s)

    def test_doesnt_misidentify_an_item_with_the_same_hash(self):
        # We assume one and two have the same hash
        self.assertEquals(self.set.container.get_hash("one"), self.set.container.get_hash("two"))

        self.set.add("one")
        self.assertIn("one", self.set)
        self.assertNotIn("two", self.set)

    def test_len_with_multiple_items_in_two_buckets(self):

        s = HashSet()
        s.add("One")
        s.add("two")
        s.add("three")
        self.assertEqual(len(s),3)

        s2=HashSet()
        s2.add("four")
        s2.add("five")
        s2.add("six")
        s2.add("seven")
        self.assertEqual(len(s2),4)



    def test_iteration(self):
        for house, saying in self.example_element.items():
            self.hashmap[house] = saying

        for house, saying in self.hashmap:
            self.assertEqual(self.example_element[house], saying)

    def test_next(self):
        s4 = HashSet()
        s4.add('MoveOut')


        it = iter(s4)
        result = next(it)

        self.assertEqual("MoveOut", result)










if __name__ == "__main__":
    unittest.main()
