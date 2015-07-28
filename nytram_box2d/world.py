from .engine import Box2DEngine, Vec2

from nytram.engine import CppEngine as NytramEngine, LoopCallback
from ctypes import byref

class World:
    """ Represents a World in the Box2D Engine """
    
    def __init__(self, gravity=Vec2(0, 0), velocityIterations=10, positionIterations=10):
        """ Initialize the world """
        self.id = None
        self.gravity = gravity
        self.velocityIterations = velocityIterations
        self.positionIterations = positionIterations
        
        self.loopCallback = LoopCallback(self.step)
        
    def step(self, msSinceLastFrame):
        """ Step the world """
        Box2DEngine.World_Step(self.id, msSinceLastFrame/1000, self.velocityIterations, self.positionIterations)
        
    def start(self):
        """ Start the world """
        self.id = Box2DEngine.World_Add(byref(self.gravity))
        NytramEngine.Loop_AddCallback(self.loopCallback)