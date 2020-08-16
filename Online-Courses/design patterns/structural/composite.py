'''
it maintain the tree data structure to represent part-whole relationships
solution:
    component : abstract class
    child : concrete class inherit from this component class
    composite : concrete class inherit from this component class and maintain child object by adding and removing them
                to a tree data structure
    --> decorator, visitor, and iterator is related to composite design patterns

'''


class Component(object):
    """Abstract class"""
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    """concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of your child items
        self.name = args[0]

    def component_function(self):
        # print the name of your child item here
        print('{}'.format(self.name))


class Composite(Component):
    """concrete class """

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of the composite objects
        self.name = args[0]

        # this is where we keep our child items
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        # print the name of the composite objects here
        print('{}'.format(self.name))

        # iterate through the child objects and invoke their component function
        for i in self.children:
            i.component_function()


# build a composite menu 1
sub1 = Composite("submenu1")

# create a new child sub_submenu11
sub11 = Child("sub_submenu11")

# create a new child sub_submenu12
sub12 = Child("sub_submenu12")

sub1.append_child(sub11)
sub1.append_child(sub12)

# build a top-level composite menu
top = Composite("top_menu")

# create submenu 2 that is not composite
sub2 = Child("submenu2")

# add child menu to parent menu
top.append_child(sub1)
top.append_child(sub2)

# test is our composite pattern works
top.component_function()
