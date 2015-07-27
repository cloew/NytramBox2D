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