#include "FixtureManager.h"

unsigned int FixtureManager::addFixture(b2Body* body)
{
	b2PolygonShape polygonShape;
	polygonShape.SetAsBox(1, 1); //a 2x2 rectangle

	b2Fixture* fixture = body->CreateFixture(&polygonShape, 1);
	fixtures.push_back(fixture);
	return fixtures.size();
}