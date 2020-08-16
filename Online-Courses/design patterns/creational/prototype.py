'''
    used when we have to create lots of identical objects, so instead of creating lot's of objects , it clone it
    solution:
    step 1: create a prototypical instance first
    step 2: simple clone it whenever you need replical
'''
import copy


class Prototype:

    def __init__(self):
        """create a dict objects that contain all the objects that will be clone"""
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """clone a registered object and update its attribute"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "skylark"
        self.color = "red"
        self.options = "ex"

    def __str__(self):
        return '{} | {} | {} '.format(self.name, self.color, self.options)


# first instantiate the car class
c = Car()

# create the instance of prototype class
prototype = Prototype()
prototype.register_object("skylark",c)

# create the clone of register class
c1 = prototype.clone("skylark")
print(c1)