#Model Module

def createComplexNumber(realPart, imagPart):
    '''
        Function that creates a complex number based on the real and the imaginary parts of the number
        input: realPart - integer, imagPart - integer
        output: the complex number in form of a list
    '''
    return [realPart, imagPart]

def getReal(complexNumber):
    '''
        Function that gets the real part of a complex number
        input: complexNumber - a complex number
        output: the real part of the number - integer
    '''
    return complexNumber[0]

def getImaginary(complexNumber):
    '''
        Function that gets the imaginary part of a complex number
        input: complexNumber: a complex number
        output: the imaginary part of the number
    '''
    return complexNumber[1]

def setReal(complexNumber, value):
    '''
        Function that sets to the real part of a complex number a value
        input: complex number - a complex number, value - integer
        output: -
    '''
    complexNumber[0] = value

def setImaginary(complexNumber, value):
    '''
        Function that sets to the imaginary part of a complex number a value
        input: complex number - a complex number, value - integer
        output: -
    '''
    complexNumber[1] = value

def modelStringRemoveString(stringInput, stringRemove):
    '''
        Function that removes a string from another string
        input: stringInput - string
               StringOutput - string
        output: leftover - string
    '''
    leftover = stringInput.replace(stringRemove, "")
    leftover = leftover.replace(" ", "")
    return leftover

import re

def checkForBadCharacters(complexString):
    '''
        Function that check if a string has other characters than 1234567890i+-
        input: complexString - string that may be a complex number
        output: True - if the string does not have other characters than 1234567890i+-
                False - if the string has other charecters than 1234567890i+-
    '''
    if re.findall("[^1234567890i+-]", complexString):
        return False
    if "i" not in complexString:
        return False
    return True

def checkStringIsComplex(complexString):
    '''
        Function that checks if a string is suitable to be a complex number
        input: complexString - string
        output: -, if the string is suitable to be a complex number
        raises: ValueError
                    if the string can not be a complex number "invalid complex number!"
    '''
    if complexString == "":
        raise Exception("Please insert complex number!")
    if checkForBadCharacters(complexString) == False:
        raise Exception("Invalid complex number!")
    
def checkForMinusInString(complexString):
    '''
        Function that checks if the string can be splited by a "+" or by a minus
        input: complexString - string
        output: splitByMinus - True if the string must be splited by a "-"
                               False if the string must be splited by a "+"
                firstMinus - True if the first element of the string is "-"
                             False if the first element of the string is not a "-"
    '''
    if "+" in complexString:
        splitByMinus = False
        firstMinus = False
        return splitByMinus, firstMinus
    if complexString[0] != "-" and "+" not in complexString:
        splitByMinus = True
        firstMinus = False
        return splitByMinus, firstMinus
    if complexString[0] == "-" and "+" not in complexString:
        splitByMinus = True
        firstMinus = True
        return splitByMinus, firstMinus

def complexStringSplit(complexString, sign):
    '''
        Function that splits sa complex number that is a string in two parts, real and imaginary
        input: complexString - string
               sign - string
        output: realPart - string
                imagPart - string
    '''
    parts = complexString.split(sign)
    for part in parts:
        if "i" in part:
            imagPart = part.replace("i", "")
        else:
            realPart = part
    return realPart, imagPart

def stringToComplexNumber(complexString):
    '''
        Function that transforms a complex number that is a string in two parts, real and imaginary
        input: complexString - string
        output: realPart - real part of the complex number
                imagPart - imaginary part of the complex number
    '''
    splitByMinus, firstMinus = checkForMinusInString(complexString)
    if splitByMinus == False:
        realPart, imagPart = complexStringSplit(complexString, "+")
        return realPart, imagPart
    if splitByMinus == True and firstMinus == True:
        complexString = complexString[1:]
        realPart, imagPart = complexStringSplit(complexString, "-")
        realPart = "-" + realPart[0:]
        imagPart = "-" + imagPart[0:]
        return realPart, imagPart
    if splitByMinus == True and firstMinus == False:
        realPart, imagPart = complexStringSplit(complexString, "-")
        imagPart = "-" + imagPart[0:]
        return realPart, imagPart

def modelStringToComplex(complexString):
    '''
        Function that puts in two parameters the real and the imaginary parts of a complex number that is a string
        input: complexString - string
        output: realPart - string
                imagPart - string
    '''
    realPart, imagPart = stringToComplexNumber(complexString)
    return realPart, imagPart

