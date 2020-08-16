'''
A factory pattern used to create the lots of object.
Example - > we already have dog class, what if we have new cat class, then parret class
            we just need to ask for object for that pet, that's all!!
'''


class Dog:
    """A simple dog class"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "bhauu!!"


class Cat:
    """A simple cat class"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "meow!!"


def get_pet(pet="dog"):
    """A factory method"""
    pets = dict(dog=Dog("sheru"), cat=Cat("heena"))
    return pets[pet]


# i want cat object
c = get_pet('cat')
print(c.speak())

# suppose i want dog object
d = get_pet('dog')
print(d.speak())
