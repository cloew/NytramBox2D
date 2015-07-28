from .collidable_pair import CollidablePair
from kao_sequence import Incrementer
        
class CollisionManager:
    """ Helper class to manage connections between colliders and collisions """
    
    def __init__(self, collisions):
        """ Initialize the Collision Manager with the list of collisions to manage """
        self.collidablePairToCollision = {collision.collidablePair:collision for collision in collisions}
        self.idToCollider = {}
        self.idProvider = Incrementer(startAt=1)
        
    def register(self, collider):
        """ Register the collider """
        id = self.idProvider.send(None)
        collider.id = id
        self.idToCollider[id] = collider
        
    def performCollisionStart(self, id1, id2):
        """ Perform the collision """
        collider1 = self.idToCollider[id1]
        collider2 = self.idToCollider[id2]
        
        collision = self.findCollision(collider1, collider2)
        collision.startCollision(collider1, collider2)
        
    def performCollisionStop(self, id1, id2):
        """ Perform the collision """
        collider1 = self.idToCollider[id1]
        collider2 = self.idToCollider[id2]
        
        collision = self.findCollision(collider1, collider2)
        collision.stopCollision(collider1, collider2)
        
    def findCollision(self, collider1, collider2):
        """ Return the collision """
        possiblePairs = collider1.pairs.intersection(collider2.pairs)
        for pair in possiblePairs:
            actingPair = CollidablePair(collider1.pairToRegistration[pair].actsAs, collider2.pairToRegistration[pair].actsAs)
            if actingPair == pair:
                return self.collidablePairToCollision[pair]
        else:
            return None