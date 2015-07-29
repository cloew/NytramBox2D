from .engine.fixture_def import FixtureDef
from kao_decorators import proxy_for

@proxy_for("fixtureDef", ["userData"])
class Fixture:
    """ Represents a fixture to apply to a body """
    
    def __init__(self, shape, **kwargs):
        """ Initialize the fixture """
        self.id = None
        self.fixtureDef = FixtureDef(**kwargs)
        self.shape = shape
        
    def addToBody(self, body):
        """ Add the fixture to the given body """
        self.id = self.shape.apply(body, self.fixtureDef)