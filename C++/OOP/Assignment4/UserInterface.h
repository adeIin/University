#pragma once
#include "Controller.h"


typedef struct {
	Controller* ctrl;
} UI;


//Function that creates an ui
UI* createUI(Controller* ctrl);


//Function that destroys the ui
void destroyUI(UI* ui);


//Function that starts the program
void run(UI* ui);