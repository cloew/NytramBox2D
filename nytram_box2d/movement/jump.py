from ..engine import Vec2

class Jump:
    """ Represents an ability of an entity to jump """
    
    def __init__(self, body, speed):
        """ Initialize with the speed to jump at """
        self.body = body
        self.speed = Vec2(0, speed)
        
    def jump(self, event=None):
        """ Jump the entity """
        impulse = self.speed*self.body.mass
        self.body.applyImpulse(impulse)