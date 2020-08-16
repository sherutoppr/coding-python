''':arg
the bridge pattern helps untangle an unnecessary complicated class hierarchy
    -> two unrelated, parallel, or orthogonal abstraction-one is implementation-specific
        and other is implementation-independent
solution : separate the abstractions into two different class hierarchy
'''


class DrawAPIOne(object):
    """implementation-specific abstraction:  concrete class one"""
    def draw_circle(self, x, y, radius):
        print("API 1st draw circle at {} , {} with radius {}".format(x, y, radius))


class DrawAPITwo(object):
    """implementation-specific abstraction:  concrete class TWO"""
    def draw_circle(self, x, y, radius):
        print("API 2nd draw circle at {} , {} with radius {}".format(x, y, radius))


class Circle(object):
    """implementation- independent abstraction"""
    def __init__(self, x, y, radius, drawing_api):
        """initialize the necessary attribute"""
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """implementation-specific"""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """implementation-independent"""
        self._radius *= percent


#  build the circle by api 1
circle1 = Circle(1, 2, 3, DrawAPIOne())
circle1.draw()

circle2 = Circle(2, 3, 4, DrawAPITwo())
circle2.draw()
