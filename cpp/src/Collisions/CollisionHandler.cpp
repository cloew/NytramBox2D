#include "CollisionHandler.h"

void CollisionHandler::BeginContact(b2Contact* contact)
{
	cout << "In Begin Contact" << endl;
	cout << "A data: " << contact->GetFixtureA()->GetUserData() << endl;
	cout << "B data: " << contact->GetFixtureB()->GetUserData() << endl;
}

void CollisionHandler::EndContact(b2Contact* contact)
{
	cout << "In End Contact" << endl;
	cout << "A data: " << contact->GetFixtureA()->GetUserData() << endl;
	cout << "B data: " << contact->GetFixtureB()->GetUserData() << endl;
}
