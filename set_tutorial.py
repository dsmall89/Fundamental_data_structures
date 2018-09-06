import string
class set_tutorial(object):

    def __init__(self, *args):
      #allows that function to accept an arbitrary number of arguments
      self.__dict = HashTable 
      for arg in args:
        self.add(arg)

    def __repr__(self):
        elems = map(repr,self.__dict.keys( ))
        elems.sort( )
        return "%s" % (self.__dict )

    def extend(self, args):
        for arg in args:
            self.add(arg)

    def add(self, item):
        self.__dict[item] = item


    def remove(self, item):
        del self.__dict[item]


    def __len__(self):
        return iter(self.__dict.copy())

    def difference(self,item):
        pass
