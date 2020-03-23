#pragma once
#include <iostream>


template <class T > class
DynamicVector {
private:
	T* items;
	int size;
	int capacity;

	//Resize function
	void resize(int factor);
public:
	//Default constructor function
	explicit DynamicVector(int capacity = 10);


	//Copy constructor function
	DynamicVector(const DynamicVector& copyVector);


	//Destructor function
	~DynamicVector();


	//Function that adds an item in the vector
	void addItem(const T& item);


	//Function that deletes an item from the vector
	void deleteItem(const int position);


	//Function that updates an item from a position in the vector
	void updateItem(const int position, const T item);


	//Getter for size
	int getSize() const { return size; }


	//Getter for capacity
	int getCapacity() const { return capacity; }


	//Getter for an item given a position
	T getItem(const int position) const;
};

///////////////////////////////////////////////////////////////////////

template <class T>
DynamicVector<T>::DynamicVector(int capacity) {
	this->size = 0;
	this->capacity = capacity;
	this->items = new T[this->capacity];
}


template <class T>
DynamicVector<T>::DynamicVector(const DynamicVector& copyVector) {
	this->size = copyVector.getSize();
	this->capacity = copyVector.getCapacity();
	this->items = new T[this->capacity];
	for (int i = 0; i < this->size; i++) {
		this->items[i] = copyVector.getItem(i);
	}
}


template <class T>
DynamicVector<T>::~DynamicVector() {
	delete[] this->items;
}


template <class T>
void DynamicVector<T>::resize(int factor) {
	this->capacity *= factor;
	T* newItems = new T[this->capacity];
	for (int i = 0; i < this->size; i++) {
		newItems[i] = this->items[i];
	}
	delete[] this->items;
	this->items = newItems;
}


template <class T>
void DynamicVector<T>::addItem(const T& item) {
	if (this->size == this->capacity) {
		this->resize(2);
	}
	this->items[this->size] = item;
	this->size += 1;
}


template <class T>
void DynamicVector<T>::deleteItem(const int position) {
	if (position < 0 || position >= this->size) {
		return;
	}
	T* newItems = new T[this->capacity];
	for (int i = 0; i < this->size; i++) {
		if (i < position) {
			newItems[i] = this->items[i];
		}
		else {
			newItems[i] = this->items[i + 1];
		}
	}
	delete[] this->items;
	this->items = newItems;
	this->size -= 1;
}


template <class T>
void DynamicVector<T>::updateItem(const int position, const T item) {
	if (position < 0 || position >= this->size) {
		return;
	}
	this->items[position] = item;
}


template <class T>
T DynamicVector<T>::getItem(const int position) const {
	return this->items[position];
}