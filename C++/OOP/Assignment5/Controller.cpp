#include "Controller.h"


void Enchantment::addGuardianStatue(const std::string& powerWordName, const std::string& material, const int& age, const std::string corporealForm) {
	GuardianStatue guardStat = { powerWordName, material, age, corporealForm };
	try {
		encyclopedia.addStatue(guardStat);
	}
	catch (std::exception&) {
		throw std::exception();
	}
}


void Enchantment::deleteGuardianStatue(const std::string& powerWordName) {
	try {
		encyclopedia.deleteStatue(powerWordName);
	}
	catch (std::exception&) {
		throw std::exception();
	}
}


void Enchantment::updateGuardianStatue(const std::string& powerWordName, const std::string& newMaterial, const int& newAge, const std::string newCorporealForm) {
	GuardianStatue guardStat = { powerWordName, newMaterial, newAge, newCorporealForm };
	try {
		encyclopedia.updateStatue(guardStat);
	}
	catch (std::exception&) {
		throw std::exception();
	}
}


int Enchantment::getSize() const {
	return encyclopedia.getSize();
}


DynamicVector<GuardianStatue> Enchantment::getAllGuardianStatues() {
	return encyclopedia.getAllStatues();
}
