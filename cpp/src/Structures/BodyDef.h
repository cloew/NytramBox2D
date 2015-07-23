#pragma once

#include "Box2D/Dynamics/b2Body.h"

struct BodyDef
{
	b2BodyType type;
	bool fixedRotation;
};

b2BodyDef ToBodyDef(const BodyDef& nytBodyDef)
{
	b2BodyDef bodyDef;
	bodyDef.type = nytBodyDef.type;
	bodyDef.fixedRotation = true;
	return bodyDef;
}