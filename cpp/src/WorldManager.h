#pragma once

#include <Box2D/Box2D.h>

#include <vector>

using namespace std;

class WorldManager
{
public:
	WorldManager(void);
	~WorldManager(void);

	unsigned int addWorld(b2Vec2 gravity);

private:
	vector<b2World*> worlds;
};

