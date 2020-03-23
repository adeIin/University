#include "UserInterface.h"
#include "Tests.h"
#include <crtdbg.h>
#define _CRTDBG_MAP_ALLOC



int main() {
	testAll();
	IngredientRepo* repo = createRepo();
	Controller* ctrl = createController(repo);
	UI* ui = createUI(ctrl);
	run(ui);
	destroyUI(ui);
	_CrtSetReportMode(_CRT_WARN, _CRTDBG_MODE_FILE);
	_CrtSetReportFile(_CRT_WARN, _CRTDBG_FILE_STDOUT);
	_CrtSetReportMode(_CRT_ERROR, _CRTDBG_MODE_FILE);
	_CrtSetReportFile(_CRT_ERROR, _CRTDBG_FILE_STDOUT);
	_CrtSetReportMode(_CRT_ASSERT, _CRTDBG_MODE_FILE);
	_CrtSetReportFile(_CRT_ASSERT, _CRTDBG_FILE_STDOUT);
	_CrtDumpMemoryLeaks();
	return 0;
}