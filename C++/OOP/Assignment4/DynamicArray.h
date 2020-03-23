#pragma once


typedef void* TElem;
typedef void(*DestroyElemFunctionType)(void*);


typedef struct {
	TElem* elements;
	int length;
	int capacity;
	DestroyElemFunctionType DestroyElem;
} DynamicArray;


//Function that creates a dynamic array 
//pre:  capacity - int, maximum capacity of the dynamic array
//	    DestroyElem - DestroyElemFunctionType, fnction pointer that is used for deallocating the elements
//post: pointer to the created dynamic array
DynamicArray* createDynamicArray(int capacity, DestroyElemFunctionType DestroyElem);

//Function that destroys a dynamic array
//pre:  array = DynamicArray, the dynamic array that needs to be destroyed
//post: -
void destroyDynamicArray(DynamicArray* array);

//Function that adds an element in a dynamic array
//pre:  array - DynamicArray, the dynamic array
//      elem - TElem, the element that needs to be added
//post: -
void addDynamicArray(DynamicArray* array, TElem elem);

//Function that deletes an element from a dynamic array
//pre:  array - DynamicArray, the dynamic array
//		pos - int, the position of the element that needs to be deleted
//post: -
void deleteDynamicArray(DynamicArray* array, int pos);

//Function that gets the lenght of a dynamic array
//pre:  array - DynamicArray, the dynamic array
//post: the length of the array
int getLength(DynamicArray* array);

//Function that gets an element from a dynamic array
//pre:  array - DynamicArray, the dynamic array
//		pos - int, the position of the element
//post: the element
TElem getElemDynamicArray(DynamicArray* array, int pos);
