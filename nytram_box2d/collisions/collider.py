
class Collider:
    """ Represents a collider property of a Fixture """
    
    def __init__(self, registrations):
        """ Initialize the collider with the collisions it participates in """
        self.registrations = set(registrations)
        self.id = None