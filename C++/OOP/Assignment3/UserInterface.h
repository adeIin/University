#pragma once
#include "Service.h"

typedef struct {
	Controller* ctrl;
}UI;

UI createUI(Controller* ctrl);
void printMenu();
void run(UI* ui);
int validCommand(int command);
int addIngredientUI(UI* ui, char parameters[][25], int noOfParameters);
void readStringSpaces(char message[], char str[]);
void getFirstWord(char input[], char output[]);
int getCommandNumber(char firstWord[], char commands[][7]);
void getParameters(char command[], char parameters[][25], int* noOfParameters);
void listAllIngredients(UI* ui);