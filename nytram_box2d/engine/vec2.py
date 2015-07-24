from ctypes import Structure, c_float

class Vec2(Structure):
    """ Represents a Box 2D Vector """
    _fields_ = [("x", c_float),
                ("y", c_float)]
    
    def __repr__(self):
        """ Return the string representation """
        return "Vec2({0}, {1})".format(self.x, self.y)