from ctypes import Structure, c_float
import math

class Vec2(Structure):
    """ Represents a Box 2D Vector """
    _fields_ = [("x", c_float),
                ("y", c_float)]
    
    def __init__(self, x=0, y=0):
        """ Initialize the vector with each coordinate """
        self.onChange = None
        if hasattr(x, '__iter__'):
            x, y, *rest = x
        Structure.__init__(self, x=x, y=y)
    
    def __add__(self, other):
        """ Add two vectors of equal length """
        return Vec2(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        """ Add two vectors of equal length """
        return self + (-other)
    
    def __neg__(self):
        """ Negate a vector """
        return self*-1
    
    def __mul__(self, other):
        """ Add scalar multiplication to the vector """
        return Vec2(*[d*other for d in [self.x, self.y]])
    
    def __eq__(self, other):
        """ Compare 2 vectors for equality """
        return (self.x, self.y) == (other.x, other.y)
        
    @property
    def unitVector(self):
        """ Return a unit vector in the direction of this vector """
        magnitude = self.magnitude
        return Vec2(self.x/magnitude, self.y/magnitude)
        
    @property
    def magnitude(self):
        """ Return the magnitude of the vector """
        return math.sqrt(self.x**2 + self.y**2)
    
    def __repr__(self):
        """ Return the string representation """
        return "Vec2({0}, {1})".format(self.x, self.y)