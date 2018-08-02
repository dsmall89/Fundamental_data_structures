class Node(object):


    def __init__(self,input_value):
        self.left = None
        self.right = None
        self.input_value = input_value

    def __eq__(self, other):
        # Node() is an instance of an node, not the class node which represented as Node
        # issue was I was checking for compatiablities of types, which often general practice with an eq method

        return isinstance(other, Node) and self.input_value == other.input_value

    def __repr__(self):
        return "Node(value = %s)" % self.input_value

    def insert(self, input_value):
        if self.input_value == input_value:
            return None


        if input_value < self.input_value:
            if self.left:
                return self.left.insert(input_value)
            else:
                self.left = Node(input_value)
        else:
            if self.right:
                return self.right.insert(input_value)
            else:
                self.right = Node(input_value)


    def in_order_iteration(self):
        if self.left:
            for left_child in self.left.in_order_iteration():
                yield left_child
        yield self
        if self.right:
            for right_child in self.right.in_order_iteration():
                yield right_child

    def in_order(self, fn):
            if self.left :
                self.left.in_order(fn)
            fn(self)
            if self.right:
                self.right.in_order(fn)

    def post_order(self, fn):
        if self:
            if self.left:
                self.left.post_order(fn)

            if self.right:
                self.right.post_order(fn)
        fn(self)

    def pre_order(self, fn):


        fn(self)
        if self:
            if self.left:
                self.left.pre_order(fn)

            if self.right:
                self.right.pre_order(fn)


    def min_input_value_node(self,node):
        current= node
        while(current.left is not None):
            current = current.left
            return current

    def delete(self, input_value):
        #root is the top Node
        # "input_value" refers to the input element/node that needs to be deleted !!!
        # Here is the base case, if there is No root, return Nothing !!!
        if self is None:
            return None
        # if the input_value is less than the root's input_value, we know it is located in the left subtree !!!
        #mport pdb; pdb.set_trace()

        if input_value < self.input_value:
            self.left = self.left.delete(input_value)

        # if the input_value is less than the root's input_value, we know it is located in the "right" subtree !!!
        elif input_value > self.input_value :
            self.right = self.right.delete(input_value)

        else:
             if self.left is None:
                 temp = self.right
                 self = None
                 return temp
             elif self.right is None:
                   temp = self.left
                   self = None
                   return temp

             temp = min_input_value_node(self.right)
             self.input_value = temp.input_value
             self.right = self.right.delete(temp.input_value)

        return self

    def search(self, input_value):
        if(input_value == self.input_value):
            return self

        elif(input_value < self.input_value):
            if self.left:
                return self.left.search(input_value)
        else:
            if self.right:
                return  self.right.search(input_value)








# def printPreorder(root ):
#     if root:
#         # First print the data of Node
#          print(root.input_value),
#         #Then recur on left child
#          printPreorder(root.left)
#         #Finally recur on right child
#          printPreorder(root.right)





if __name__ == '__main__':
    tree = Node(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)

    def print_it(n):
        print(n),

    print("\nPre_order ")
    tree.pre_order(print_it)
    print("")
    print("\nIn_order ")
    tree.in_order(print_it)
    print("")
    print("\nPost_order")
    tree.post_order(print_it)

    print("\n")
    #import pdb; pdb.set_trace()
    tree.delete(5)
    tree.post_order(print_it)
    print("\n")
    print(tree.search(2))







#
# print("Preorder traversal of binary tree is")
# printPreorder(root)

# print("\nInorder traversal of binary tree is")

#
# print("\nPostorder traversal of binary tree is")
# printPostorder(root)


# root = root.delete(root, 50)
# print_Inorder(root)
