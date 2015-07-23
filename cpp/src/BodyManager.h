#pragma once

#include "WorldManager.h"

class BodyManager
{
public:
	unsigned int addBody(b2World* world, const b2BodyDef& bodyDef);
	b2Body* getBody(unsigned int id) {return bodies[id-1];}
	const b2Vec2& getPosition(unsigned int id) {return getBody(id)->GetPosition();}

private:
	vector<b2Body*> bodies;
};