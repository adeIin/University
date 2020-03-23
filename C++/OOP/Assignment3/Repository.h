#pragma once
#include "Domain.h"

typedef struct {
	Ingredient ingredients[100];
	int lenght;
} IngredientRepo;
 
IngredientRepo createRepo();
int getLenght(IngredientRepo* repo);
int addIngredient(IngredientRepo* repo, Ingredient ingr);
Ingredient* getIngredients(IngredientRepo* repo);
int deleteIngredient(IngredientRepo* repo, Ingredient ingr);
int updateIngredient(IngredientRepo* repo, Ingredient ingr);