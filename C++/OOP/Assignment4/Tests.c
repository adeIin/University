#include "Tests.h"
#include "Domain.h"
#include "Repository.h"
#include "DynamicArray.h"
#include "Controller.h"
#include "UndoRedo.h"
#include <assert.h>


void testDomain() {
	printf("Domain test\n");
	Ingredient* ingr = createIngredient(1, "state", "type", 10);
	assert(getCatalogueNumberDomain(ingr) == 1);
	assert(getValueDomain(ingr) == 10);
	assert(strcmp(getStateDomain(ingr), "state") == 0);
	assert(strcmp(getTypeDomain(ingr), "type") == 0);
	destroyIngredient(ingr);
}


void testDynamicArray() {
	printf("Dynamic Array test\n");
	DynamicArray* array = createDynamicArray(10, &destroyIngredient);
	Ingredient* ingr = createIngredient(1, "state", "type", 10);
	addDynamicArray(array, ingr);
	deleteDynamicArray(array, 0);
	Ingredient* ingr1 = createIngredient(1, "state", "type", 10);
	addDynamicArray(array, ingr1);
	Ingredient* ingr2 = getElemDynamicArray(array, 0);
	assert(getCatalogueNumberDomain(ingr2) == getCatalogueNumberDomain(ingr1));
	deleteDynamicArray(array, 0);
	assert(getLength(array) == 0);
	destroyDynamicArray(array);
}


void testRepository() {
	printf("Repository test\n");
	IngredientRepo* repo = createRepo();
	Ingredient* ingr = createIngredient(10, "sd", "sd", 3);
	int result = addIngredientRepository(repo, ingr);
	Ingredient* ingr1 =  getIngredientByPosition(repo, 0);
	assert(getCatalogueNumberDomain(ingr1) == getCatalogueNumberDomain(ingr));
	deleteIngredientRepository(repo, 10);
	assert(getLengthRepo(repo) == 0);
	addIngredientRepository(repo, ingr);
	Ingredient* ingr2 = createIngredient(10, "adda", "asd", 983);
	updateIngredientRepository(repo, ingr2);
	assert(getValueDomain(getIngredientByCatalogueNumber(repo, 10)) == 983);
	destroyIngredient(ingr2);
	destroyIngredient(ingr);
	destroyRepo(repo);
}


void testStack() {
	printf("Stack test\n");
	Ingredient* ingr1 = createIngredient(1, "s", "t", 10);
	Ingredient* ingr2 = createIngredient(2, "s", "t", 20);
	UndoRedoAction* ura = createUndoRedoAction(ingr1, ingr2, 1, 2);

	Stack* stack = createStack();
	pushStack(stack, ura);
	assert(stack->top == 0);
	clearStack(stack);
	assert(stack->top == -1);
	pushStack(stack, ura);
	pushStack(stack, ura);
	pushStack(stack, ura);
	pushStack(stack, ura);
	pushStack(stack, ura);
	pushStack(stack, ura);
	pushStack(stack, ura);
	assert(stack->top == 6);
	UndoRedoAction* ura2 = popStack(stack);

	destroyStack(stack);
	destroyIngredient(ingr1);
	destroyIngredient(ingr2);
	destroyUndoRedoAction(ura);
	destroyUndoRedoAction(ura2);
}


void testUndoRedo() {
	printf("Undo and Redo test\n");
	Ingredient* ingr1 = createIngredient(1, "s", "t", 10);
	Ingredient* ingr2 = createIngredient(2, "s", "t", 20);
	UndoRedoAction* ura = createUndoRedoAction(ingr1, ingr2, 1, 2);
	destroyIngredient(ingr1);
	destroyIngredient(ingr2);
	destroyUndoRedoAction(ura);
}


void testController() {
	printf("Controller test\n");
	IngredientRepo* repo = createRepo();
	Controller* ctrl = createController(repo);
	addIngredientController(ctrl, 1, "s", "t", 10);
	deleteIngredientController(ctrl, 1);
	assert(getLengthController(ctrl) == 0);
	undo(ctrl);
	assert(getLengthController(ctrl) == 1);
	redo(ctrl);
	assert(getLengthController(ctrl) == 0);
	undo(ctrl);
	assert(getLengthController(ctrl) == 1);
	updateIngredientController(ctrl, 1, "ds", "kj", 98);
	undo(ctrl);
	redo(ctrl);
	destroyController(ctrl);
}


void testAll() {
	testDomain();
	testDynamicArray();
	testRepository();
	testStack();
	testUndoRedo();
	testController();
	printf("\nAll tests done!\n\n");
}
