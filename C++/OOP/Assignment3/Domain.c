#include "Domain.h"
#include <string.h>
#include <stdio.h>

Ingredient createIngredient(int number, char state[], char type[], double value) {
	Ingredient ingr;
	ingr.catalogueNumber = number;
	strcpy(ingr.state, state);
	strcpy(ingr.type, type);
	ingr.value = value;
	return ingr;
}

int getCatalogueNumber(Ingredient* ingr) {
	return ingr->catalogueNumber;
}

char* getState(Ingredient* ingr) {
	return ingr->state;
}

char* getType(Ingredient* ingr) {
	return ingr->type;
}

double getValue(Ingredient* ingr) {
	return ingr->value;
}

void ingredientToString(Ingredient ingr, char str[]) {
	sprintf(str, "Ingredient information:\nCatalogue number: %d \nState: %s \nType: %s \nValue: %.2lf\n", ingr.catalogueNumber, ingr.state, ingr.type, ingr.value);
}