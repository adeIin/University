#pragma once
#include "Domain.h"
#include "DynamicArray.h"


typedef struct {
	DynamicArray* ingredients;
} IngredientRepo;


//Function that creates the repository
IngredientRepo* createRepo();


//Function that destroys the repository
void destroyRepo(IngredientRepo* repo);


//Function that adds an ingredient to the repository
int addIngredientRepository(IngredientRepo* repo, Ingredient* ingr);


//Function that deletes an ingredient from the repository
int deleteIngredientRepository(IngredientRepo* repo, int catalogueNumber);


//Function that updates an ingredient from the repository
int updateIngredientRepository(IngredientRepo* repo, Ingredient* ingr);


//Function that gets the length of the repository
int getLengthRepo(IngredientRepo* repo);


//Function that gets an ingredient by catalogueNumber
Ingredient* getIngredientByCatalogueNumber(IngredientRepo* repo, int catalogueNumber);


//Function that gets an ingredient by position
Ingredient* getIngredientByPosition(IngredientRepo* repo, int pos);
