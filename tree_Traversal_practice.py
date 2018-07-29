class Node(object):


    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

    def __eq__(self, other):
        return other is not None and self.val == other.val

    def __repr__(self):
        return "Node(val=%s)" % self.val

    def insert(self, val):
        if self.val == val:
            return None


        if val < self.val:
            if self.left:
                return self.left.insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                return self.right.insert(val)
            else:
                self.right = Node(val)


    def in_order(self, fn):
        if self:
            if self.left:
                self.left.in_order(fn)
            fn(self)
            if self.right:
                self.right.in_order(fn)



    def min_value_node(self,node):
        current= node
        while(current.left is not None):
            current = current.left
            return current

    def delete(self, root, val):
        #root is the top Node
        # "val" refers to the input element/node that needs to be deleted !!!
        # Here is the base case, if there is No root, return Nothing !!!
        if root is None:
            return root
        # if the val is less than the root's val, we know it is located in the left subtree !!!
        if val < root.val:
            root.left = self.delete(root.left, val)

        # if the val is less than the root's val, we know it is located in the "right" subtree !!!
        elif val > root.val:
            root.right= self.delete(root.right, val)

        else:
             if root.right is None:
                 temp = root.left is None
                 root = None
                 return temp
             elif root.right is None:
                   temp = root.left
                   root = None
                   return temp

             temp = min_Value_node(root.right)

             root.val = temp.val

             root.right = delete(root.right, temp)

        return root





# def printPostorder(root):
#     if root:
#         #First recur on left child
#          printPostorder(root.left)
#          #Then recur on right child
#          printPostorder(root.right)
#          print(root.val),

# def printPreorder(root ):
#     if root:
#         # First print the data of Node
#          print(root.val),
#         #Then recur on left child
#          printPreorder(root.left)
#         #Finally recur on right child
#          printPreorder(root.right)





if __name__ == '__main__':
    tree = Node(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(32)

    def print_it(n):
        print(n)

    tree.in_order(print_it)




#
# print("Preorder traversal of binary tree is")
# printPreorder(root)

# print("\nInorder traversal of binary tree is")

#
# print("\nPostorder traversal of binary tree is")
# printPostorder(root)


# root = root.delete(root, 50)
# print_Inorder(root)
