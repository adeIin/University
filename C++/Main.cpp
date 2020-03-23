#define _CRTDBG_MAP_ALLOC
#include <crtdbg.h>
#include "Tests.h"
#include "UserInterface.h"

int main() {

	Tests::testAll();
	{
		Encyclopedia encl = Encyclopedia(); //Repository
		Enchantment ench = Enchantment(encl); //Controller
		//ench.addGuardianStatue("Piertotum Locomotor", "stone", 358, "Warrior with poleax");
		//ench.addGuardianStatue("Laykyun Setkyar", "marble", 287, "Bouddha");
		//ench.addGuardianStatue("Ushiku Daibutsu", "bronze", 890, "Amitabha");
		//ench.addGuardianStatue("Guanyin", "stone", 78, "Guanyin");
		//ench.addGuardianStatue("Emperors Yan and Huang", "rock", 46, "Yan Di et Huang Di");
		//ench.addGuardianStatue("Dai", "marble", 1500, "White Daikannon");
		//ench.addGuardianStatue("Peter the Great", "metal", 708, "Peter the Great");
		//ench.addGuardianStatue("The legendary beauty of the Miao", "marble", 3, "Yang'asha");
		//ench.addGuardianStatue("Birth of the New World", "metal", 236, "Christopher Colombus");
		RunicAltar runicAltar = RunicAltar(ench); //UI
		runicAltar.lightRunicAltar(); //Run program
	}

	_CrtSetReportMode(_CRT_WARN, _CRTDBG_MODE_FILE);
	_CrtSetReportFile(_CRT_WARN, _CRTDBG_FILE_STDOUT);
	_CrtSetReportMode(_CRT_ERROR, _CRTDBG_MODE_FILE);
	_CrtSetReportFile(_CRT_ERROR, _CRTDBG_FILE_STDOUT);
	_CrtSetReportMode(_CRT_ASSERT, _CRTDBG_MODE_FILE);
	_CrtSetReportFile(_CRT_ASSERT, _CRTDBG_FILE_STDOUT);
	_CrtDumpMemoryLeaks();
	return 0;
}