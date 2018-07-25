class Node(object):

    def __init__(self, data = None, next_node= None):
        self.data =  data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_pointer_to_next_node(self, new_next):
        self.next_node = new_next

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

    def to_string(self):
        return "Node value :" + str(self.data)


class LinkedList(object):

    def __init__(self, head = None):
        self.head = head

    def insert_a_new_node_into_the_list(self, data):
        new_node = Node(data)
        new_node.set_pointer_to_next_node(self.head)
        self.head = new_node
 # Returns size of list
    def return_size_of_list(self):
        current_item_in_list = self.head
        count = 0
        while current_item_in_list:
            count += 1
            current_item_in_list = current_item_in_list.get_next()
        return count

    #Searches list for a node containing the data and returns that node if found.
    def search(self, data):
        current_item_in_list = self.head
        found = False
        while current_item_in_list and found is False:
            if current_item_in_list.get_data() == data:
                found = True
            else:
                current_item_in_list = current_item_in_list.get_next()
        if current_item_in_list is None:
            raise ValueError("Data not in list")
        return current_item_in_list
    #searches list for a node containing the requested data and
    #removes it from list if found.
    def delete(self, data):
        current_item_in_list = self.head
        previous = None
        found = False
        while current_item_in_list and found is False:
            if current_item_in_list.get_data() == data:
                found = True
            else:
                previous = current_item_in_list
                current_item_in_list = current_item_in_list.get_next()

        if current_item_in_list is None:
            raise ValueError("Data not in list")

        if previous is None:
            self.head = current_item_in_list.get_next()
        else:
            previous.set_pointer_to_next_node(current_item_in_list.get_next())

    def remove_duplicates(self,data):
        current_item_in_list = self.head
        second = None
        while current_item_in_list is not None:

            while second.get_next() is not None:
                if second.get_next().get_data() == current_item_in_list.get_data():


                else:
                    the_second_node = second.get_next()
                current_item_in_list = second= current_item_in_list.get_next()



#Prints out the values in a LinkedList
    def print_list(self):
        print("Print List.........")
        if self.head is None:
            return
        this_node= self.head
        print(this_node.to_string())

        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.to_string())
#Original list
# a-> a->b-> c -> d -> e -> e

def main():
    l = LinkedList()
    l.insert_a_new_node_into_the_list("a")
    l.insert_a_new_node_into_the_list("a")
    l.insert_a_new_node_into_the_list("b")
    l.insert_a_new_node_into_the_list("c")
    l.insert_a_new_node_into_the_list("d")
    l.insert_a_new_node_into_the_list("e")
    l.insert_a_new_node_into_the_list("e")
    l.print_list()

    l.remove_duplicates('a')
    l.print_list()

main()
