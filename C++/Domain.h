#pragma once
#include <iostream>
#include <string>


class GuardianStatue {
private:
	std::string powerWordName;
	std::string material;
	int age;
	std::string corporealForm;

public:
	//Default constructor
	GuardianStatue();


	//Constructor function for GuardianStatue
	GuardianStatue(const std::string& powerWordName, const std::string& material, const int& age, const std::string& corporealForm);


	//Getter for powerWordName
	std::string getPowerWordName() const { return powerWordName; }

	
	//Getter for material
	std::string getMaterial() const { return material; }


	//Getter for age
	int getAge() const { return age; }


	//Getter for corporealForm
	std::string getCorporealForm() const { return corporealForm; }

};
