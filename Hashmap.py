
from LinkedList import linkedList,Node

class hashcontainer_of_hashed_elements(object):
    def __init__(self):
        self.size = 4
        self.container_of_hashed_elements= [None] * self.size

    def __set__(self,key, value):
        # gets the key
        indx_of_key_value = self.__get__(key)

        #creates key + value pairs
        value = [key,value]

        if self.container_of_hashed_elements[indx_of_key_value] is None:

            #sets the empty container to list of "key" "value"
            self.container_of_hashed_elements[indx_of_key_value] = list([value])
            assigned_value = self.container_of_hashed_elements[indx_of_key_value]
            return assigned_value

        else:
            # if not empty, check if element at indx[0] equals key
            print self.container_of_hashed_elements[indx_of_key_value],
            for pair in self.container_of_hashed_elements[indx_of_key_value]:

                if pair[0] == key:
                    print(pair[0])
                    # if so, then the element at indx[1] corresponds to its value
                    pair[1] = value
                    return True

    def __repr__(self):
        return str(self.container_of_hashed_elements)
    def has_key(self,key):
        pass

    def __get__(self,key):
        hash = 0
        for indx_value in str(key):
            hash += ord(indx_value)
            calculatated_values = hash % self.size

        return calculatated_values
    def get_item(self,key):
        key_value = self.__get__(key)
        if self.container_of_hashed_elements[key_value] is not None:

            for pair in self.container_of_hashed_elements[key_value]:

                if pair[0] == key:
                    return pair[1]
        return None





    def delete(self,key):
        value = self.__get__(key)
        if self.container_of_hashed_elements[value] != None:
            if isinstance(self.container_of_hashed_elements[value], list):
                #import pdb; pdb.set_trace()
                indx = self.container_of_hashed_elements[value].index(key)
                self.container_of_hashed_elements[value][indx] = None
            else:
                keyError()

def main():
    h = hashcontainer_of_hashed_elements()
    h.__set__(10,"Nope")
    h.__set__(13,"Almost")
    h.__set__(12,"Gone")
    h.get_item(12)
    print(h)
    #h.delete(13)
    print(h.get_item(10))
