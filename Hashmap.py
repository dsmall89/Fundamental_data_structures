
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

        self.count = 0
        self.container= HashTable()


    def add(self,item):
        self.container[item] = item

    def __contains__(self,item):
        # it passed, Yay !!!
        return item in self.container

    def __len__(self):
        return len(self.container)

    def __iter__(self):

        return iter(self.container)

    def next(self):
      self.count += 1
      if self.count > self.container:
          raise StopIteration
      else:
          for x in self:
              yield x

    def isSubset(self,set2):
        set1 = self.container
        for item in set1 and set2:

            if item in set2:
                return True
            else:
                return False
    def __repr__(self):
        return str(self.container)

    def isSuperSet(self, set1, set2):
        set1 = self.container

        for item in set2:
            if item in set1:
                return True
            else:
                return False

    def union(self, set1):
        bucket = []
        for i in self:
            #should copy all the values into bucket
            if i in set1 or self:
                    #should check if value is not in self,
                    #then add value bucket
                bucket.append(i)
            else:
                return False
        return bucket





    def intersect(self,set1,set2):
        if len(set1) > len(set2):
            set1,set2 = set2,set1

            result = self.container
            for item in set1 :
                if item in set2:
                    result.add(item)
            return result

    def my_difference(self,other):
        try:
            for item in self.container:
                for item in other:
                    if item not in other:
                        self.container.add(item)
            return self.container
        except KeyError:
            return False


class HashTable(object):
    def __init__(self):
            #pigeonhole principle, used when you have more than one item in a bucket
            #it gets counted correctly !
        self.size = 8
        self.__bucket = [[] for _ in range(0, self.size)]
    def __iter__(self):
        return self

    def __len__(self):
        return sum(len(b) for b in self.__bucket)
    def __iter__(self):
        return iter(self.__bucket)


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
        # So we iterate through the __bucket
        for pair in self.__bucket[key_index]:
            if pair[0] == key:
                pair[1] = value
                #only returns if we found a match, per 125 (match found!)
                return
        self.__bucket[key_index].append(new_pair)
            # if the key is not in the bucket we add it to the bucket
            # Note that if there's a hash collision we don't add the item

    def __repr__(self):
        return str(self.__bucket)

    def __getitem__(self, key):
        key_index = self.get_hash(key)
        for pair in self.__bucket[key_index]:
            if pair[0] == key:
                return pair[1]

        raise KeyError(key)
        #important lesson here regrading writing unittest, if you expect to raise a KeyError then it has to be present
        #Also,None is a good choice to return but the unittest is expecting you to raise a KeyError given a test case
    def __repr__(self):
        return "Hash (value = %s)" % self.__bucket


    def delete(self,key):
        key_index = self.get_hash(key)

        for index in range (0,len(self.__bucket[key_index])):
            if self.__bucket[key_index][index][0] == key:
                self.__bucket[key_index].pop(index)
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
