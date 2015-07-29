from .axis import Axis

class InstantVelocity:
    """ Represents a method of providing an instant velocity """
    
    def __init__(self, speed, axis=Axis.Both):
        """ Initialize with the body speed and direction """
        self.speed = speed
        self.axis = axis
        
    def apply(self, body, direction):
        """ Apply the speed in the given direction to the given body """
        velocity = body.velocity
        impulse = (direction*self.speed - velocity)*body.mass
        
        if self.axis is Axis.Horizontal:
            impulse.y = 0
        elif self.axis is Axis.Vertical:
            impulse.x = 0
        
        body.applyImpulse(impulse)