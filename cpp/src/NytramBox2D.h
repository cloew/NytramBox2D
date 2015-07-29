#pragma once

#include "WorldManager.h"
#include "BodyManager.h"
#include "FixtureManager.h"

#include "Structures/BodyDef.h"
#include "Structures/FixtureDef.h"

#define NYTRAM_API __declspec(dllexport)

#if __cplusplus
extern "C" {
#endif

	typedef void (*Collision_Callback_fp)(unsigned int, unsigned int);

	// World
	NYTRAM_API unsigned int World_Add(const b2Vec2& gravity);
	NYTRAM_API void World_Step(unsigned int worldId, float32 step, int32 velocityIterations, int32 positionIterations);
	NYTRAM_API unsigned int World_AddBody(unsigned int worldId, const BodyDef& bodyDef);

	// Body
	NYTRAM_API float32 Body_GetMass(unsigned int bodyId);
	NYTRAM_API const b2Vec2& Body_GetPosition(unsigned int bodyId);
	NYTRAM_API void Body_SetPosition(unsigned int bodyId, const b2Vec2& position);
	NYTRAM_API unsigned int Body_AddBoxFixture(unsigned int bodyId, const FixtureDef& fixtureDef, float width, float height);
	NYTRAM_API unsigned int Body_AddEdgeFixture(unsigned int bodyId, const FixtureDef& fixtureDef, const b2Vec2& v1, const b2Vec2& v2);

	// Collision
	NYTRAM_API void Collision_SetStartCallback(Collision_Callback_fp callback);
	NYTRAM_API void Collision_SetStopCallback(Collision_Callback_fp callback);
	
#if __cplusplus
}
#endif