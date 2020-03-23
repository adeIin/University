#pragma once

typedef struct {
	int catalogueNumber;
	char state[50];
	char type[50];
	double value;
} Ingredient;

Ingredient createIngredient(int number, char state[], char type[], double value);

int getCatalogueNumber(Ingredient* ingr);
char* getState(Ingredient* ingr);
char* getType(Ingredient* ingr);
double getValue(Ingredient* ingr);

void ingredientToString(Ingredient ingr, char str[]);
