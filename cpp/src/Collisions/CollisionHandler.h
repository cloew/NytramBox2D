#pragma once

#include "Box2D/Dynamics/Contacts/b2Contact.h"
#include "Box2D/Dynamics/b2WorldCallbacks.h"

#include <iostream>
#include <functional>
using namespace std;


typedef std::function<void(unsigned int, unsigned int)> Collision_Callback;

class CollisionHandler : public b2ContactListener
{
public:
	void BeginContact(b2Contact* contact);
    void EndContact(b2Contact* contact);

	// Setters
	void setStartCallback(Collision_Callback startCallback) {this->collisionStartCallback = startCallback;}
	void setStopCallback(Collision_Callback stopCallback) {this->collisionStopCallback = stopCallback;}

private:
	Collision_Callback collisionStartCallback;
	Collision_Callback collisionStopCallback;

	void callCallback(const Collision_Callback& callback, const b2Contact* contact);
};

