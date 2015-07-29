from ..engine import Vec2

class DirectionalMovement:
    """ Represents a Directional Movement """
    
    def __init__(self, direction, speed):
        """ Initialize the movement with the direction to move in and the speed to move at """
        self.direction = Vec2(direction)
        self.speed = speed
    
    def update(self):
        """ Update the behavior """
        self.speed.apply(self.entity.body, self.direction)