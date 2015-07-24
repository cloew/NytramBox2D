#pragma once

#include "WorldManager.h"
#include "BodyManager.h"
#include "FixtureManager.h"
#include "Structures/BodyDef.h"

#define NYTRAM_API __declspec(dllexport)

#if __cplusplus
extern "C" {
#endif

	NYTRAM_API unsigned int World_Add();
	NYTRAM_API void World_Step(unsigned int worldId, float32 step, int32 velocityIterations, int32 positionIterations);
	NYTRAM_API unsigned int World_AddBody(unsigned int worldId, const BodyDef& bodyDef);
	NYTRAM_API const b2Vec2& Body_GetPosition(unsigned int bodyId);
	NYTRAM_API unsigned int Body_AddBoxFixture(unsigned int bodyId, float width, float height);
	
#if __cplusplus
}
#endif