def checkStringEmpty(stringEmp):
    '''
        Function that checks if a string is empty
        input: stringEmp - a string
        output: True - if the list is empty
                False - if the string is not empty
    '''
    if stringEmp == "":
        return True
    else:
        return False

def modelComplexToString(complexList):
    '''
        Function that transform a complex number from the list in a string by the form a+bi
        input: complexList - a complex number
        output: complexNumber - a string
    '''
    if getImaginary(complexList) >= 0:
        complexNumber = str(getReal(complexList)) + "+" + str(getImaginary(complexList)) + "i"
    else:
        complexNumber = str(getReal(complexList)) + str(getImaginary(complexList)) + "i"
    return complexNumber

def modelCreateListRealNumber(l, position1, position2):
    '''
        Function that creates a list of real numbers between two positions from the list of complex numbers
        input: l - a list
               position1 - a number
               position2 - a number
        output: listReal - a lsit
    '''
    listReal = []
    for x in range(position1, position2 + 1):
        if getImaginary(l[x]) == 0:
            listReal.append(l[x])
    return listReal

def modelCreateListModuloEqual(l, value):
    '''
        Function that creates a list of complex numbers that have the modulo equal to a value
        input: l - a list
               value - a numeber
        output: listModuloEqual - a list
    '''
    listModuloEqual = []
    for x in l:
        modulo = modelModuloOfComplexNumber(x)
        if modulo == value:
            listModuloEqual.append(x)
    return(listModuloEqual)

def modelCreateListModuloGreater(l, value):
    '''
        Function that creates a list of complex numbers that have the modulo greater then a value
        input: l - a list
               value - a number
        output: listModuloGreater - a list
    '''
    listModuloGreater = []
    for x in l:
        modulo = modelModuloOfComplexNumber(x)
        if modulo > value:
            listModuloGreater.append(x)
    return listModuloGreater

def modelCreateListModuloLess(l, value):
    '''
        Function that creates a list of complex numbers that have the modulo less then a value
        input: l - a list
               value - a number
        output: listModuloLess - a list
    '''
    listModuloLess = []
    for x in l:
        modulo = modelModuloOfComplexNumber(x)
        if modulo < value:
            listModuloLess.append(x)
    return listModuloLess

import math

def modelModuloOfComplexNumber(complexNumber):
    '''
        Function that calculates the modulo of a complex number
        input: complexNumber - a complex number
        output: modulo - the modulo of a complex number
    '''
    modulo = getReal(complexNumber) ** 2 + getImaginary(complexNumber) ** 2
    modulo = math.sqrt(modulo)
    return modulo

def modelSumTwoComplexNumbers(complexNumber1, complexNumber2):
    '''
        Function that sums two complex numbers
        input: complexNumber1 - a complex number
               complexMNumber2 - a complex number
        output: result - a complex number
    '''
    resultRealPart = getReal(complexNumber1) + getReal(complexNumber2)
    resultImagPart = getImaginary(complexNumber1) + getImaginary(complexNumber2)
    result = createComplexNumber(resultRealPart, resultImagPart)
    return result

def modelSumComplexBetweenPositions(l, position1, position2):
    '''
        Function that sums all the numbers between two positions
        input: l - a list
               position1 - a number
               position2 - a number
        output: result - a complex number
    '''
    result = [0,0]
    for x in range(position1, position2):
        result = modelSumTwoComplexNumbers(result, l[x])
    return result

def modelProductTwoComplexNumbers(complexNumber1, complexNumber2):
    '''
        Function that multiplies two complex numbers
        input: complexNumber1 - a complex number
               complexNumber2 - a complex number
        output: result - a complex number
    '''
    resultRealPart = getReal(complexNumber1) * getReal(complexNumber2) - getImaginary(complexNumber1) * getImaginary(complexNumber2)
    resultImagPart = getReal(complexNumber1) * getImaginary(complexNumber2) + getImaginary(complexNumber1) * getReal(complexNumber2)
    result = createComplexNumber(resultRealPart, resultImagPart)
    return result

def modelProductComplexBetweenPositions(l, position1, position2):
    '''
        Functuion that multiplies the complex numbers between two positions in a list
        input: l - a list
               position1 - a number
               position2 - a number
        output: result - a complex number
    '''
    result = [getReal(l[position1]), getImaginary(l[position1])]
    for x in range(position1 + 1, position2):
        result = modelProductTwoComplexNumbers(result, l[x])
    return result
