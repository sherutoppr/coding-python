'''
used then we want to
    1: add new features to an existing objects
    2: dynamic change
    3: not using subclasses
solution:
    1: function is also an objects in python
    2: using build-in decorator @
'''
from functools import wraps


def make_blink(function):
    """define the decorator"""

    # this makes the decorator transparent in terms of name and docstrings
    @wraps(function)
    # define the inner function
    def decorator():
        # grab the return value
        ret = function()

        # add the functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator


# apply the decorator here
@make_blink
def hello():
    """original function"""
    return "Hello World!"


# check the result of decorating
print(hello())

# check if the function name is still the same as before
print(hello.__name__)

# check if the docstring same as the before applying the decoratior
print(hello.__doc__)

