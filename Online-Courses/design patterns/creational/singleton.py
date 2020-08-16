'''
used when we want to create only one object of a class, only one

'''


class Borg:
    """borg class making class attribute global"""
    _shared_state = {}    # attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state    # make it an attribute dictionary


class Singleton(Borg):
    """ child class of borg class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # update the attribute dictionary by inserting the new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        return str(self._shared_state)


# let;s create the first object
x = Singleton(HTTP = "hypertext Text Transfer Protocol")
print(x)

# let's create another singleton object and check if it create total new object of borg or use old one
y = Singleton(SNMP = "simple Network Management Protocol")
print(y)


