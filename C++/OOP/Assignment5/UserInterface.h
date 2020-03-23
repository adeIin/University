#pragma once
#include "Controller.h"


class RunicAltar {
private:
	Enchantment enchantment;
public:
	//Constructor for user interface
	RunicAltar(const Enchantment ench) : enchantment(ench) {}


	//Run function for main program
	void lightRunicAltar();

	
	//Run function for admin mode
	void communionPatternMage();


	//Run function for user mode
	void communionPatternApprentice();

private:
	//Prints a help menu for admin mode
	void showEnchantmentsMage();

	
	//Prints a help menu for user mode
	void showEnchantmentsApprentice();


	//Prints a help menu for main program
	void showEnchantmentsFirstFire();


	//Adds a new item
	void addGuardianStatue(std::string parametersLine);


	//Deletes an item
	void deleteGuardianStatue(std::string parametersLine);


	//Updates an item
	void updateGuardianStatue(std::string parametersLine);


	//List all items
	void listAllGuardianStatues(std::string parametersLine);
};