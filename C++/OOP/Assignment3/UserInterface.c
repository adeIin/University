#include "UserInterface.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


UI createUI(Controller* ctrl) {
	UI ui;
	ui.ctrl = ctrl;
	return ui;
}

void printMenu() {
	printf("Menu:\n");
	printf("'exit' to exit the app;\n");
	printf("'add catalogue_number state type value' to add an ingredient;\n");
	printf("\n");
}

void run(UI* ui) {
	char commands[6][7]= {"exit\n", "add", "delete", "update", "list", "list\n"};
	char parameters[4][25];
	char command[100], firstWord[20];
	int commandNumber = 0, noOfParameters = 0;
	while (1) {
		printMenu();
		readStringSpaces("Input command:\n>>>", command);
		printf("\n");
		getFirstWord(command, firstWord);
		commandNumber = getCommandNumber(firstWord, commands);
		while (validCommand(commandNumber) == 0) {
			printf("Invalid command!\n\n");
			readStringSpaces("Input command:\n>>>", command);
			printf("\n");
			getFirstWord(command, firstWord);
			commandNumber = getCommandNumber(firstWord, commands);
		}
		if (commandNumber == 0) {
			break;
		}
		getParameters(command, parameters, &noOfParameters);
		switch (commandNumber) {
		case 1: {
			int result = addIngredientUI(ui, parameters, noOfParameters);
			if (result == 0) {
				printf("No!\n\n");
			}
			else {
				if (result == 1) {
					printf("Ingredient successfully added!\n\n");
				}
				else {
					if (result == -1) {
						printf("Invalid number of parameters!\n\n");
					}
					else {
						printf("Invalid parameters!\n\n");
					}
				}
			}
			break;
		}
		case 2: {
			int result = deleteIngredientUI(ui, parameters, noOfParameters);
			if (result == 0) {
				printf("No!\n\n");
			}
			else {
				if (result == 1) {
					printf("Ingredient successfully deleted!\n\n");
				}
				else {
					if (result == -1) {
						printf("Invalid number of parameters!\n\n");
					}
					else {
						printf("Invalid parameters!\n\n");
					}
				}
			}
			break;
		}
		case 3: {
			int result = updateIngredientUI(ui, parameters, noOfParameters);
			if (result == 0) {
				printf("No!\n\n");
			}
			else {
				if (result == 1) {
					printf("Ingredient successfully updated!\n\n");
				}
				else {
					if (result == -1) {
						printf("Invalid number of parameters!\n\n");
					}
					else {
						printf("Invalid parameters!\n\n");
					}
				}
			}
			break;
		}
		case 4: {
			int result = listIngredientsByTypeUI(ui, parameters, noOfParameters);
			if (result == -1) {
				printf("Invalid number of parameters!\n\n");
			}
			break;
		}
		case 5: {
			listAllIngredients(ui);
			break;
		}
		}
	}
}

int getCommandNumber(char firstWord[], char commands[][7]) {
	for (int i = 0; i <= 5; i++) {
		if (strcmp(firstWord, commands[i]) == 0) {
			return i;
		}
	}
	return -1;
}

void getParameters(char command[], char parameters[][25], int* noOfParameters) {
	int pos = -1;
	char* token = strtok(command, " ");
	token = strtok(NULL, " ");
	while (token != NULL) {
		strcpy(parameters[++pos], token);
		token = strtok(NULL, " ");
	}
	*noOfParameters = pos + 1;
}

void readStringSpaces(char message[], char str[]) {
	char readingString[100];
	printf("%s", message);
	fgets(readingString, 100, stdin);
	strcpy(str, readingString);
}

void getFirstWord(char input[], char output[]) {
	char inputCopy[100];
	strcpy(inputCopy, input);
	char* token = strtok(inputCopy, " ");
	strcpy(output, token);
}

int validCommand(int command) {
	if (command >= 0 && command <= 5) {
		return 1;
	}
	return 0;
}

