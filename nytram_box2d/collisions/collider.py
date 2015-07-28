
class Collider:
    """ Represents a collider property of a Fixture """
    
    def __init__(self, registrations):
        """ Initialize the collider with the collisions it participates in """
        self.pairToRegistration = {reg.pair:reg for reg in registrations}
        self.id = None
        
    @property
    def pairs(self):
        """ Return the collidable pairs this collider interacts with """
        return set(self.pairToRegistration.keys())