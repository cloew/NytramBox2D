from .vec2 import Vec2
from .body_types import BodyTypes
from .fixture_def import FixtureDef

from ctypes import cdll, c_int, c_uint, c_float, POINTER
from nytram.engine import EngineCallback

CppEngine = cdll.LoadLibrary("NytramBox2D.dll")

CppEngine.Body_GetPosition.restype = POINTER(Vec2)
CppEngine.Body_AddBoxFixture.argtypes = [c_uint, FixtureDef, c_float, c_float]
CppEngine.World_Step.argtypes = [c_uint, c_float, c_int, c_int]