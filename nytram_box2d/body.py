from .engine import Box2DEngine
from .engine.body_def import BodyDef

class Body:
    """ Represents a Box2D Body """
    
    def __init__(self, world, **kwargs):
        """ Initialize the Body """
        self.id = Box2DEngine.World_AddBody(world.id, BodyDef(**kwargs))
        
    @property
    def position(self):
        """ Return the position """
        return Box2DEngine.Body_GetPosition(self.id).contents