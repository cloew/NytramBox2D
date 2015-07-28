from .engine import Box2DEngine
from .engine.body_def import BodyDef
from .transform import BodyTransform
from nytram.engine import EngineAttr

class Body:
    """ Represents a Box2D Body """
    entity = EngineAttr("applyTransform")
    
    def __init__(self, fixtures, **kwargs):
        """ Initialize the Body """
        self.id = None
        self.fixtures = fixtures
        self.bodyDef = BodyDef(**kwargs)
        
    def applyTransform(self):
        """ Apply the Body Transform """
        bodyTransform = BodyTransform(self.entity.transform)
        self.entity.transform = bodyTransform
        
    def start(self):
        """ Start the body in the Physics Engine """
        self.id = Box2DEngine.World_AddBody(self.world.id, self.bodyDef)
        
        for fixture in self.fixtures:
            fixture.addToBody(self)
        
    @property
    def world(self):
        """ Return the world this body is associated with """
        return self.entity.scene.world