#pragma once
#include "Repository.h"
#include "UndoRedo.h"


typedef struct {
	IngredientRepo* repo;
	Stack* undoStack;
	Stack* redoStack;
} Controller;


//Function that creates a controller
Controller* createController(IngredientRepo* repo);


//Function that destroys a controller
void destroyController(Controller* ctrl);


//Function that creates an ingredient and adds it in the repository
int addIngredientController(Controller* ctrl, int catalogueNumber, char* state, char* type, int value);


//Function that deletes an element from the repository
int deleteIngredientController(Controller* ctrl, int catalogueNumber);


//Function that creates an ingredient and replaces the ingredient fromthe repository that have the same
//catalogue number with it
int updateIngredientController(Controller* ctrl, int catalogueNumber, char* state, char* type, int value);


//Function that gets all the ingredients
IngredientRepo* getAllIngredients(Controller* ctrl);


//Function that gets the ingredients by type
IngredientRepo* getIngredientsByTypeController(Controller* ctrl, char* type);


//Function that gets the ingredients by value
IngredientRepo* getIngredientsByValueController(Controller* ctrl, int valu);


//Function that gets the lenght of the repository
int getLengthController(Controller* ctrl);


//Function for the undo
int undo(Controller* ctrl);


//Function for the redo
int redo(Controller* ctrl);