#pragma once

#include "../../BodyManager.h"
#include "Box2D/Dynamics/Joints/b2WeldJoint.h"

struct WeldJointDef
{
	unsigned int bodyAId;
	unsigned int bodyBId;
	b2Vec2 anchor;
};

b2WeldJointDef ToWeldJointDef(const WeldJointDef& nytJointDef, const BodyManager& bodyManager)
{
	b2WeldJointDef jointDef;
	b2Body* bodyA = bodyManager.getBody(nytJointDef.bodyAId);
	b2Body* bodyB = bodyManager.getBody(nytJointDef.bodyBId);
	jointDef.Initialize(bodyA, bodyB, nytJointDef.anchor);
	return jointDef;
}