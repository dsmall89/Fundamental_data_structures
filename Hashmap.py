
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
    def __init__(self, initial_values = []):
        self.index = 0
        self.container = HashTable()

        for v in initial_values:
            self.add(v)


    def add(self,item):
        self.container[item] = item

    def __contains__(self,item):
        # it passed, Yay !!!
        return item in self.container

    def __len__(self):
        return len(self.container)

    def __iter__(self):
        for k, _ in self.container:
            yield k

    #     return iterator
    #
    # def __next__(self):
    #     if self.index >= len(self.container):
    #         raise StopIteration
    #
    #     obj = self.container[self.index]
    #     self.index += 1
    #     return obj
    #
    #     for k, _ in self.container:
    #         yield k

    def __eq__(self, other):
        return  isinstance(other,HashTable) and self.container == other.container

    def isSubset(self,set1):
        # true if each element in self is in set1
        for element in self:
            if element not in set1:
                return False
        return True

    def __repr__(self):
        #self.container=

        return str(self.container)

    def isSuperSet(self, set1):

        #Should simply return TRUE OR False
        for element in set1:
            if element not in self:
                return False
        return True

    def union(self, set1):
        bucket = HashSet()
        for idx in self:
            bucket.add(idx)
                #should copy all the values into bucket
        for other in set1:
            if other not in self:
                bucket.add(other)
                        #should check if value is not in self,
                        #then add value to bucket
        # s = [ x for x in self if x in set1 ]
        return  bucket


    def intersect(self,set1):
        if len(set1) > len(self):
            set1,self = self,set1
        li_dif = [i for i in self if i in self and i in set1]
        return li_dif

    def my_difference(self,other):
            bucket = []
            for item in self:

                if item not in other:
                    bucket.append(item)
            return bucket
    def map(my_function, my_list):
        result = []
        for i in my_list:
            result.append(my_function(i))
        return result



class HashTable(object):
    def __init__(self):
            #pigeonhole principle, used when you have more than one item in a bucket
            #it gets counted correctly !
        self.size = 8
        self._buckets = [[] for _ in range(0, self.size)]

    def __len__(self):
        return sum(len(b) for b in self._buckets)

    def __iter__(self):
        #just need to iterate over the key value

         for bucket in self._buckets:
             for pair in bucket:
                 yield pair


    def get_hash(self,key):
        hash = 0
        for character in str(key):
            hash += ord(character)
            calculatated_hash_ref_num_in_buckets = hash % self.size

        return calculatated_hash_ref_num_in_buckets

    def __setitem__(self, key, value):
        key_index = self.get_hash(key)
        new_pair = [key, value]

        # At this point, there's already a bucket with items
        # So we iterate through the _buckets
        for pair in self._buckets[key_index]:
            if pair[0] == key:
                pair[1] = value
                #only returns if we found a match, per 125 (match found!)
                return
        self._buckets[key_index].append(new_pair)
            # if the key is not in the bucket we add it to the bucket
            # Note that if there's a hash collision we don't add the item

    def __repr__(self):
        return str(self._buckets)

    def __getitem__(self, key):
        key_index = self.get_hash(key)
        for pair in self._buckets[key_index]:
            if pair[0] == key:
                return pair[1]

        raise KeyError(key)
        #important lesson here regrading writing unittest, if you expect to raise a KeyError then it has to be present
        #Also,None is a good choice to return but the unittest is expecting you to raise a KeyError given a test case


    def delete(self,key):
        key_index = self.get_hash(key)

        for index in range (0,len(self._buckets[key_index])):
            if self._buckets[key_index][index][0] == key:
                self._buckets[key_index].pop(index)
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
