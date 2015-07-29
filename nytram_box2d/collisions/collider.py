from nytram.engine import EngineAttr

class Collider:
    """ Represents a collider property of a Fixture """
    entity = EngineAttr("register")
    
    def __init__(self, fixtures, registrations):
        """ Initialize the collider with the collisions it participates in """
        self.id = None
        self.fixtures = fixtures
        self.pairToRegistration = {reg.pair:reg for reg in registrations}
        
    @property
    def pairs(self):
        """ Return the collidable pairs this collider interacts with """
        return set(self.pairToRegistration.keys())
        
    def register(self):
        """ Register the collider with the collision manager """
        self.collisionManager.register(self)
        for fixture in self.fixtures:
            fixture.userData = self.id
        
    @property
    def collisionManager(self):
        """ Return the current collision manager """
        return self.entity.scene.collisionManager