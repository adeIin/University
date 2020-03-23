#include "Tests.h"
#include "Controller.h"

#include <assert.h>


void Tests::testAll() {
	testDomain();
	testDynamicArray();
	testRepository();
	testController();
	std::cout << "\nAll tests done!\n\n";
}


void Tests::testDomain() {
	std::cout << "Testing domain\n";
	GuardianStatue guardStat{ "piertotum locomotor", "stone", 328, "warrior with poleax" };
	assert(guardStat.getPowerWordName() == "piertotum locomotor");
	assert(guardStat.getMaterial() == "stone");
	assert(guardStat.getAge() == 328);
	assert(guardStat.getCorporealForm() == "warrior with poleax");
	GuardianStatue guardStat2{ "piertotum locomotor", "stone", 328, "warrior with poleax" };
}


void Tests::testDynamicArray() {
	std::cout << "Testing dynamic array\n";
	/*auto vect1 = DynamicVector<int>();
	vect1.addItem(3);
	vect1.addItem(67);
	vect1.addItem(8);
	assert(vect1.getSize() == 3);*/
}


void Tests::testRepository() {
	std::cout << "Testing repository\n";
	Encyclopedia encl = Encyclopedia();
	GuardianStatue g1 = GuardianStatue{ "piertotum locomotor", "stone", 328, "warrior with poleax" };
	encl.addStatue(g1);
	assert(encl.getSize() == 1);
	try {
		encl.addStatue(g1);
		assert(false);
	}
	catch (std::exception&) {
		assert(true);
	}
	encl.deleteStatue("piertotum locomotor");
	assert(encl.getSize() == 0);
	encl.addStatue(g1);
}


void Tests::testController() {
	std::cout << "Testing controller\n";
	Encyclopedia encl = Encyclopedia();
	Enchantment ench = Enchantment(encl);
	assert(ench.getSize() == 0);
	ench.addGuardianStatue("piertotum locomotor", "stone", 328, "warrior with poleax");
	assert(ench.getSize() == 1);
	ench.deleteGuardianStatue("piertotum locomotor");
	assert(ench.getSize() == 0);
}