#include "CollisionHandler.h"

void CollisionHandler::BeginContact(b2Contact* contact)
{
	callCallback(collisionStartCallback, contact);
}

void CollisionHandler::EndContact(b2Contact* contact)
{
	callCallback(collisionStopCallback, contact);
}

void CollisionHandler::callCallback(const Collision_Callback& callback, const b2Contact* contact)
{
	if (callback)
	{
		unsigned int colliderAId = (unsigned int) contact->GetFixtureA()->GetUserData();
		unsigned int colliderBId = (unsigned int) contact->GetFixtureB()->GetUserData();
		if (colliderAId != 0 && colliderBId != 0)
		{
			callback(colliderAId, colliderBId);
		}
	}
}