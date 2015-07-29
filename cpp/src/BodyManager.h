#pragma once

#include "WorldManager.h"

class BodyManager
{
public:
	unsigned int addBody(b2World* world, const b2BodyDef& bodyDef);
	b2Body* getBody(unsigned int id) {return bodies[id-1];}

	// Forces
	void applyImpulse(unsigned int id, const b2Vec2& impulse) {b2Body* body = getBody(id); body->ApplyLinearImpulse(impulse, body->GetWorldCenter(), true);}

	// Getters
	float32 getBodyMass(unsigned int id) {return getBody(id)->GetMass();}
	const b2Vec2& getPosition(unsigned int id) {return getBody(id)->GetPosition();}

	// Setters
	void setPosition(unsigned int id, const b2Vec2& position) {b2Body* body = getBody(id); body->SetTransform(position, body->GetAngle());}

private:
	vector<b2Body*> bodies;
};