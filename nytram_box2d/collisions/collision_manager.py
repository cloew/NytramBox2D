from .collidable_pair import CollidablePair
from ..engine import CollisionCallback, Box2DEngine

from kao_sequence import Incrementer
        
class CollisionManager:
    """ Helper class to manage connections between colliders and collisions """
    
    def __init__(self, collisions):
        """ Initialize the Collision Manager with the list of collisions to manage """
        self.collidablePairToCollision = {collision.collidablePair:collision for collision in collisions}
        self.idToCollider = {}
        self.idProvider = Incrementer(startAt=1)
        
    def start(self):
        """ Start the collision Manager by binding the Collision Callbacks """
        self.startCallback = CollisionCallback(self.performCollisionStart)
        Box2DEngine.Collision_SetStartCallback(self.startCallback)
        
        self.stopCallback = CollisionCallback(self.performCollisionStop)
        Box2DEngine.Collision_SetStopCallback(self.stopCallback)
        
    def register(self, collider):
        """ Register the collider """
        id = self.idProvider.send(None)
        collider.id = id
        self.idToCollider[id] = collider
        
    def performCollisionStart(self, id1, id2):
        """ Perform the collision """
        collision, firstCollider, secondCollider = self.findCollision(id1, id2)
        if collision:
            collision.startCollision(firstCollider, secondCollider)
        
    def performCollisionStop(self, id1, id2):
        """ Perform the collision """
        collision, firstCollider, secondCollider = self.findCollision(id1, id2)
        if collision:
            collision.stopCollision(firstCollider, secondCollider)
        
    def findCollision(self, id1, id2):
        """ Return the collision """
        collider1 = self.idToCollider[id1]
        collider2 = self.idToCollider[id2]
        
        possiblePairs = collider1.pairs.intersection(collider2.pairs)
        for pair in possiblePairs:
            actingPair = CollidablePair(collider1.pairToRegistration[pair].actsAs, collider2.pairToRegistration[pair].actsAs)
            if actingPair == pair:
                collision = self.collidablePairToCollision[pair]
                if actingPair.first == pair.first:
                    return collision, collider1, collider2
                else:
                    return collision, collider2, collider1
        else:
            return None, None, None