#include "NytramBox2D.h"

WorldManager worldManager;
BodyManager bodyManager;

unsigned int World_Add()
{
	b2Vec2 gravity(0,0);
	return worldManager.addWorld(gravity);
}

unsigned int Body_Add(unsigned int worldId, const BodyDef& bodyDef)
{
	return bodyManager.addBody(worldManager.getWorld(worldId), ToBodyDef(bodyDef));
}