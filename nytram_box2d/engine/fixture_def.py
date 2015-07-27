from ctypes import Structure, c_void_p, c_bool, c_float

class FixtureDef(Structure):
    """ Represents the definition of a Fixture in Box2D """
    _fields_ = [("userData", c_void_p),
                ("restitution", c_float),
                ("density", c_float),
                ("isSensor", c_bool)]
    
    