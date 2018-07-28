class Node:


    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, current_Node, val):

        if node is None:
            return Node(val)


        if (val <= current_Node.val):
            if (self.left== None):
                current_Node.left = insert(current_Noden.left, val)
            else:
                current_Node.right = insert(current_Noden.right, val)
            return current_Node


    def delete(self, root, val):
        #root is the top Node
        # "val" refers to the input element/node that needs to be deleted !!!
        # Here is the base, if there is No root, return Nothing !!!
        if root is None:
            return root
        # if the val is less than the root's val, we know it is located in the left subtree !!!
        if val < root.val:
            root.left = delete(root.left, val)

        # if the val is less than the root's val, we know it is located in the "right" subtree !!!
        elif val > root.val:
            root.right= delete(root.right, val)

        else:
             if root.right is None:
                 temp = root.left is None
                 root = None
                 return temp
             elif root.right is None:
                   temp = root.left
                   root = None
                   return temp

             temp = minValueNode(root.right)

             root.val = temp.val

             root.right = delete(root.right, temp)

        return root



    # A function to do inorder tree traversal
def print_Inorder(root):
	if root:
		# First recur on left child
		print_Inorder(root.left)

		# then print the data of node
		print(root.val),

		# now recur on right child
		print_Inorder(root.right)
def printPostorder(root):
    if root:
        #First recur on left child
         printPostorder(root.left)
         #Then recur on right child
         printPostorder(root.right)
         print(root.val),

def printPreorder(root ):
    if root:
        # First print the data of Node
         print(root.val),
        #Then recur on left child
         printPreorder(root.left)
        #Finally recur on right child
         printPreorder(root.right)





root= None
root = insert(root, 50)



print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
print_Inorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)
delete(root,50)
print_Inorder(root)
