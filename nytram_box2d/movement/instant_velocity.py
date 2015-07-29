
class InstantVelocity:
    """ Represents a method of providing an instant velocity """
    
    def __init__(self, speed):
        """ Initialize with the body speed and direction """
        self.speed = speed
        
    def apply(self, body, direction):
        """ Apply the speed in the given direction to the given body """
        velocity = body.velocity
        impulse = (direction*self.speed - velocity)*body.mass
        body.applyImpulse(impulse)