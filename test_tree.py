from tree_Traversal_practice import Node
import unittest

class NodeInsertionTest(unittest.TestCase):
    def test_equality_if_values_are_equal_and_no_children(self):
        a = Node(5)
        b = Node(5)
        self.assertEquals(a, b)

    def test_not_equal_if_not_a_node(self):
        a = Node(5)
        b = "foo"
        self.assertNotEquals(a, b)
        self.assertNotEquals(b, a)

    def test_default_node_has_given_value_and_no_children(self):
        n = Node(5)
        self.assertEquals(5, n.val)
        self.assertEquals(None, n.left)
        self.assertEquals(None, n.right)

    def test_insert_less_than_root(self):
        root = Node(5)
        root.insert(4)
        self.assertEquals(Node(4), root.left)
        self.assertEquals(None, root.right)

    def test_insert_less_than_root_when_child_on_that_side_already(self):
        root = Node(5)
        root.insert(4)
        root.insert(3)
        self.assertEquals(Node(4), root.left)
        self.assertEquals(Node(3), root.left.left)
        self.assertEquals(None, root.right)

    def test_insert_greater_than_root(self):
        root= Node(5)
        root.insert(6)
        self.assertEquals(Node(6),root.right)
        self.assertEquals(None,root.left)

    def test_insert_greater_than_root_when_child_on_that_side_already(self):
        root = Node(5)
        root.insert(6)
        root.insert(7)
        self.assertEquals(Node(6), root.right)
        self.assertEquals(Node(7), root.right.right)
        self.assertEquals(None, root.left)

if __name__ == "__main__":
    unittest.main()
