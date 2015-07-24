from .vec2 import Vec2
from ctypes import Structure, c_int, c_bool

class BodyDef(Structure):
    """ Represents the definition of a body """
    _fields_ = [("bodyType", c_int),
                ("position", Vec2),
                ("fixedRotation", c_bool)]