
from LinkedList import linkedList,Node

class HashMap_practice(object):
    def __init__(self):
        self.size = 8
        self.bucket_of_hashed_elements= [None] * self.size
    def get_hash(self,key):
        hash = 0
        for indx_hash_ref_num_in_bucket in str(key):
            hash += ord(indx_hash_ref_num_in_bucket)
            calculatated_hash_ref_num_in_buckets = hash % self.size

        return calculatated_hash_ref_num_in_buckets

    def __setitem__(self,key, hash_ref_num_in_bucket):
        # gets the key
        indx_of_key_hash_ref_num_in_bucket = self.get_hash(key)

        #creates key + hash_ref_num_in_bucket pairs
        hash_ref_num_in_bucket = [key,hash_ref_num_in_bucket]

        if self.bucket_of_hashed_elements[indx_of_key_hash_ref_num_in_bucket] is None:

            #sets the empty container to list of "key" "hash_ref_num_in_bucket"
            self.bucket_of_hashed_elements[indx_of_key_hash_ref_num_in_bucket] = list([hash_ref_num_in_bucket])


        else:
            # if not empty, check if element at indx[0] equals key
            print self.bucket_of_hashed_elements[indx_of_key_hash_ref_num_in_bucket],
            for pair in self.bucket_of_hashed_elements[indx_of_key_hash_ref_num_in_bucket]:

                if pair[0] == key:
                    print(pair[0])
                    # if so, then the element at indx[1] corresponds to its hash_ref_num_in_bucket
                    pair[1] = hash_ref_num_in_bucket
                    self.map[indx_of_key_hash_ref_num_in_bucket].append(key_hash_ref_num_in_bucket)
                    return True

    def __repr__(self):
        return str(self.bucket_of_hashed_elements)


    def __getitem__(self,key):
        key_hash_ref_num_in_bucket = self.get_hash(key)
        if self.bucket_of_hashed_elements[key_hash_ref_num_in_bucket] is not None:

            for pair in self.bucket_of_hashed_elements[key_hash_ref_num_in_bucket]:

                if pair[0] == key:
                    return pair[1]
        return None


    def delete(self,key):
        hash_ref_num_in_bucket = self.get_hash(key)
        if self.bucket_of_hashed_elements[hash_ref_num_in_bucket] is None:
            return None


        for index in range (0,len(self.bucket_of_hashed_elements[hash_ref_num_in_bucket])):
            if self.bucket_of_hashed_elements[hash_ref_num_in_bucket][index][0] == key:
                self.bucket_of_hashed_elements[hash_ref_num_in_bucket].pop(index)
                return True

        return None

    def __contain__(self, key):

        if self.__get__(key):
            return True
        else:
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
