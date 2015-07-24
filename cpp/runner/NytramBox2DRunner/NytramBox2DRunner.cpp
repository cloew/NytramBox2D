// NytramBox2DRunner.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "NytramBox2D.h"

#include <iostream>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	BodyDef bodyDef;
	bodyDef.type = b2BodyType::b2_dynamicBody;
	bodyDef.fixedRotation = true;

	unsigned int worldId = World_Add();
	unsigned int bodyId = World_AddBody(worldId, bodyDef);
	unsigned int fixtureId = Body_AddBoxFixture(bodyId, 2, 2);

	for (int i = 0; i < 60; i++)
	{
		World_Step(worldId, 1/60.0, 10, 10);
		const b2Vec2 v = Body_GetPosition(bodyId);
		cout << "X: " << v.x << " Y: " << v.y << endl;
	}

	system("PAUSE");
	return 0;
}

