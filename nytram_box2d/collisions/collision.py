from .collidable_pair import CollidablePair

class Collision:
    """ Represents a possible collision between bodies """
    @classmethod
    def createCollision(cls, first, second, fnKwarg):
        def createCollision(fn):
            kwargs = {fnKwarg: fn}
            return cls(CollidablePair(first, second), **kwargs)
        return createCollision
    
    
    @classmethod
    def start(cls, first, second):
        """ Decorator to create a collision between the given collidables """
        return cls.createCollision(first, second, "start")
    
    @classmethod
    def stop(cls, first, second):
        """ Decorator to create a collision between the given collidables """
        return cls.createCollision(first, second, "stop")
    
    def __init__(self, collidablePair, start=None, stop=None):
        """ Initialize with the collidable pair to cause this collision """
        self.collidablePair = collidablePair
        self.start = start
        self.stop = stop
        
    def startCollision(self, collider1, collider2):
        """ Start the collision """
        if self.start:
            self.start(collider1, collider2)
        
    def stopCollision(self, collider1, collider2):
        """ Stop the collision """
        if self.stop:
            self.stop(collider1, collider2)