
from LinkedList import linkedList,Node

class HashMap(object):
    def __init__(self):
        self._table = HashTable()

    def __setitem__(self, key, value):
        self._table[key] = value
    #
    def __getitem__(self,key):
        #return self._table.__getitem__(key)
        return self._table[key]

    def __contains__(self,key):
        #think proxy
        return key in self._table

    def delete(self, key):
        return self._table.delete(key)

class HashSet(object):
    def __init__(self):
        self.container= HashTable()

    def add(self,item):
        self.container[item] = item

    def __contains__(self,item):
        # it passed, Yay !!!
        return item in self.container

    def count(self,item):
        return len(self.container)
    def issubset(self,set1, set2):
        set1 = self.container
        if set1 in set2:
            return True
        else:
            return False





class HashTable(object):
    def __init__(self):
        self.size = 8
        self.bucket_of_hashed_elements= [None] * self.size

    def get_hash(self,key):
        hash = 0
        for character in str(key):
            hash += ord(character)
            calculatated_hash_ref_num_in_buckets = hash % self.size

        return calculatated_hash_ref_num_in_buckets

    def __setitem__(self, key, value):
        key_index = self.get_hash(key)
        new_pair = [key, value]

        if self.bucket_of_hashed_elements[key_index] is None:
            #sets the empty container to list of "key" "value"
            self.bucket_of_hashed_elements[key_index] = list([new_pair])

        else:
            # if not empty, check if element at indx[0] equals key
            for pair in self.bucket_of_hashed_elements[key_index]:
                if pair[0] == key:
                    # if so, then the element at indx[1] corresponds to its value
                    pair[1] = value
                    self.map[key_index].append(new_pair)
                    return True
                # Note that if there's a hash collision we don't add the item

    def __repr__(self):
        return str(self.bucket_of_hashed_elements)


    def __getitem__(self,key,default = None):
        key_index = self.get_hash(key)
        if self.bucket_of_hashed_elements[key_index] is not None:

            for pair in self.bucket_of_hashed_elements[key_index]:
                if pair[0] == key:
                    return pair[1]
                else:
                    return default
        #import pdb; pdb.set_trace()

        raise KeyError(key)
        #important lesson here regrading writing unittest, if you expect to raise a KeyError then it has to be present
        #Also,None is a good choice to return but the unittest is expecting you to raise a KeyError given a test case
    def __repr__(self):
        return "Hash (value = %s)" % self.bucket_of_hashed_elements


    def delete(self,key):
        key_index = self.get_hash(key)
        if self.bucket_of_hashed_elements[key_index] is None:
            return None


        for index in range (0,len(self.bucket_of_hashed_elements[key_index])):
            if self.bucket_of_hashed_elements[key_index][index][0] == key:
                self.bucket_of_hashed_elements[key_index].pop(index)
                return True

        return None

    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def remove_empty_list(self,empty_list):
        empty_list = [t for t in  enum(empty_list) if t ]
        return empty_list



def main():
    h = HashMap_practice()
    h.__setitem__(10,"Nope")
    h.__setitem__(13,"Almost")
    h.__setitem__(12,"Gone")
    h.__getitem__(12)
    print(h)
    h.delete(13)
    print("Print New Hashmap")

    print(h)
    print(h.__getitem__(10))
