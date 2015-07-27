from .engine import CppEngine
from .engine.fixture_def import FixtureDef

from ctypes import Structure, c_void_p, c_bool, c_float

class Fixture:
    """ Represents a fixture to apply to a body """
    
    def __init__(self, body, **kwargs):
        """ Initialize the fixture """
        self.id = CppEngine.Body_AddBoxFixture(body.id, FixtureDef(**kwargs), c_float(2), c_float(2))