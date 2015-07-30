#pragma once

#include "Box2D/Dynamics/b2World.h"
#include "Box2D/Dynamics/Joints/b2Joint.h"
#include <vector>
using namespace std;

class JointManager
{
public:
	unsigned int addJoint(b2World* world, const b2JointDef* jointDef);
	b2Joint* getJoint(unsigned int id) {return joints[id-1];}

private:
	vector<b2Joint*> joints;
};