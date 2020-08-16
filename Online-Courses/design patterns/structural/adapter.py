'''
Adapter is translate an interface into another one , a client is expecting
example: server have speak_korea() and speak_british(), but a client want speak()
'''


class Korean:
    """Korean speaker"""
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong"


class British:
    """ english speaker"""

    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"


class Adapter:
    """this change the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """change the name of the method"""
        self.object = object

        # add a new dictionary that establish mapping between generic method name: speak() and concrete method
        # ex. speak() will be translate to speak_korean() if mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """simple return the rest of attribute"""
        return getattr(self.object, attr)


# list to store speaker objects
objects = []

# create the korean object
korean = Korean()

# create the british objects
british = British()

# mapped the objects to the objects list
objects.append(Adapter(korean, speak = korean.speak_korean))
objects.append(Adapter(british, speak = british.speak_english))

for obj in objects:
    print("{} says {} \n ".format(obj.name, obj.speak()))