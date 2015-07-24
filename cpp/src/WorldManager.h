#pragma once

#include <Box2D/Box2D.h>
#include "Collisions/CollisionHandler.h"

#include <vector>

using namespace std;

class WorldManager
{
public:
	unsigned int addWorld(b2Vec2 gravity);
	b2World* getWorld(unsigned int id) {return worlds[id-1];}

	// Collisions
	void setCollisionStartCallback(Collision_Callback startCallback) {collisionHandler.setStartCallback(startCallback);}
	void setCollisionStopCallback(Collision_Callback stopCallback) {collisionHandler.setStopCallback(stopCallback);}

private:
	vector<b2World*> worlds;
	CollisionHandler collisionHandler;
};

