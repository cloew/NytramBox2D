from .collidable_pair import CollidablePair

from kao_decorators import proxy_for

class CollisionRegistration:
    """ Represents a collider's registration with a collision """
    
    def __init__(self, first, second, *, actsAs):
        """ Initialize the registration with the collidables in collision and the collidable this collider should act as """
        self.pair = CollidablePair(first, second)
        self.actsAs = actsAs
        
    def __eq__(self, other):
        """ Return if this registration is equal to the other """
        return self.pair == other.pair and self.actsAs == other.actsAs
        
    def __hash__(self):
        """ Return the hash code """
        return hash((self.pair, self.actsAs))