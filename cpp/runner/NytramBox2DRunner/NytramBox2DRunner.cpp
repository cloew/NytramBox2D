// NytramBox2DRunner.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "NytramBox2D.h"

#include <iostream>
using namespace std;

struct MyVec
{
	float32 x, y;
};


int _tmain(int argc, _TCHAR* argv[])
{
	MyVec v;
	v.x = 0;
	v.y = 2;

	b2Vec2* v2 = (b2Vec2*) &v;
	cout << "X: " << v2->x << " Y: " << v2->y << endl;
	cout << "Mag: " << v2->Length() << endl;
	system("PAUSE");
	return 0;
}

