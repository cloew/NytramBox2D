from ..engine import Box2DEngine, Vec2
from nytram.engine import EngineAttr

from ctypes import byref
from kao_decorators import proxy_for

@proxy_for("graphicalPosition", ["z", "__repr__"])
class BodyPosition:
    """ Represents a body position """
    body = EngineAttr("setPhysicsPosition")
    
    def __init__(self, graphicalPosition, body):
        """ Initialize the body position """
        self.graphicalPosition = graphicalPosition
        self.body = body
        
    def assign(self, x=None, y=None):
        """ Assign the position """
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
    
    @property
    def x(self):
        """ Return the x value of the position """
        return self.graphicalPosition.x
    
    @x.setter
    def x(self, value):
        """ Set the x value of the position """
        self.graphicalPosition.x = value
        self.setPhysicsPosition()
    
    @property
    def y(self):
        """ Return the y value of the position """
        return self.graphicalPosition.y
    
    @y.setter
    def y(self, value):
        """ Set the y value of the position """
        self.graphicalPosition.y = value
        self.setPhysicsPosition()
        
    @property
    def vec2Position(self):
        """ Return the Vector form of the position """
        return Vec2(self.x, self.y)
        
    def setPhysicsPosition(self):
        """ Set the Physics Position """
        if self.body.id:
            self.body.setPositionInPhysicsEngine(self.vec2Position)