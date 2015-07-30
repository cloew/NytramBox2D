from .body import Body
from .engine import BodyTypes, Vec2
from .joints import WeldJoint

from kao_decorators import proxy_for
from nytram.engine import EngineAttr

@proxy_for("dynamicBody", ["id", "world", "mass", "position", "velocity", "applyImpulse"])
class PlayerBody:
    """ Represents a Player's Body that is bound to a dynamic and kinematic body """
    entity = EngineAttr("attachEntityToBodies")
    
    def __init__(self, fixtures, kinematicFixtures=None, **kwargs):
        """ Initialize the Body """
        if kinematicFixtures is None:
            kinematicFixtures = fixtures
        self.dynamicBody = Body(fixtures, bodyType=BodyTypes.Dynamic, **kwargs)
        self.kinematicBody = Body(kinematicFixtures, wrapTransform=False, bodyType=BodyTypes.Kinematic, **kwargs)
        self.joint = WeldJoint(self.dynamicBody, self.kinematicBody, Vec2(0, 0))
        
    def attachEntityToBodies(self):
        """ Attach the entity to the boides """
        self.dynamicBody.entity = self.entity
        self.kinematicBody.entity = self.entity
        
    def start(self):
        """ Start the body in the Physics Engine """
        self.dynamicBody.start()
        self.kinematicBody.start()
        self.joint.anchor = Vec2(self.position.x, self.position.y)
        self.joint.apply()