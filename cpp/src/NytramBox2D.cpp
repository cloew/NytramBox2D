#include "NytramBox2D.h"

WorldManager worldManager;
BodyManager bodyManager;
FixtureManager fixtureManager;
JointManager jointManager;

// World
unsigned int World_Add(const b2Vec2& gravity)
{
	return worldManager.addWorld(gravity);
}

void World_Step(unsigned int worldId, float32 step, int32 velocityIterations, int32 positionIterations)
{
	b2World* world = worldManager.getWorld(worldId);
	world->Step(step, velocityIterations, positionIterations);
}

unsigned int World_AddBody(unsigned int worldId, const BodyDef& bodyDef)
{
	return bodyManager.addBody(worldManager.getWorld(worldId), ToBodyDef(bodyDef));
}

// Body
void Body_ApplyImpulse(unsigned int bodyId, const b2Vec2& impulse)
{
	bodyManager.applyImpulse(bodyId, impulse);
}

float32 Body_GetMass(unsigned int bodyId)
{
	return bodyManager.getBodyMass(bodyId);
}

const b2Vec2& Body_GetPosition(unsigned int bodyId)
{
	return bodyManager.getPosition(bodyId);
}

const b2Vec2& Body_GetVelocity(unsigned int bodyId)
{
	return bodyManager.getVelocity(bodyId);
}

void Body_SetPosition(unsigned int bodyId, const b2Vec2& position)
{
	bodyManager.setPosition(bodyId, position);
}

unsigned int Body_AddBoxFixture(unsigned int bodyId, const FixtureDef& fixtureDef, float width, float height)
{
	b2PolygonShape box;
	box.SetAsBox(width/2, height/2);
	return fixtureManager.addFixture(bodyManager.getBody(bodyId), &ToFixtureDef(fixtureDef, &box));
}

unsigned int Body_AddEdgeFixture(unsigned int bodyId, const FixtureDef& fixtureDef, const b2Vec2& v1, const b2Vec2& v2)
{
	b2EdgeShape edge;
	edge.Set(v1, v2);

	return fixtureManager.addFixture(bodyManager.getBody(bodyId), &ToFixtureDef(fixtureDef, &edge));
}

// Collisions
void Collision_SetStartCallback(Collision_Callback_fp callback)
{
	worldManager.setCollisionStartCallback(callback);
}

void Collision_SetStopCallback(Collision_Callback_fp callback)
{
	worldManager.setCollisionStopCallback(callback);
}

// Joints
unsigned int Joint_AddWeldJoint(unsigned int worldId, const WeldJointDef& jointDef)
{
	b2WeldJointDef weldJointDef = ToWeldJointDef(jointDef, bodyManager);
	return jointManager.addJoint(worldManager.getWorld(worldId), &weldJointDef);
}