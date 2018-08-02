class hashmap(object):
    def __init__(self, size=8):
        self.buckets = self.init_storage(size)
        self.count = 0 

    def set(self,key, value):
        bucket = self.bucket(key)

        if bucket.has_key(key):
            bucket.update(key,value)
        else:
            bucket.append(key,value)
            self.count +=1

        if self.count > self.num_buckets():
            self.resize()

        return size

    def init_storage(self,num_buckets):
        storage = []
        if num_buckets  < 8:
           num_buckets = 8
        while len(storage) < num_buckets:
            storage.append(linkedList())

            return storage
