#pragma once
#include "Repository.h"

typedef struct {
	IngredientRepo* repo;
} Controller;

Controller createController(IngredientRepo*);
int addIngredientController(Controller* ctrl, int catalogueNumber, char* state, char* type, double value);
Ingredient* getAllIngredients(Controller* ctrl);
int getLenghtCtrl(Controller* ctrl);
int deleteIngredientController(Controller* ctrl, int catalogueNumber);
int updateIngredientController(Controller* ctrl, int catalogueNumber, char* newState, char* newType, double newValue);
Ingredient* getIngredientsByType(Controller* ctrl, char* type, int*position);