from ..engine import Box2DEngine

from ctypes import c_float

class Box:
    """ Represents a box shape for a fixture """
    
    def __init__(self, width=0, height=0):
        """ Initialize the Box """
        self.width = width
        self.height = height
        
    def apply(self, body, fixtureDef):
        """ Apply the shape and fixture definition to the body """
        return Box2DEngine.Body_AddBoxFixture(body.id, fixtureDef, self.width, self.height)