#pragma once

#include "WorldManager.h"
#include "BodyManager.h"
#include "Structures/BodyDef.h"

#define NYTRAM_API __declspec(dllexport)

#if __cplusplus
extern "C" {
#endif

	NYTRAM_API unsigned int World_Add();
	NYTRAM_API unsigned int Body_Add(unsigned int worldId, const BodyDef& bodyDef);
	
#if __cplusplus
}
#endif