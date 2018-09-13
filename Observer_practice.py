def synchronized(method):
    def f(*args):
        self = args[0]
        self.mutex.acquire();
        # print(method.__name__, 'acquired')
        try:
            return apply(method, args)
        finally:
            self.mutex.release();
            # print(method.__name__, 'released')
    return f

def synchronize(klass, names=None):

    if type(names)==type(''): names = names.split()
    for (name, val) in klass.__dict__.items():
        if callable(val) and name != '__init__' and \
          (names == None or name in names):
            # print("synchronizing", name)
            klass.__dict__[name] = synchronized(val)

class Synchronization:
    def __init__(self):
        self.mutex = threading.RLock()

class Observer:
  def update(observable, arg):
      pass

class Observable(Synchronization):
    def __init__(self):
         self.obs = []
         self.changed= 0
         Synchronization.__init__(self)
    def addObserver(self,observer):
        if observer not in self.obs:
            self.obs.append(observer)

    def deleteObserver(self,observer):
        self.obs.remove(observer)

    def notifyObserver(self,arg = None):
        self.mutex.acquire()
        try:
            self.clearChanged()
        finally:
            self.mutex.release()

            for observer in localArray:
                observer.update(self,arg)

    def deleteObservers(self):
         self.obs = []
    def setChanged(self):
        self.changed = 1
    def clearChanged(self):
        self.changed = 0
    def hasChanged(self):
        return self.changed
    def countObservers(self):
        return len(self.obs)


synchronize(Observable,
  "addObserver deleteObserver deleteObservers " +
  "setChanged clearChanged hasChanged " +
  "countObservers")
