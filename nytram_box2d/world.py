from .engine import CppEngine
from ctypes import c_float

class World:
    """ Represents a World in the Box2D Engine """
    
    def __init__(self):
        """ Initialize the world """
        self.id = CppEngine.World_Add()
        
    def step(self, timeStep, velocityIterations=10, positionIterations=10):
        """ Step the world """
        print(timeStep, velocityIterations, positionIterations)
        CppEngine.World_Step(self.id, c_float(timeStep), velocityIterations, positionIterations)