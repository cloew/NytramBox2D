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
	bodyDef.position.Set(0, 20);
	bodyDef.fixedRotation = true;

	BodyDef bodyDef2;
	bodyDef2.type = b2BodyType::b2_staticBody;
	bodyDef2.position.Set(0, 0);

	FixtureDef fixtureDef;
	fixtureDef.restitution = 1;
	FixtureDef fixtureDef2;

	unsigned int worldId = World_Add();
	unsigned int bodyId = World_AddBody(worldId, bodyDef);
	unsigned int fixtureId = Body_AddBoxFixture(bodyId, fixtureDef, 2, 2);
	unsigned int bodyId2 = World_AddBody(worldId, bodyDef2);
	unsigned int fixtureId2 = Body_AddEdgeFixture(bodyId2, fixtureDef2, b2Vec2(-10, 0), b2Vec2(10, 0));

	for (int i = 0; i < 2*60; i++)
	{
		World_Step(worldId, 1/60.0, 10, 10);
		const b2Vec2 v = Body_GetPosition(bodyId);
		cout << "X: " << v.x << " Y: " << v.y << endl;
	}
	system("PAUSE");
	for (int i = 0; i < 4*60; i++)
	{
		World_Step(worldId, 1/60.0, 10, 10);
		const b2Vec2 v = Body_GetPosition(bodyId);
		cout << "X: " << v.x << " Y: " << v.y << endl;
	}

	system("PAUSE");
	return 0;
}

