#include "JointManager.h"

unsigned int JointManager::addJoint(b2World* world, const b2JointDef* jointDef)
{
	b2Joint* joint = world->CreateJoint(jointDef);
	joints.push_back(joint);
	return joints.size();
}