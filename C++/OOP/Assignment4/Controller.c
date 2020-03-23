#include "Controller.h"


Controller* createController(IngredientRepo* repo) {
	Controller* ctrl = (Controller*)malloc(sizeof(Controller));
	Stack* undoStack = createStack(sizeof(UndoRedoAction), 10);
	Stack* redoStack = createStack(sizeof(UndoRedoAction), 10);
	if (ctrl) {
		ctrl->repo = repo;
		ctrl->undoStack = undoStack;
		ctrl->redoStack = redoStack;
	}
	return ctrl;
}


void destroyController(Controller* ctrl) {
	destroyRepo(ctrl->repo);
	destroyStack(ctrl->undoStack);
	destroyStack(ctrl->redoStack);
	free(ctrl);
}


int addIngredientController(Controller* ctrl, int catalogueNumber, char* state, char* type, int value) {
	Ingredient* ingr = createIngredient(catalogueNumber, state, type, value);
	Ingredient* copy1 = copyIngredient(ingr);
	Ingredient* copy2 = copyIngredient(ingr);
	UndoRedoAction* action = createUndoRedoAction(copy1, copy2, 1, 2);
	int result = addIngredientRepository(ctrl->repo, ingr);
	if (result == 1) {
		pushStack(ctrl->undoStack, action);
		clearStack(ctrl->redoStack);
	}
	destroyUndoRedoAction(action);
	destroyIngredient(ingr);
	destroyIngredient(copy1);
	destroyIngredient(copy2);

	return result;
}


int deleteIngredientController(Controller* ctrl, int catalogueNumber) {
	Ingredient* ingr = copyIngredient(getIngredientByCatalogueNumber(ctrl->repo, catalogueNumber));
	Ingredient* copy1 = copyIngredient(ingr);
	Ingredient* copy2 = copyIngredient(ingr);
	UndoRedoAction* action = createUndoRedoAction(copy1, copy2, 2, 1);
	int result = deleteIngredientRepository(ctrl->repo, catalogueNumber);
	if (result == 1) {
		pushStack(ctrl->undoStack, action);
		clearStack(ctrl->redoStack);
	}
	destroyIngredient(ingr);
	destroyIngredient(copy1);
	destroyIngredient(copy2);
	destroyUndoRedoAction(action);
	return result;
}


int updateIngredientController(Controller* ctrl, int catalogueNumber, char* state, char* type, int value) {
	Ingredient* newIngr = createIngredient(catalogueNumber, state, type, value);
	Ingredient* oldIngr = copyIngredient(getIngredientByCatalogueNumber(ctrl->repo, catalogueNumber));
	Ingredient* copy1 = copyIngredient(newIngr);
	Ingredient* copy2 = copyIngredient(oldIngr);
	UndoRedoAction* action = createUndoRedoAction(copy1, copy2, 3, 3);
	int result = updateIngredientRepository(ctrl->repo, newIngr);
	if (result == 1) {
		pushStack(ctrl->undoStack, action);
		clearStack(ctrl->redoStack);
	}
	destroyIngredient(newIngr);
	destroyIngredient(oldIngr);
	destroyIngredient(copy1);
	destroyIngredient(copy2);
	destroyUndoRedoAction(action);
	return result;
}


IngredientRepo* getAllIngredients(Controller* ctrl) {
	return ctrl->repo;
}


IngredientRepo* getIngredientsByTypeController(Controller* ctrl, char* type) {
	IngredientRepo* resultRepo = createRepo();
	for (int i = 0; i < getLengthRepo(ctrl->repo); i++) {
		Ingredient* ingr = ctrl->repo->ingredients->elements[i];
		if (strcmp(getTypeDomain(ingr), type) == 0) {
			addIngredientRepository(resultRepo, ingr);
		}
		//destroyIngredient(ingr);
	}
	return resultRepo;
}


IngredientRepo* getIngredientsByValueController(Controller* ctrl, int value) {
	IngredientRepo* resultRepo = createRepo();
	for (int i = 0; i < getLengthRepo(ctrl->repo); i++) {
		Ingredient* ingr = ctrl->repo->ingredients->elements[i];
		if (getValueDomain(ingr) < value) {
			addIngredientRepository(resultRepo, ingr);
		}
	}
	for (int i = 0; i < getLengthRepo(resultRepo) - 1; i++) {
		for (int j = i + 1; j < getLengthRepo(resultRepo); j++) {
			if (strcmp(getStateDomain(resultRepo->ingredients->elements[i]), getStateDomain(resultRepo->ingredients->elements[j])) > 0) {
				Ingredient* aux = resultRepo->ingredients->elements[i];
				resultRepo->ingredients->elements[i] = resultRepo->ingredients->elements[j];
				resultRepo->ingredients->elements[j] = aux;
			}
		}
	}
	return resultRepo;
}


int getLengthController(Controller* ctrl) {
	return getLengthRepo(ctrl->repo);
}


int undo(Controller* ctrl) {
	if (ctrl->undoStack->top == -1) {
		return 0;
	}
	UndoRedoAction* action = popStack(ctrl->undoStack);
	if (getAction(action) == 1) {
		Ingredient* ingr1 = getIngredient1(action);
		deleteIngredientRepository(ctrl->repo, getCatalogueNumberDomain(ingr1));
		UndoRedoAction* redoAction = getOpposite(action);
		pushStack(ctrl->redoStack, redoAction);
		destroyUndoRedoAction(redoAction);
		//destroyIngredient(ingr1);
	}
	if (getAction(action) == 2) {
		addIngredientRepository(ctrl->repo, getIngredient1(action));
		UndoRedoAction* redoAction = getOpposite(action);
		pushStack(ctrl->redoStack, redoAction);
		destroyUndoRedoAction(redoAction);
	}
	if (getAction(action) == 3) {
		updateIngredientRepository(ctrl->repo, getIngredient1(action));
		UndoRedoAction* redoAction = getOpposite(action);
		pushStack(ctrl->redoStack, action);
		destroyUndoRedoAction(redoAction);
	}
	destroyUndoRedoAction(action);
	return 1;
}


int redo(Controller* ctrl) {
	if (ctrl->redoStack->top == -1) {
		return 0;
	}
	UndoRedoAction* action = popStack(ctrl->redoStack);

	if (getAction(action) == 1) {
		Ingredient* ingr = getIngredient1(action);
		deleteIngredientRepository(ctrl->repo, getCatalogueNumberDomain(ingr));
		UndoRedoAction* undoAction = getOpposite(action);
		pushStack(ctrl->undoStack, undoAction);
		//destroyIngredient(ingr);
		destroyUndoRedoAction(undoAction);
	}
	if (getAction(action) == 2) {
		addIngredientRepository(ctrl->repo, getIngredient1(action));
		UndoRedoAction* undoAction = getOpposite(action);
		pushStack(ctrl->undoStack, undoAction);
		destroyUndoRedoAction(undoAction);
	}
	if (getAction(action) == 3) {
		updateIngredientRepository(ctrl->repo, getIngredient2(action));
		UndoRedoAction* undoAction = getOpposite(action);
		pushStack(ctrl->undoStack, action);
		destroyUndoRedoAction(undoAction);
	}
	destroyUndoRedoAction(action);
	return 1;
}

