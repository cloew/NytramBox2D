from .vec2 import Vec2
from .body_types import BodyTypes

from ctypes import cdll, c_bool, c_float, CFUNCTYPE, POINTER
from nytram.engine import EngineCallback

CppEngine = cdll.LoadLibrary("NytramBox2D.dll")

CppEngine.Body_GetPosition.restype = POINTER(Vec2)