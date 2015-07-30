from .filter import Filter
from ctypes import Structure, c_void_p, c_bool, c_float

class FixtureDef(Structure):
    """ Represents the definition of a Fixture in Box2D """
    _fields_ = [("userData", c_void_p),
                ("friction", c_float),
                ("restitution", c_float),
                ("density", c_float),
                ("isSensor", c_bool),
                ("filter", Filter)]
                
    def __init__(self, **kwargs):
        """ Initialize the Fixture Def """
        if "filter" not in kwargs:
            kwargs["filter"] = Filter()
        
        Structure.__init__(self, **kwargs)