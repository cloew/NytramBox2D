#include "FixtureManager.h"

unsigned int FixtureManager::addFixture(b2Body* body, const b2FixtureDef* fixtureDef)
{
	b2Fixture* fixture = body->CreateFixture(fixtureDef);
	fixtures.push_back(fixture);
	return fixtures.size();
}