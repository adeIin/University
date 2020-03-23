#include "Repository.h"
#include <string.h>
#include <stdio.h>

IngredientRepo createRepo() {
	IngredientRepo repo;
	repo.lenght = -1;
	return repo;
}

int getLenght(IngredientRepo* repo) {
	return repo->lenght;
}

int addIngredient(IngredientRepo* repo, Ingredient ingr) {
	for (int i = 0; i <= repo->lenght; i++) {
		if (repo->ingredients[i].catalogueNumber == ingr.catalogueNumber) {
			return 0;
		}
	}
	repo->lenght = repo->lenght + 1;
	repo->ingredients[repo->lenght].catalogueNumber = ingr.catalogueNumber;
	strcpy(repo->ingredients[repo->lenght].state, ingr.state);
	strcpy(repo->ingredients[repo->lenght].type, ingr.type);
	repo->ingredients[repo->lenght].value = ingr.value;
	return 1;
}

Ingredient* getIngredients(IngredientRepo* repo) {
	return repo->ingredients;
}

int deleteIngredient(IngredientRepo* repo, Ingredient ingr) {
	int position = -1;
	for (int i = 0; i <= repo->lenght; i++) {
		if (repo->ingredients[i].catalogueNumber == ingr.catalogueNumber) {
			position = i;
		}
	}
	if (position == -1) {
		return 0;
	}
	for (int i = position; i <= repo->lenght - 1; i++) {
		repo->ingredients[i] = repo->ingredients[i + 1];
	}
	repo->lenght = repo->lenght - 1;
	return 1;
}

int updateIngredient(IngredientRepo* repo, Ingredient ingr) {
	for (int i = 0; i <= repo->lenght; i++) {
		if (repo->ingredients[i].catalogueNumber == ingr.catalogueNumber) {
			strcpy(repo->ingredients[repo->lenght].state, ingr.state);
			strcpy(repo->ingredients[repo->lenght].type, ingr.type);
			repo->ingredients[repo->lenght].value = ingr.value;
			return 1;
		}
	}
	return 0;
}

