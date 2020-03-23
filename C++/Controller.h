#pragma once
#include "Repository.h"


class Enchantment {
private:
	Encyclopedia encyclopedia;
public:
	//Constructor function for enchantment
	Enchantment(Encyclopedia& enclp) : encyclopedia{ enclp } {}


	//Function that creates a guardian statue and adds it in the encyclopedia
	void addGuardianStatue(const std::string& powerWordName, const std::string& material, const int& age, const std::string corporealForm);


	//Function that deletes a guardian statue from the encyclopedia
	void deleteGuardianStatue(const std::string& powerWordName);


	//Function that updates a guardian statue
	void updateGuardianStatue(const std::string& powerWordName, const std::string& newMaterial, const int& newAge, const std::string newCorporealForm);


	//Getter for size in the encyclopedia
	int getSize() const;


	//Getter for all the statues
	DynamicVector<GuardianStatue> getAllGuardianStatues();
};
