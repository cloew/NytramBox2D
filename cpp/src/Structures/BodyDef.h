#pragma once

#include "Box2D/Dynamics/b2Body.h"

struct BodyDef
{
	BodyDef()
	{
		type = b2_staticBody;
		position.SetZero();
		fixedRotation = false;
	}
	b2BodyType type;
	b2Vec2 position;
	bool fixedRotation;
};

b2BodyDef ToBodyDef(const BodyDef& nytBodyDef)
{
	b2BodyDef bodyDef;
	bodyDef.type = nytBodyDef.type;
	bodyDef.position = nytBodyDef.position;
	bodyDef.fixedRotation = true;
	return bodyDef;
}