#Validate Module

from modelModule import getReal, getImaginary

def checkIsNumber(stringNumber):
    try:
        int(stringNumber)
        return True
    except ValueError:
        return False

def validateComplexNumber(complexNumber):
    '''
        Function that validates the real and the imaginary part of a complex number\
        input: complexNumber - a complex number
        output: - ; if the real and the imaginary parts are valid
        raises: Exception
                    if the real part is not an integer number "invalid real part!"
                    if the imaginary is not an integer number "invalid imaginary part!"
    
    errors = ""
    if type(getReal(complexNumber)) != int:
        errors = errors + "Invalid real part!\n"
    if type(getImaginary(complexNumber)) != int:
        errors = errors + "Invalid imaginary part!\n"
    if len(errors) > 0:
        raise Exception(errors)
    '''
    errors = ""
    if checkIsNumber(getReal(complexNumber)) == False:
        errors = errors + "Invalid real part!\n"
    if checkIsNumber(getImaginary(complexNumber)) == False:
        errors = errors + "Invalid imaginary part!\n"
    if len(errors) > 0:
        raise Exception(errors)

def validatePosition(position):
    '''
        Function that validates a position
        input: position - number
        output: - if the position is valid
        raises: Exception
                    if the position its not an natural number
    
    error = ""
    if type(position) != int:
        error = error + "Invalid position!\n"
    if len(error) > 0:
        raise Exception(error)
    '''
    if checkIsNumber(position) == False:
        raise Exception("Invalid position!\n")
    


