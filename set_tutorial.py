class set_tutorial(object):

    def __init__(self, *args):
      self.__dict = {}
      for arg in args:
        self.add(arg)

    def __repr__(self):
        import string
        elems = map(repr,self.__dict.keys( ))
        elems.sort( )
        return "%s" % (self.__dict)

    def extend(self, args):
        for arg in args:
            self.add(arg)

    def add(self, item):
        self.__dict[item] = item
