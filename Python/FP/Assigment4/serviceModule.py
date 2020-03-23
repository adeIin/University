#Service Module

from validateModule import validateComplexNumber, validatePosition
from modelModule import createComplexNumber
from featureModule import featureAddComplexNumber, featureInsertAt, featureRemoveSimple, featureRemoveTo, featureReplaceWith, featureList, featureListReal, featureListModuloEqual, featureListModuloGreater, featureListModuloLess, featureSumComplexNumbers, featureProductComplexNumbers, featureFilterReal, featureFilterModuloEqual, featureFilterModuloGreater, featureFilterModuloLess

def serviceAddComplexNumber(l, realPart, imagPart):
    '''
        Function that creates a complex number with the real part and the imaginary part,
        validates the real and the imaginary part,
        adds the complex number to the list
        input: l - a list
               realPart - integer
               imagPart - integer
        output: - if the parameters are valid
        raises: Exception
                    if the real part is invalid: "invalid real part!"
                    if the imaginary part is invalisd: "invalid imaginary part!"
    '''
    complexNumber = createComplexNumber(realPart, imagPart)
    validateComplexNumber(complexNumber)
    featureAddComplexNumber(l, complexNumber)

def serviceInsertAt(l, realPart, imagPart, position):
    '''
        Function that creates a complex number with the real part and the imaginary part,
        validates the real and the imaginary part,
        inserts the complex number at the given position in list
        input: l - a list
               realPart - integer
               imagPart - integer
               position - natural number
        output: - if the parameters are valid
        raises: Exception
                    if the real part is invalid: "invalid real part!"
                    if the imaginary part is invalid: "invalid imagonary part!"
    '''
    complexNumber = createComplexNumber(realPart, imagPart)
    validateComplexNumber(complexNumber)
    featureInsertAt(l, complexNumber, position)

def serviceRemoveSimple(l, position):
    '''
        Function that validates a position and remove the element from a position from a list
        input: l - a list, position - number
        output: - if the position is valid
        raises: Exception
                    if the position is invalid: "Invalid position!"
    '''
    validatePosition(position)
    featureRemoveSimple(l, position)

def serviceRemoveTo(l, position1, position2):
    '''
        Function that validates the position1 and the position2 and 
        remove all the elements between the two positions
        input: l - a list, position1 - number, position2 - number
        output: - if the parameters are valid
        raises: Exception
                    if the parameters are invalid: "Invalid positions!"
    '''
    validatePosition(position1)
    validatePosition(position2)
    position1 = int(position1)
    position2 = int(position2)
    featureRemoveTo(l, position1, position2)
    
def serviceReplaceWith(l, realPartOld, imagPartOld, realPartNew, imagPartNew):
    '''
        Function that creates two complex numbers, validates them and replaces the first one with the second one
        input: l - a list
               realPartOld - the real part of the first complex number
               imagPartOld - the imaginary part of the first complex number
               realPartNew - the real part of the second complex number
               imagPartNew - the imaginary part of the second complex number
        oyutput: -
        raises: Exception
                    if the parameters of the complex numbers are invalid
    '''
    complexNumberOld = createComplexNumber(realPartOld, imagPartOld)
    complexNumberNew = createComplexNumber(realPartNew, imagPartNew)
    validateComplexNumber(complexNumberOld)
    validateComplexNumber(complexNumberNew)
    featureReplaceWith(l, complexNumberOld, complexNumberNew)

def servicePrintList(l):
    '''
        Function that prints a list of complex numbers in the form a+bi
        input: l - a list of complex numbers
        output: -
    '''
    featureList(l)

def servicePrintListReal(l, position1, position2):
    '''
        Function that prints a list of real numbers between two positions from the list of complex numbers
        input: l - a list
               position1 - a number
               position2 - a number
        output: -
    '''
    featureListReal(l, position1, position2)

def servicePrintListModuloEqual(l, value):
    '''
        Function that prints the complex numbers from the list that have the modulo equal to a value
        input: l - a list
               value - a number
        output: -
    '''
    featureListModuloEqual(l,value)

def servicePrintListModuloGreater(l, value):
    '''
        Function that prints the complex numbers from the list that have the modulo greater then a value
        input: l - a list
               value - a number
        output: -
    '''
    featureListModuloGreater(l, value)

def servicePrintListModuloLess(l, value):
    '''
        Function that prints the complex numbers from the list that have the modulo less then a value
        input: l - a list
               value - a number
        output: -
    '''
    featureListModuloLess(l, value)

def serviceSumComplexNumbers(l, position1, position2):
    '''
        Function that prints the result of the sum of the complex numbers between position1 and position2 in the list l
        input: l - a list
               position1 - a number
               position2 - a number
        output: -
    '''
    featureSumComplexNumbers(l, position1, position2)

def serviceProductComplexNumbers(l, position1, position2):
    '''
        Function that prints the result of the product of the complex numbers between two positions in a list
        input: l - a list
               position1 - a number
               position2 - a number
        outpu: -
    '''
    featureProductComplexNumbers(l, position1, position2)

def serviceFilterReal(l):
    '''
        Function that filters the real numbers from a list
        input: l - a list
        output: -
    '''
    featureFilterReal(l)

def serviceFilterModuloEqual(l, value):
    '''
        Function that filters the complex numbers from a list that have the modulo equal to a value
        input: l - a list
               value - an integer
        output: -
    '''
    featureFilterModuloEqual(l, value)

def serviceFilterModuloGreater(l, value):
    '''
        Function that filters the complex numbers from a list that have the modulo greater than a value
        input: l - a list
               value - an integer
        output: -
    '''
    featureFilterModuloGreater(l, value)

def serviceFilterModuloLess(l, value):
    '''
        Function that filters the complex numbers from a list that have the modulo less than a value
        input: l - a list
               value - an integer
        output: -
    '''
    featureFilterModuloLess(l, value)