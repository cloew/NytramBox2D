#include "NytramBox2D.h"

WorldManager worldManager;
BodyManager bodyManager;
FixtureManager fixtureManager;

unsigned int World_Add()
{
	b2Vec2 gravity(0,-10);
	return worldManager.addWorld(gravity);
}

void World_Step(unsigned int worldId, float32 step, int32 velocityIterations, int32 positionIterations)
{
	b2World* world = worldManager.getWorld(worldId);
	world->Step(step, velocityIterations, positionIterations);
}

unsigned int World_AddBody(unsigned int worldId, const BodyDef& bodyDef)
{
	return bodyManager.addBody(worldManager.getWorld(worldId), ToBodyDef(bodyDef));
}

const b2Vec2& Body_GetPosition(unsigned int bodyId)
{
	return bodyManager.getPosition(bodyId);
}

unsigned int Body_AddBoxFixture(unsigned int bodyId, float width, float height)
{
	b2PolygonShape box;
	box.SetAsBox(width/2, height/2);

	return fixtureManager.addFixture(bodyManager.getBody(bodyId), &box);
}