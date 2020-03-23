#pragma once
#include "Repository.h"


typedef struct {
	Ingredient* ingr1;
	Ingredient* ingr2;
	int action;
	int reverseAction;
} UndoRedoAction;


//Function that creates an action
UndoRedoAction* createUndoRedoAction(Ingredient* ingr1, Ingredient* ingr2, int action, int reverseAction);


//Function that destroys an action
void destroyUndoRedoAction(UndoRedoAction* ura);


//Function that gets an action
int getAction(UndoRedoAction* ura);


//Function that gets the reverse action
int getReverseAction(UndoRedoAction* ura);


//Function that gets the first ingredient
Ingredient* getIngredient1(UndoRedoAction* ura);


//Function that gets the second ingredient
Ingredient* getIngredient2(UndoRedoAction* ura);


//Function that copies an action
UndoRedoAction* copyUndoRedoAction(UndoRedoAction* ura);


//Function that gets the opposite of an action
UndoRedoAction* getOpposite(UndoRedoAction* ura);


////////////////////////////////////////////////////////////////////


typedef struct {
	UndoRedoAction* items[100];
	int top;
} Stack;


Stack* createStack();


void destroyStack(Stack* stack);


void pushStack(Stack* stack, UndoRedoAction* ura);


UndoRedoAction* popStack(Stack* stack);


void clearStack(Stack* stack);
