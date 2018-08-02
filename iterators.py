class NaturalNumbers(object):
  def __iter__(self):
    self.count = 0
    return self

  def next(self):
    self.count = self.count + 1
    return self.count

