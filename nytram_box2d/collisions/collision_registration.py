from .collidable_pair import CollidablePair

from kao_decorators import proxy_for

@proxy_for("pair", ["__hash__"])
class CollisionRegistration:
    """ Represents a collider's registration with a collision """
    
    def __init__(self, first, second, *, actsAs):
        """ Initialize the registration with the collidables in collision and the collidable this collider should act as """
        self.pair = CollidablePair(first, second)
        self.actsAs = actsAs