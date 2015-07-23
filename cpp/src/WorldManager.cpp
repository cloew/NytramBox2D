#include "WorldManager.h"

unsigned int WorldManager::addWorld(b2Vec2 gravity)
{
	b2World* word = new b2World(gravity);
	worlds.push_back(word);
	return worlds.size();
}