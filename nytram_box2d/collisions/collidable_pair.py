
class CollidablePair:
    """ Represents a pair of Collidable Bodies """
    
    def __init__(self, first, second):
        """ Initialize the pair """
        self.first = first
        self.second = second
    
    def __eq__(self, other):
        """ Return if the collidables are equal """
        otherItems = (other.first, other.second)
        return (self.first, self.second) == otherItems or (self.second, self.first) == otherItems
        
    def __hash__(self):
        """ Return the hash of this pair """
        return hash(self.first) + hash(self.second)