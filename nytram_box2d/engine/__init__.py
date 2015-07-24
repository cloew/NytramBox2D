from .b2vec2 import B2Vec2

from ctypes import cdll, c_bool, c_int, CFUNCTYPE
from nytram.engine import EngineCallback

CppEngine = cdll.LoadLibrary("NytramBox2D.dll")

CppEngine.Body_GetPosition.restype = B2Vec2