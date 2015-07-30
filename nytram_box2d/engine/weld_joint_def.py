from .vec2 import Vec2
from ctypes import Structure, c_uint

class WeldJointDef(Structure):
    """ Represents the definition for a Weld Joint """
    _fields_ = [("bodyAId", c_uint),
                ("bodyBId", c_unit),
                ("anchor", Vec2)]