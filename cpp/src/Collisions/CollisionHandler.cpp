#include "CollisionHandler.h"

void CollisionHandler::BeginContact(b2Contact* contact)
{
	cout << "In Begin Contact" << endl;
}

void CollisionHandler::EndContact(b2Contact* contact)
{
	cout << "In End Contact" << endl;
}
