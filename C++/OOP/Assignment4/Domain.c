#include "Domain.h"


Ingredient* createIngredient(int catalogueNumber,
	char* state, char* type, int value) {
	Ingredient* ingr = (Ingredient*)malloc(sizeof(Ingredient));
	if (ingr == NULL) {
		return NULL;
	}
	ingr->catalogueNumber = catalogueNumber;
	ingr->state = (char*)malloc(sizeof(char) * (strlen(state) + 1));
	if (ingr->state) {
		strcpy(ingr->state, state);
	}
	ingr->type = (char*)malloc(sizeof(char) * (strlen(type) + 1));
	if (ingr->type) {
		strcpy(ingr->type, type);
	}
	ingr->value = value;

	return ingr;
}

void destroyIngredient(Ingredient* ingr) {
	if (ingr == NULL) {
		return;
	}
	free(ingr->state);
	free(ingr->type);
	free(ingr);
}

Ingredient* copyIngredient(Ingredient* ingr) {
	if (ingr == NULL) {
		return NULL;
	}
	Ingredient* newIngr = createIngredient(getCatalogueNumberDomain(ingr),
		getStateDomain(ingr), getTypeDomain(ingr), getValueDomain(ingr));
	return newIngr;
}

int getCatalogueNumberDomain(Ingredient* ingr) {
	return ingr->catalogueNumber;
}

char* getStateDomain(Ingredient* ingr) {
	return ingr->state;
}

char* getTypeDomain(Ingredient* ingr) {
	return ingr->type;
}

int getValueDomain(Ingredient* ingr) {
	return ingr->value;
}

void toString(Ingredient* ingr, char* str) {
	sprintf(str, "%d %s %s %d", getCatalogueNumberDomain(ingr),
		getStateDomain(ingr), getTypeDomain(ingr), getValueDomain(ingr));
}
