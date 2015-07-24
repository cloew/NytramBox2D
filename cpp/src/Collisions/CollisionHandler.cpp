#include "CollisionHandler.h"

void CollisionHandler::BeginContact(b2Contact* contact)
{
	cout << "In Begin Contact" << endl;
	cout << "A is Sensor: " << contact->GetFixtureA()->IsSensor() << endl;
	cout << "B is Sensor: " << contact->GetFixtureB()->IsSensor() << endl;
}

void CollisionHandler::EndContact(b2Contact* contact)
{
	cout << "In End Contact" << endl;
	cout << "A is Sensor: " << contact->GetFixtureA()->IsSensor() << endl;
	cout << "B is Sensor: " << contact->GetFixtureB()->IsSensor() << endl;
}
