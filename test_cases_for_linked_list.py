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

    def test_deleted_value_is_removed_from_list(self):
        self.list.insert_a_new_node_into_the_list("The")
        self.list.insert_a_new_node_into_the_list("quick")
        self.list.insert_a_new_node_into_the_list("brown")
        self.list.insert_a_new_node_into_the_list("fox")

        self.list.delete("fox")
        self.assertTrue(self.list.head.get_data() == "brown")

        self.list.delete("The")
        self.list.delete("quick")
        self.assertTrue(self.list.head.get_next() is None )








if __name__ == '__main__':
    unittest.main()
