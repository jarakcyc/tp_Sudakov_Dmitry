#pragma once
#include <string>

using namespace std;

class Car {
private:
	string mark;
public:
	Car();
	Car(string model_);
	string get_mark();
};