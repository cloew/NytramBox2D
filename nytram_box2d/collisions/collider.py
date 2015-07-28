from nytram.engine import EngineAttr

class Collider:
    """ Represents a collider property of a Fixture """
    entity = EngineAttr("register")
    
    def __init__(self, registrations):
        """ Initialize the collider with the collisions it participates in """
        self.pairToRegistration = {reg.pair:reg for reg in registrations}
        self.id = None
        
    @property
    def pairs(self):
        """ Return the collidable pairs this collider interacts with """
        return set(self.pairToRegistration.keys())
        
    def register(self):
        """ Register the collider with the collision manager """
        self.collisionManager.register(self)
        
    @property
    def collisionManager(self):
        """ Return the current collision manager """
        return self.entity.scene.collisionManager