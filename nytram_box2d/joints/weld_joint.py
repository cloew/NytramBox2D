from ..engine import Box2DEngine, WeldJointDef

class WeldJoint:
    """ Represents a weld joint in the Box2D Engine """
    
    def __init__(self, bodyA, bodyB, anchor):
        """ Initialize the Weld Joint """
        self.bodyA = bodyA
        self.bodyB = bodyB
        self.anchor = anchor
        
    def apply(self):
        """ Apply the weld joint to the Physics Engine """
        self.jointDef = WeldJointDef(self.bodyA.id, self.bodyB.id, self.anchor)
        return Box2DEngine.Joint_AddWeldJoint(self.bodyA.world.id, self.jointDef)