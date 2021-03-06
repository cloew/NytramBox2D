#pragma once

#include "Box2D/Collision/Shapes/b2PolygonShape.h"
#include "Box2D/Dynamics/b2Fixture.h"

#include <iostream>
#include <vector>
using namespace std;

class FixtureManager
{
public:
	unsigned int addFixture(b2Body* body, const b2FixtureDef* fixtureDef);
	
private:
	vector<b2Fixture*> fixtures;
};