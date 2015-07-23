#include "BodyManager.h"

unsigned int BodyManager::addBody(b2World* world, const b2BodyDef& bodyDef)
{
	b2Body* body = world->CreateBody(&bodyDef);
	bodies.push_back(body);
	return bodies.size();
}