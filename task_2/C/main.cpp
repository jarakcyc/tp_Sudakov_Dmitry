#include "main.h"
#include <iostream>

using namespace std;

int main() {
	vector<Car> cars(3, Car());
	cars[0] = Car("lamborginy");
	cars[1] = Car("ferrari");
	cars[2] = Car("porshe");
	for (int i = 0; i < 3; ++i) {
		cout << cars[i].get_mark() << endl;
	}
}