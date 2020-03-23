#include "Repository.h"
#include "DynamicArray.h"


IngredientRepo* createRepo() {
	IngredientRepo* repo = (IngredientRepo*)malloc(sizeof(IngredientRepo));
	if (repo) {
		repo->ingredients = createDynamicArray(10, &destroyIngredient);
	}
	return repo;
}


void destroyRepo(IngredientRepo* repo) {
	if (repo == NULL) {
		return;
	}
	destroyDynamicArray(repo->ingredients);
	free(repo);
}


int addIngredientRepository(IngredientRepo* repo, Ingredient* ingr) {
	if (repo == NULL) {
		return 0;
	}
	for (int i = 0; i < getLengthRepo(repo); i++) {
		if (getCatalogueNumberDomain(repo->ingredients->elements[i]) == getCatalogueNumberDomain(ingr)) {
			return 0;
		}
	}
	Ingredient* copy = copyIngredient(ingr);
	addDynamicArray(repo->ingredients, copy);
	return 1;
}


int deleteIngredientRepository(IngredientRepo* repo, int catalogueNumber) {
	if (repo == NULL) {
		return 0;
	}
	if (repo->ingredients == NULL) {
		return 0;
	}
	for (int i = 0; i < getLengthRepo(repo); i++) {
		if (getCatalogueNumberDomain(repo->ingredients->elements[i]) == catalogueNumber) {
			deleteDynamicArray(repo->ingredients, i);
			return 1;
		}
	}
	return 0;
}


int updateIngredientRepository(IngredientRepo* repo, Ingredient* ingr) {
	if (repo == NULL) {
		return 0;
	}
	for (int i = 0; i < getLengthRepo(repo); i++) {
		if (getCatalogueNumberDomain(repo->ingredients->elements[i]) == getCatalogueNumberDomain(ingr)) {
			deleteIngredientRepository(repo, getCatalogueNumberDomain(ingr));
			addIngredientRepository(repo, ingr);
			return 1;
		}
	}
	return 0;
}


int getLengthRepo(IngredientRepo* repo) {
	return getLength(repo->ingredients);
}


Ingredient* getIngredientByCatalogueNumber(IngredientRepo* repo, int catalogueNumber) {
	for (int i = 0; i < getLengthRepo(repo); i++) {
		if (getCatalogueNumberDomain(repo->ingredients->elements[i]) == catalogueNumber) {
			return getIngredientByPosition(repo, i);
		}
	}
	return NULL;
}

Ingredient* getIngredientByPosition(IngredientRepo* repo, int pos) {
	if (repo == NULL) {
		return NULL;
	}
	if (pos < 0 || pos >= getLengthRepo(repo)) {
		return NULL;
	}
	return getElemDynamicArray(repo->ingredients, pos);
}

