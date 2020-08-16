'''
the observer pattern set one-to-many relationship between subject and multiple observers.
solution:
    subject: abstract class with attach, detach, and notify functionality
    concrete subject:
'''


class Subject(object):

    def __init__(self):
        self._observers = []  # this where reference of all observers are being kept, one sub - many observer

    # if observer is not in list, append it
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    # notify to all observer except who create the change
    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name      # set the name of the core
        self._temp = 0     # initialize the temperature of the core

    @property   # getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter   # setter that set the core temperature
    def temp(self, temp):
        self._temp = temp
        self.notify()


class TempViewer:

    # alert method that is invoked when the notify() method in a concrete subject is invoked
    def update(self, subject):
        print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))


# create the subject or core
c1 = Core("core 1")
c2 = Core("core 2")

# let's create the viewer
v1 = TempViewer()
v2 = TempViewer()

# lets attach our observer to first core
c1.attach(v1)
c1.attach(v2)

# let's change the temperature of first core
c1.temp = 80
c1.temp = 90
