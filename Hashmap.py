
from LinkedList import linkedList,Node

class hashcontainer_of_hashed_elements(object):
    def __init__(self):
        self.size = 8
        self.container_of_hashed_elements= [None] * self.size

    def __set__(self,key, value):

        indx_of_key_value = self.__get__(key)
        value = [key,value]

        if self.container_of_hashed_elements[indx_of_key_value] is None:
            self.container_of_hashed_elements[indx_of_key_value] = list([value])
        else:
            for pair in self.container_of_hashed_elements[indx_of_key_value]:
                if pair[0] == key:
                    pair[1] = value
                    return True

    def __repr__(self):
        return str(self.container_of_hashed_elements)
    def has_key(self,key):
        pass


    def __get__(self,key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size


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
    print(h)
    #h.delete(13)
    print("Was removed")
    print(h)
main()
