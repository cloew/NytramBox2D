#include "NytramBox2D.h"

WorldManager worldManager;

unsigned int Add_World()
{
	b2Vec2 gravity(0,0);
	return worldManager.addWorld(gravity);
}