#include "UserInterface.h"


UI* createUI(Controller* ctrl) {
	UI* ui = (UI*)malloc(sizeof(UI));
	if (ui) {
		ui->ctrl = ctrl;
	}
	return ui;
}


void destroyUI(UI* ui) {
	destroyController(ui->ctrl);
	free(ui);
}


void printMenu() {
	printf("Menu:\n");
	printf("'exit' to exit the app;\n");
	printf("'add catalogueNumber, state, type, value' to add an ingredient;\n");
	printf("'update catalogueNumber, newState, newType, newValue' to update an ingredient;\n");
	printf("'delete catalogueNumber' to delete an ingredient;\n");
	printf("'list' to list all ingredients;\n");
	printf("'list type' to list ingredients by type\n");
	printf("'undo'\n");
	printf("'redo'\n");
	printf("\n");
}

void readStringSpaces(char message[], char str[]) {
	char readingString[100];
	printf("%s", message);
	fgets(readingString, 100, stdin);
	strcpy(str, readingString);
}

void removeComma(char* str) {
	if (str[strlen(str) - 1] == ',') {
		str[strlen(str) - 1] = '\0';
	}
}

void getFirstWord(char input[], char output[]) {
	char inputCopy[100];
	strcpy(inputCopy, input);
	char* token = strtok(inputCopy, " ");
	strcpy(output, token);
}

int validCommand(int command) {
	if (command >= 0 && command <= 8) {
		return 1;
	}
	return 0;
}

void stringToInteger(char str[], int* number, int* flag) {
	if (str[strlen(str) - 1] == '\n') {
		str[strlen(str) - 1] = '\0';
	}
	*number = atoi(str);
	*flag = 0;
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

int getCommandNumber(char firstWord[], char commands[][7]) {
	for (int i = 0; i <= 7; i++) {
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


void listAllIngredients(UI* ui) {
	IngredientRepo* repo = getAllIngredients(ui->ctrl);
	for (int i = 0; i < getLengthController(ui->ctrl); i++) {
		char str[256];
		toString(repo->ingredients->elements[i], str);
		printf("%s\n", str);
	}
	printf("\n");
}

int addIngredientUI(UI* ui, char parameters[][25], int noOfParameters) {
	if (noOfParameters != 4) {
		return -1;
	}
	for (int i = 0; i < noOfParameters; i++) {
		removeComma(parameters[i]);
	}
	int flag = 0;
	int catalogueNumber = 0;
	stringToInteger(parameters[0], &catalogueNumber, &flag);
	if (flag == 1) {
		return -1;
	}
	char state[256], type[256];
	strcpy(state, parameters[1]);
	strcpy(type, parameters[2]);
	int value = 0;
	stringToInteger(parameters[3], &value, &flag);
	if (flag == 1) {
		return -1;
	}
	return addIngredientController(ui->ctrl, catalogueNumber, state, type, value);
}


int deleteIngredientUI(UI* ui, char parameters[][25], int noOfParameters) {
	if (noOfParameters != 1) {
		return -1;
	}
	for (int i = 0; i < noOfParameters; i++) {
		removeComma(parameters[i]);
	}
	int flag = 0;
	int catalogueNumber = 0;
	stringToInteger(parameters[0], &catalogueNumber, &flag);
	if (flag == 1) {
		return -1;
	}
	return deleteIngredientController(ui->ctrl, catalogueNumber);
}

int updateIngredientUI(UI* ui, char parameters[][25], int noOfParameters) {
	if (noOfParameters != 4) {
		return -1;
	}
	for (int i = 0; i < noOfParameters; i++) {
		removeComma(parameters[i]);
	}
	int flag = 0;
	int catalogueNumber = 0;
	stringToInteger(parameters[0], &catalogueNumber, &flag);
	if (flag == 1) {
		return -1;
	}
	char newState[256], newType[256];
	strcpy(newState, parameters[1]);
	strcpy(newType, parameters[2]);
	int newValue = 0;
	stringToInteger(parameters[3], &newValue, &flag);
	if (flag == 1) {
		return -1;
	}
	return updateIngredientController(ui->ctrl, catalogueNumber, newState, newType, newValue);
}

int listIngredientsByTypeUI(UI* ui, char parameters[][25], int noOfParameters) {
	if (noOfParameters != 1) {
		return -1;
	}
	int number = 0, flag = 0;
	stringToInteger(parameters[0], &number, &flag);
	if (flag == 1) {
		char type[256];
		strcpy(type, parameters[0]);
		IngredientRepo* resultRepo = getIngredientsByTypeController(ui->ctrl, type);
		for (int i = 0; i < getLengthRepo(resultRepo); i++) {
			char str[256];
			toString(resultRepo->ingredients->elements[i], str);
			printf("%s\n", str);
		}
		destroyRepo(resultRepo);
		printf("\n");
	}
	else {
		IngredientRepo* repo = getIngredientsByValueController(ui->ctrl, number);
		for (int i = 0; i < getLengthRepo(repo); i++) {
			char str1[256];
			toString(repo->ingredients->elements[i], str1);
			printf("%s\n", str1);
		}
		destroyRepo(repo);
		printf("\n");
	}
	return 1;
}

int undoUI(UI* ui) {
	return undo(ui->ctrl);
}

int redoUI(UI* ui) {
	return redo(ui->ctrl);
}

void run(UI* ui) {
	char commands[8][7] = { "exit\n", "add", "delete", "update", "list", "list\n", "undo\n", "redo\n" };
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
		case 6: {
			int rez = undoUI(ui);
			if (rez == 0) {
				printf("No more undo!\n\n");
			}
			else {
				printf("Undo successfully!\n\n");
			}
			break;
		}
		case 7: {
			int rez = redoUI(ui);
			if (rez == 0) {
				printf("No more redo!\n\n");
			}
			else {
				printf("Redo successfully!\n\n");
			}
			break;
		}
		}
	}
}
