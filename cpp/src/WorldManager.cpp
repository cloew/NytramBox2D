#include "WorldManager.h"

unsigned int WorldManager::addWorld(b2Vec2 gravity)
{
	b2World* world = new b2World(gravity);
	world->SetContactListener(&collisionHandler);
	worlds.push_back(world);
	return worlds.size();
}