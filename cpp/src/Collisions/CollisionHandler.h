#pragma once

#include "Box2D/Dynamics/Contacts/b2Contact.h"
#include "Box2D/Dynamics/b2WorldCallbacks.h"

#include <iostream>
using namespace std;

class CollisionHandler : public b2ContactListener
{
public:
	void BeginContact(b2Contact* contact);
    void EndContact(b2Contact* contact);
};

