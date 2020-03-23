#include <stdio.h>
#include "UserInterface.h"

int main() {
	IngredientRepo repo = createRepo();
	Controller ctrl = createController(&repo);
	UI ui = createUI(&ctrl);
	run(&ui);

	return 0;
}