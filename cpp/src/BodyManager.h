#pragma once

#include "WorldManager.h"

class BodyManager
{
public:
	unsigned int addBody(b2World* world, const b2BodyDef& bodyDef);

private:
	vector<b2Body*> bodies;
};