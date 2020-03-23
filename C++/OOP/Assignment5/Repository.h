#pragma once
#include "Domain.h"
#include "DynamicArray.h"
#include <exception>


class Encyclopedia {
private:
	DynamicVector<GuardianStatue> statues;
public:
	//Constructor function
	Encyclopedia() {}


	//Getter for size
	int getSize() const;


	//Function that adds a statue in the encyclopedia
	void addStatue(const GuardianStatue& guardStat);


	//Function that deletes a statue from the encyclopedia
	void deleteStatue(const std::string& powerWordName);


	//Function that updates a statue in the encyclopedia
	void updateStatue(const GuardianStatue& guardStat);


	//Getter for all the statues in the ecyclopedia
	DynamicVector<GuardianStatue> getAllStatues();
};