void stringToInteger(char str[], int* number, int* flag) {
	if (str[strlen(str) - 1] == '\n') {
		str[strlen(str) - 1] = NULL;
	}
	*number = atoi(str);
	int numbers[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }, ok = 0;
	for (int i = 0; i < strlen(str); i++) {
		ok = 0;
		for (int j = 0; j <= 9; j++) {
			if (str[i] - '0' == numbers[j]) {
				ok = 1;
				//break;
			}
		}
		if (ok == 0) {
			*flag = 1;
			break;
		}
	}
}

void stringToDouble(char str[], double* number, int* flag) {
	if (str[strlen(str) - 1] == '\n') {
		str[strlen(str) - 1] = NULL;
	}
	*number = atof(str);
	int numbers[10] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }, ok = 0, ok2 = 0;
	for (int i = 0; i < strlen(str); i++) { 
		ok = 0;
		for (int j = 0; j <= 9; j++) {
			if (str[i] - '0' == numbers[j]) {
				ok = 1;
			}
		}
		if (str[i] == '.' && ok2 == 0) {
			ok2 = 1;
			ok = 1;
		}
		if (ok == 0) {
			*flag = 1;
			break;
		}
	}
}

int addIngredientUI(UI* ui, char parameters[][25], int noOfParameters) {
	if (noOfParameters != 4) {
		return -1;
	}
	int flag = 0;
	int catalogueNumber = 0;
	stringToInteger(parameters[0], &catalogueNumber, &flag);
	if (flag == 1) {
		return -2;
	}
	char state[256], type[256];
	strcpy(state, parameters[1]);
	strcpy(type, parameters[2]);
	double value = 0.0;
	stringToDouble(parameters[3], &value, &flag);
	if (flag == 1) {
		return -2;
	}
	return addIngredientController(ui->ctrl, catalogueNumber, state, type, value);
}

int deleteIngredientUI(UI* ui, char parameters[][25], int noOfParameters) {
	if (noOfParameters != 1) {
		return -1;
	}
	int flag = 0;
	int catalogueNumber = 0;
	stringToInteger(parameters[0], &catalogueNumber, &flag);
	if (flag == 1) {
		return -2;
	}
	return deleteIngredientController(ui->ctrl, catalogueNumber);
}

int updateIngredientUI(UI* ui, char parameters[][25], int noOfParameters) {
	if (noOfParameters != 4) {
		return -1;
	}
	int flag = 0;
	int catalogueNumber = 0;
	stringToInteger(parameters[0], &catalogueNumber, &flag);
	if (flag == 1) {
		return -2;
	}
	char newState[256], newType[256];
	strcpy(newState, parameters[1]);
	strcpy(newType, parameters[2]);
	double newValue = 0.0;
	stringToDouble(parameters[3], &newValue, &flag);
	if (flag == 1) {
		return -2;
	}
	return updateIngredientController(ui->ctrl, catalogueNumber, newState, newType, newValue);
}

void listAllIngredients(UI* ui) {
	Ingredient* ingredients = getAllIngredients(ui->ctrl);
	for (int i = 0; i <= getLenghtCtrl(ui->ctrl); i++) {
		char str[256];
		ingredientToString(ingredients[i], str);
		printf("Ingredient no: %d\n%s\n", i + 1, str);
	}
}

int listIngredientsByTypeUI(UI* ui, char parameters[][25], int noOfParameters) {
	if (noOfParameters != 1) {
		return -1;
	}
	int lenght = 0;
	char type[256];
	strcpy(type, parameters[0]);
	type[strlen(type) - 1] = NULL;
	Ingredient* ingredients = getIngredientsByType(ui->ctrl, type, &lenght);
	for (int i = 0; i <= lenght; i++) {
		char str[256];
		ingredientToString(ingredients[i], str);
		printf("Ingredient no: %d\n%s\n", i + 1, str);
	}
	return 1;
}
