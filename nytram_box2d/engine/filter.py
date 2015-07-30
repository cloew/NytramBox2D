from ctypes import Structure, c_int16, c_uint16

class Filter(Structure):
    """ Represents a Fixture filter """
    _fields_ = [("categoryBits", c_uint16),
                ("maskBits", c_uint16),
                ("groupIndex", c_int16)]
                
    def __init__(self, categoryBits=0x1, maskBits=0xFFFF, groupIndex=0):
        """ Initialize the filter with the proper defaults """
        Structure.__init__(self, categoryBits=categoryBits, maskBits=maskBits, groupIndex=groupIndex)