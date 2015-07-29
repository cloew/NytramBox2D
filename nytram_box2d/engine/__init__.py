from .vec2 import Vec2
from .body_types import BodyTypes
from .fixture_def import FixtureDef

from ctypes import cdll, c_int, c_uint, c_float, POINTER, CFUNCTYPE
from nytram.engine import EngineCallback

Box2DEngine = cdll.LoadLibrary("NytramBox2D.dll")

CollisionCallback = EngineCallback(CFUNCTYPE(None, c_uint, c_uint))

Box2DEngine.Body_GetPosition.restype = POINTER(Vec2)
Box2DEngine.Body_GetVelocity.restype = POINTER(Vec2)
Box2DEngine.Body_AddBoxFixture.argtypes = [c_uint, FixtureDef, c_float, c_float]
Box2DEngine.World_Step.argtypes = [c_uint, c_float, c_int, c_int]