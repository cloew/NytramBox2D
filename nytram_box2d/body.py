from .engine import Box2DEngine, Vec2
from .engine.body_def import BodyDef
from .transform import BodyTransform

from nytram.engine import EngineAttr

from ctypes import byref

class Body:
    """ Represents a Box2D Body """
    entity = EngineAttr("applyTransform")
    
    def __init__(self, fixtures, wrapTransform=True, **kwargs):
        """ Initialize the Body """
        self.id = None
        self.fixtures = fixtures
        self.bodyDef = BodyDef(**kwargs)
        self.wrapTransform = wrapTransform
        
    def applyTransform(self):
        """ Apply the Body Transform """
        if self.wrapTransform:
            bodyTransform = BodyTransform(self.entity.transform)
            self.entity.transform = bodyTransform
        
    def start(self):
        """ Start the body in the Physics Engine """
        self.bodyDef.position = Vec2(self.position.x, self.position.y)
        self.id = Box2DEngine.World_AddBody(self.world.id, self.bodyDef)
        
        for fixture in self.fixtures:
            fixture.addToBody(self)
            
    def applyImpulse(self, impulse):
        """ Apply the impulse """
        Box2DEngine.Body_ApplyImpulse(self.id, byref(impulse))
        
    @property
    def world(self):
        """ Return the world this body is associated with """
        return self.entity.scene.world
        
    @property
    def mass(self):
        """ Return the body's current mass """
        return Box2DEngine.Body_GetMass(self.id)
        
    @property
    def position(self):
        """ Return the body's matching transform position """
        return self.entity.transform.position
        
    @property
    def velocity(self):
        """ Return the body's current velocity """
        return Box2DEngine.Body_GetVelocity(self.id).contents
        
    def getPositionInPhysicsEngine(self):
        """ Get the position in the physics engine """
        return Box2DEngine.Body_GetPosition(self.id).contents
        
    def setPositionInPhysicsEngine(self, position):
        """ Set the position in the physics engine """
        Box2DEngine.Body_SetPosition(self.id, byref(position))