#pragma once

#include <Box2D/Box2D.h>

#include <vector>

using namespace std;

class WorldManager
{
public:
	unsigned int addWorld(b2Vec2 gravity);
	b2World* getWorld(unsigned int id) {return worlds[id-1];}

private:
	vector<b2World*> worlds;
};

