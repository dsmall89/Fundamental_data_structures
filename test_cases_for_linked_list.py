import unittest
from LinkedList import Node,linkedList

class linked_List_Tests(unittest.TestCase):
    def setUp(self):
        self.list= linkedList()


    def test_insert_one_element(self):
        self.list.insert_a_new_node_into_the_list("z")
        self.assertTrue(self.list.head.get_data()== 'z')

    def test_insert_two_element(self):
        self.list.insert_a_new_node_into_the_list("apple")
        self.list.insert_a_new_node_into_the_list("Mango")
        # Bottom-up stack
        self.assertTrue(self.list.head.get_data()== "Mango")

        next_element = self.list.head.get_next()
        self.assertTrue(next_element.get_data()== "apple")




if __name__ == '__main__':
    unittest.main()
