#include "Domain.h"


GuardianStatue::GuardianStatue() : powerWordName(""), material(""), age(0), corporealForm("") {}


GuardianStatue::GuardianStatue(const std::string& powerWordName, const std::string& material, const int& age, const std::string& corporealForm) {
	this->powerWordName = powerWordName;
	this->material = material;
	this->age = age;
	this->corporealForm = corporealForm;
}


