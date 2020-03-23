#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
	int catalogueNumber;
	char* state;
	char* type;
	int value;
} Ingredient;


//Function that creates an Ingredient
//pre:  catalogueNumber - int, the id of the ingredient
//		state - char, the state of the ingredient
//		type - char, the type of the ingredient
//		value - int, the value of the ingredient
//post: a pointer to the created ingredient
Ingredient* createIngredient(int catalogueNumber, char* state, char* type, int value);

//Function that destroys an Ingredient
//pre:  ingr - Ingredient, the ingredient that needs to be destroyed
//post: -
void destroyIngredient(Ingredient* ingr);

//Function that copies an Ingredient
//pre:  ingr - Ingredient, the ingredient that needs to be copied
//post: a pointer to the copied ingredient
Ingredient* copyIngredient(Ingredient* ingr);

//Function that gets the catalogue number of an Ingredient
//pre:  ingr - Ingredient
//post: the catalogue number of the ingredient
int getCatalogueNumberDomain(Ingredient* ingr);

//Function that gets the state of an Ingredient
//pre:  ingr - Ingredient
//post: a pointer to the state of the ingredient
char* getStateDomain(Ingredient* ingr);

//Function that gets the type of an Ingredient
//pre:  ingr - Ingredient
//post: a pointer to the type of the ingredient
char* getTypeDomain(Ingredient* ingr);

//Function that gets the value of an ingredient
//pre:  ingr - Ingredient
//post: the value of the ingredient
int getValueDomain(Ingredient* ingr);

//Function that converts an Ingredient to string
//pre:  ingr - Ingredient
//		str - char, pointer to the string were the ingredient will be stored
//post: -
void toString(Ingredient* ingr, char* str);