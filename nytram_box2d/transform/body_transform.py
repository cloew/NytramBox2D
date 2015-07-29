from .body_position import BodyPosition
from ..engine import Box2DEngine
from kao_decorators import proxy_for

@proxy_for("graphicalTransform", ["scale", "rotation"])
class BodyTransform:
    """ Represents a transform that uses its bodies position to determine its location """
    
    def __init__(self, graphicalTransform):
        """ Initialize the Body Transform with the graphical transform to wrap """
        self.graphicalTransform = graphicalTransform
        self.started = False
        self.position = self.graphicalTransform.position
        
    def start(self):
        """ Start the body transform """
        self.started = True
        self.wrapPosition()
        
    def update(self):
        """ Update the body transform """
        position = self.getCurrentPosition()
        # print("Updating Body position:", position)
        self.graphicalTransform.position.assign(x=position.x, y=position.y)
        
    def getCurrentPosition(self):
        """ Return the current position """
        return Box2DEngine.Body_GetPosition(self.body.id).contents
        
    @property
    def body(self):
        """ Return the related body """
        return self.entity.body
    
    @property
    def position(self):
        """ Return the position """
        return self.__position
    
    @position.setter
    def position(self, value):
        """ Set the x value of the position """
        self.graphicalTransform.position = value
        if self.started:
            self.wrapPosition()
        else:
            self.__position = self.graphicalTransform.position
            
        
    def wrapPosition(self):
        """ Wrap the position """
        self.__position = BodyPosition(self.graphicalTransform.position, self.body)