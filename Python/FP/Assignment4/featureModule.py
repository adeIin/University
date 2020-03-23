#Feature Module

from modelModule import getReal, getImaginary, setReal, setImaginary, modelComplexToString, checkStringEmpty, modelCreateListRealNumber, modelCreateListModuloEqual, modelCreateListModuloGreater, modelCreateListModuloLess, modelSumComplexBetweenPositions, modelProductComplexBetweenPositions, modelModuloOfComplexNumber

def featureAddComplexNumber(l, complexNumber):
    '''
        Function that adds a complex number to a list
        input: l - a list, complexNumber - a complex number
        output: -
    '''
    l.append(complexNumber)

def featureInsertAt(l, complexNumber, position):
    '''
        Function that inserts a complex number at a given position
        input: l - a list, complexNumber - a complex number, position - natural number
        output: -
    '''
    l.insert(position, complexNumber)

def featureRemoveSimple(l, position):
    '''
        Function that removes a complex number from a position
        input: l - a list, position - natural number
        output: -
    '''
    del l[position:position + 1]

def featureRemoveTo(l, position1, position2):
    '''
        Function that removes from the list all elements between the position1 and the position2
        input: l - a list, position1 - number, position2 - number
        output: -
    '''
    del l[position1:position2 + 1]

def featureReplaceWith(l, complexNumberOld, complexNumberNew):
    '''
        Function that replaces an old complex number from a list with a new one
        input: l - list, complexNumberOld - a complex number, complexNumberNew - a complex number
        output: -
    '''
    for complexNumber in l:
        if getReal(complexNumber) == getReal(complexNumberOld) and getImaginary(complexNumber) == getImaginary(complexNumberOld):
            setReal(complexNumber, getReal(complexNumberNew))
            setImaginary(complexNumber, getImaginary(complexNumberNew))

def featureList(l):
    '''
        Function that prints a list of complex numbers in the form of a+bi
        input: l - a list
        output: -
    '''
    printString = ""
    for x in l:
        complexNumber = modelComplexToString(x)
        if x == l[len(l) - 1]:
            printString = printString + complexNumber + ". "
        else:
            printString = printString + complexNumber + ", "
    if checkStringEmpty(printString) == True:
        printString = "List is empty!"
    print(printString)

def featureListReal(l, position1, position2):
    '''
        Function that prints the list of real numbers from two positions in the list of complex numbers
        input: l - a list
               position1 - a number
               position2 - a number
        outupt: -
    '''
    listReal = modelCreateListRealNumber(l, position1, position2)
    featureList(listReal)

def featureListModuloEqual(l, value):
    '''
        Function that prints the complex numbers from the list that have the modulo equal to a value
        input: l - a list
               value - a numeber
        output: -
    '''
    listModuloEqual = modelCreateListModuloEqual(l, value)
    featureList(listModuloEqual)

def featureListModuloGreater(l, value):
    '''
        Function that prints the complex numbers from the list that have the modulo greater then a value
        input: l - a list
               Value - a number
        output: -
    '''
    listModuloGreater = modelCreateListModuloGreater(l, value)
    featureList(listModuloGreater)

def featureListModuloLess(l, value):
    '''
        Function that prints the complex numbers from the list that have the modulo less then a value
        input: l - a list
               Value - a number
        output: -
    '''
    listModuloLess = modelCreateListModuloLess(l, value)
    featureList(listModuloLess)

def featureSumComplexNumbers(l, position1, position2):
    '''
        Function that sums all the complex numbers between the two positions and prints the result
        input: l - a list
               position1 - a number
               position2 - a number
        output: -
    '''
    result = modelSumComplexBetweenPositions(l, position1, position2)
    result = modelComplexToString(result)
    print(result)

def featureProductComplexNumbers(l, position1, position2):
    '''
        Function that multiplies all the complex numbers between the two positions and prints the result
        input: l - a list
               position1 - a number
               position2 - a number
        output: - 
    '''
    result = modelProductComplexBetweenPositions(l, position1, position2)
    result = modelComplexToString(result)
    print(result)

def featureFilterReal(l):
    '''
        Function that filters the real numbers from a list
        input: l - a list
        output: -
    '''
    for x in range(len(l) - 1, -1, -1):
        if getImaginary(l[x]) != 0:
            featureRemoveSimple(l, x)

def featureFilterModuloEqual(l, value):
    '''
        Function that filters the complex numbers from a list that have the modulo equal to a value
        input: l - a list
               value - an integer
        output: -
    '''
    for x in range(len(l) - 1, -1, -1):
        if modelModuloOfComplexNumber(l[x]) == value:
            featureRemoveSimple(l, x)

def featureFilterModuloGreater(l, value):
    '''
        Function that filters the complex numbers from a list that have the modulo greater than a value
        input: l - a list
               value - an integer
        output: -
    '''
    for x in range(len(l) - 1, -1, -1):
        if modelModuloOfComplexNumber(l[x]) > value:
            featureRemoveSimple(l, x)

def featureFilterModuloLess(l, value):
    '''
        Function that filters the complex numbers from a list that have the modulo less than a value
        input: l - a list
               value - an integer
        output: -
    '''
    for x in range(len(l) - 1, -1, -1):
        if modelModuloOfComplexNumber(l[x]) < value:
            featureRemoveSimple(l, x)


