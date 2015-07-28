from ..engine import Box2DEngine

class BodyTransform:
    """ Represents a transform that uses its bodies position to determine its location """
    
    def __init__(self, graphicalTransform):
        """ Initialize the Body Transform with the graphical transform to wrap """
        self.graphicalTransform = graphicalTransform
        
    def update(self):
        """ Update the body transform """
        position = self.getCurrentPosition()
        self.graphicalTransform.position.assign(x=position.x, y=position.y)
        
    def getCurrentPosition(self):
        """ Return the current position """
        return Box2DEngine.Body_GetPosition(self.body.id).contents
        
    @property
    def body(self):
        """ Return the related body """
        return self.entity.body