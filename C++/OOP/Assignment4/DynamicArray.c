#include "DynamicArray.h"
#include <stdlib.h>
#include <stdio.h>


DynamicArray* createDynamicArray(int capacity, DestroyElemFunctionType DestroyElem) {
	DynamicArray* array = (DynamicArray*)malloc(sizeof(DynamicArray));
	if (array == NULL) {
		return NULL;
	}
	array->capacity = capacity;
	array->length = 0;
	array->DestroyElem = DestroyElem;
	array->elements = NULL;
	array->elements = (TElem*)malloc(sizeof(TElem) * capacity);
	if (array->elements == NULL) {
		return NULL;
	}
	return array;
}


void destroyDynamicArray(DynamicArray* array) {
	if (array == NULL) {
		return;
	}
	for (int i = 0; i < array->length; i++) {
		array->DestroyElem(array->elements[i]);
	}
	free(array->elements);
	free(array);
}

void resizeDynamicArray(DynamicArray* array) {
	if (array == NULL) {
		return;
	}
	if (array->capacity == 0) {
		array->capacity = 1;
	}
	array->capacity *= 2;
	TElem* newElements = (TElem*)malloc(array->capacity * sizeof(TElem));
	if (newElements == NULL) {
		return;
	}
	for (int i = 0; i < array->length; i++) {
		newElements[i] = array->elements[i];
	}
	free(array->elements);
	array->elements = newElements;
}

void addDynamicArray(DynamicArray* array, TElem elem) {
	if (array == NULL) {
		return;
	}
	if (array->length == array->capacity) {
		resizeDynamicArray(array);
	}
	array->elements[array->length] = elem;
	array->length += 1;
}


void deleteDynamicArray(DynamicArray* array, int pos) {
	if (array == NULL) {
		return;
	}
	if (array->elements == NULL) {
		return;
	}
	if (pos < 0 || pos >= array->length) {
		return;
	}
	array->DestroyElem(array->elements[pos]);
	for (int i = pos; i < array->length - 1; i++) {
		array->elements[i] = array->elements[i + 1];
	}
	array->length -= 1;
}


int getLength(DynamicArray* array) {
	return array->length;
}


TElem getElemDynamicArray(DynamicArray* array, int pos) {
	if (array == NULL) {
		return NULL;
	}
	if (pos < 0 || pos >= array->length) {
		return NULL;
	}
	return array->elements[pos];
}
