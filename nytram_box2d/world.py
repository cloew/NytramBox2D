from .engine import CppEngine, Vec2
from ctypes import byref

class World:
    """ Represents a World in the Box2D Engine """
    
    def __init__(self, gravity=Vec2(0, 0), velocityIterations=10, positionIterations=10):
        """ Initialize the world """
        self.id = CppEngine.World_Add(byref(gravity))
        self.velocityIterations = velocityIterations
        self.positionIterations = positionIterations
        
    def step(self, msSinceLastFrame):
        """ Step the world """
        CppEngine.World_Step(self.id, msSinceLastFrame/1000, self.velocityIterations, self.positionIterations)