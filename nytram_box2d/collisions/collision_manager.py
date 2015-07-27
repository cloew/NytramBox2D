
class CollisionManager:
    """ Helper class to manage connections between colliders and collisions """
    
    def __init__(self, collisions):
        """ Initialize the Collision Manager with the list of collisions to manage """
        self.collidablePairToCollision = {collision.collidablePair:collision for collision in collisions}
        self.idToCollider = {}