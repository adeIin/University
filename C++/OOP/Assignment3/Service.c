#include "Service.h"
#include <stdio.h>
#include <string.h>

Controller createController(IngredientRepo* repo) {
	Controller ctrl;
	ctrl.repo = repo;
	return ctrl;
}

int addIngredientController(Controller* ctrl, int catalogueNumber, char* state, char* type, double value) {
	Ingredient ingr = createIngredient(catalogueNumber, state, type, value);
	return addIngredient(ctrl->repo, ingr);
}

int deleteIngredientController(Controller* ctrl, int catalogueNumber) {
	Ingredient ingr = createIngredient(catalogueNumber, " ", " ", 0.0);
	return deleteIngredient(ctrl->repo, ingr);
}

int updateIngredientController(Controller* ctrl, int catalogueNumber, char* newState, char* newType, double newValue) {
	Ingredient ingr = createIngredient(catalogueNumber, newState, newType, newValue);
	return updateIngredient(ctrl->repo, ingr);
}

Ingredient* getAllIngredients(Controller* ctrl) {
	Ingredient* ingredients = getIngredients(ctrl->repo);
	for (int i = 0; i <= getLenghtCtrl(ctrl) - 1; i++) {
		for (int j = i + 1; j <= getLenghtCtrl(ctrl); j++) {
			if (ingredients[i].catalogueNumber < ingredients[j].catalogueNumber) {
				Ingredient aux;
				aux = ingredients[i];
				ingredients[i] = ingredients[j];
				ingredients[j] = aux;
			}
		}
	}
	return ingredients;
}

Ingredient* getIngredientsByType(Controller* ctrl, char* type, int* position) {
	Ingredient* ingredients = getAllIngredients(ctrl);
	Ingredient result[100];
	Ingredient ingr = createIngredient(0, " ", type, 0.0);
	*position = -1;
	for (int i = 0; i <= getLenghtCtrl(ctrl); i++) {
		if (strcmp(ingredients[i].type, ingr.type) == 0) {
			result[++(*position)] = ingredients[i];
		}
	}
	return result;
}

int getLenghtCtrl(Controller* ctrl) {
	return getLenght(ctrl->repo);
}