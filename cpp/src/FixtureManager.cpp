#include "FixtureManager.h"

unsigned int FixtureManager::addFixture(b2Body* body, b2Shape* shape)
{
	b2Fixture* fixture = body->CreateFixture(shape, 1);
	fixtures.push_back(fixture);
	return fixtures.size();
}