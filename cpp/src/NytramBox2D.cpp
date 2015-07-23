#include "NytramBox2D.h"

WorldManager worldManager;
BodyManager bodyManager;
FixtureManager fixtureManager;

unsigned int World_Add()
{
	b2Vec2 gravity(0,-10);
	return worldManager.addWorld(gravity);
}

void World_Step(unsigned int worldId)
{
	b2World* world = worldManager.getWorld(worldId);
	world->Step(1, 10, 10);
}

unsigned int Body_Add(unsigned int worldId, const BodyDef& bodyDef)
{
	return bodyManager.addBody(worldManager.getWorld(worldId), ToBodyDef(bodyDef));
}

const b2Vec2& Body_GetPosition(unsigned int bodyId)
{
	return bodyManager.getPosition(bodyId);
}

unsigned int Fixture_Add(unsigned int bodyId)
{
	return fixtureManager.addFixture(bodyManager.getBody(bodyId));
}