from .engine.fixture_def import FixtureDef

class Fixture:
    """ Represents a fixture to apply to a body """
    
    def __init__(self, body, shape, **kwargs):
        """ Initialize the fixture """
        self.id = shape.apply(body, FixtureDef(**kwargs))