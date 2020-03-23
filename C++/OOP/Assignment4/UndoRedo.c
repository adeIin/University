#include "UndoRedo.h"


UndoRedoAction* createUndoRedoAction(Ingredient* ingr1, Ingredient* ingr2, int action, int reverseAction) {
	UndoRedoAction* ura = (UndoRedoAction*)malloc(sizeof(UndoRedoAction));
	if (ura == NULL) {
		return NULL;
	}
	ura->action = action;
	ura->reverseAction = reverseAction;
	Ingredient* copy1 = copyIngredient(ingr1);
	Ingredient* copy2 = copyIngredient(ingr2);
	ura->ingr1 = copy1;
	ura->ingr2 = copy2;

	return ura;
}


void destroyUndoRedoAction(UndoRedoAction* ura) {
	if (ura == NULL) {
		return;
	}
	destroyIngredient(ura->ingr1);
	destroyIngredient(ura->ingr2);
	free(ura);
}


int getAction(UndoRedoAction* ura) {
	return ura->action;
}


int getReverseAction(UndoRedoAction* ura) {
	return ura->reverseAction;
}


Ingredient* getIngredient1(UndoRedoAction* ura) {
	return ura->ingr1;
}


Ingredient* getIngredient2(UndoRedoAction* ura) {
	return ura->ingr2;
}


UndoRedoAction* copyUndoRedoAction(UndoRedoAction* ura) {
	if (ura == NULL) {
		return NULL;
	}
	UndoRedoAction* copy = createUndoRedoAction(getIngredient1(ura), getIngredient2(ura), getAction(ura), getReverseAction(ura));

	return copy;
}


UndoRedoAction* getOpposite(UndoRedoAction* ura) {
	UndoRedoAction* uraOpposite = createUndoRedoAction(ura->ingr2, ura->ingr1, ura->reverseAction, ura->action);
	return uraOpposite;
}


///////////////////////////////////////////////////////////////////////////////////////////////////////////////


Stack* createStack() {
	Stack* stack = (Stack*)malloc(sizeof(Stack));
	if (stack) {
		stack->top = -1;
	}
}


void destroyStack(Stack* stack) {
	if (stack == NULL) {
		return;
	}
	for (int i = 0; i <= stack->top; i++) {
		destroyUndoRedoAction(stack->items[i]);
	}
	free(stack);
}


void pushStack(Stack* stack, UndoRedoAction* ura) {
	if (stack->top == 100) {
		return;
	}
	stack->items[++stack->top] = copyUndoRedoAction(ura);
}


UndoRedoAction* popStack(Stack* stack) {
	if (stack->top == -1) {
		return;
	}
	return stack->items[stack->top--];
}


void clearStack(Stack* stack) {
	for (int i = 0; i <= stack->top; i++) {
		destroyUndoRedoAction(stack->items[i]);
	}
	stack->top = -1;
}
