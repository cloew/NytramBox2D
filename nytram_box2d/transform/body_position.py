from ..engine import Box2DEngine
from nytram.engine import EngineAttr
from kao_decorators import proxy_for

@proxy_for("graphicalPosition", ["z"])
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
        
    def setPhysicsPosition(self):
        """ Set the Physics Position """
        if self.body.id:
            Box2DEngine.Body_SetPosition(self.body.id, self.graphicalPosition.x, self.graphicalPosition.y)