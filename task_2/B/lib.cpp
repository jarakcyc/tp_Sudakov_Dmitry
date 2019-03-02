#include "lib.h"

Car::Car(): mark("") {}

Car::Car(std::string mark_): mark(mark_) {}

std::string Car::get_mark() {
	return mark;
}
