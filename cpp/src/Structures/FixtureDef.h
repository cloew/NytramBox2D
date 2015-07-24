#pragma once

#include "Box2D/Dynamics/b2Fixture.h"

struct FixtureDef
{
	FixtureDef()
	{
		//userData = NULL;
		//friction = 0.2f;
		restitution = 0.0f;
		density = 0.0f;
		isSensor = false;
	}
	
	//void* userData;
	//float32 friction;
	float32 restitution;
	float32 density;
	bool isSensor;
	//b2Filter filter;
};

b2FixtureDef ToFixtureDef(const FixtureDef& nytFixtureDef, const b2Shape* shape)
{
	b2FixtureDef fixtureDef;
	fixtureDef.shape = shape;
	fixtureDef.restitution = nytFixtureDef.restitution;
	fixtureDef.density = nytFixtureDef.density;
	fixtureDef.isSensor = nytFixtureDef.isSensor;
	return fixtureDef;
}