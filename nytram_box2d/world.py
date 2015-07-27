from .engine import CppEngine, Vec2
from ctypes import c_float, byref

class World:
    """ Represents a World in the Box2D Engine """
    
    def __init__(self, gravity=Vec2(0, 0)):
        """ Initialize the world """
        self.id = CppEngine.World_Add(byref(gravity))
        
    def step(self, timeStep, velocityIterations=10, positionIterations=10):
        """ Step the world """
        CppEngine.World_Step(self.id, c_float(timeStep), velocityIterations, positionIterations)