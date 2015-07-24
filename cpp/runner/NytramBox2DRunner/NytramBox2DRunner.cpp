// NytramBox2DRunner.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "NytramBox2D.h"

#include <iostream>
using namespace std;

void CollisionStart(unsigned int colliderA, unsigned int colliderB)
{
	cout << colliderA << " hit " << colliderB << endl;
}

void CollisionStop(unsigned int colliderA, unsigned int colliderB)
{
	cout << colliderA << " stopped hitting " << colliderB << endl;
}


int _tmain(int argc, _TCHAR* argv[])
{
	BodyDef bodyDef;
	bodyDef.type = b2BodyType::b2_dynamicBody;
	bodyDef.position.Set(0, 20);
	bodyDef.fixedRotation = true;

	BodyDef bodyDef2;
	bodyDef2.type = b2BodyType::b2_staticBody;
	bodyDef2.position.Set(0, 0);

	BodyDef bodyDef3;
	bodyDef3.type = b2BodyType::b2_staticBody;
	bodyDef3.position.Set(0, 1);

	FixtureDef fixtureDef;
	fixtureDef.userData = (void*) 1;
	fixtureDef.restitution = 1;
	FixtureDef fixtureDef2;
	fixtureDef2.userData = (void*) 2;
	FixtureDef fixtureDef3;
	fixtureDef3.userData = (void*) 3;
	fixtureDef3.isSensor = true;

	unsigned int worldId = World_Add();
	Collision_SetStartCallback(CollisionStart);
	Collision_SetStopCallback(CollisionStop);

	unsigned int bodyId = World_AddBody(worldId, bodyDef);
	unsigned int fixtureId = Body_AddBoxFixture(bodyId, fixtureDef, 2, 2);
	unsigned int bodyId2 = World_AddBody(worldId, bodyDef2);
	unsigned int fixtureId2 = Body_AddEdgeFixture(bodyId2, fixtureDef2, b2Vec2(-10, 0), b2Vec2(10, 0));
	unsigned int bodyId3 = World_AddBody(worldId, bodyDef3);
	unsigned int fixtureId3 = Body_AddBoxFixture(bodyId3, fixtureDef3, 20, 2);
	
	const b2Vec2 v = Body_GetPosition(bodyId3);
	cout << "X: " << v.x << " Y: " << v.y << endl;

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

