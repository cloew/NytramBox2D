from .engine import Box2DEngine
from .engine.body_def import BodyDef

class Body:
    """ Represents a Box2D Body """
    
    def __init__(self, fixtures, **kwargs):
        """ Initialize the Body """
        self.id = None
        self.fixtures = fixtures
        self.bodyDef = BodyDef(**kwargs)
        
    @property
    def position(self):
        """ Return the position """
        return Box2DEngine.Body_GetPosition(self.id).contents
        
    def start(self):
        """ Start the body in the Physics Engine """
        self.id = Box2DEngine.World_AddBody(self.world.id, self.bodyDef)
        
        for fixture in self.fixtures:
            fixture.addToBody(self)
        
    @property
    def world(self):
        """ Return the world this body is associated with """
        return self.entity.scene.world