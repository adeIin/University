#Tests Module

from serviceModule import serviceAddComplexNumber, serviceInsertAt, serviceRemoveSimple, serviceRemoveTo, serviceReplaceWith
from modelModule import createComplexNumber, getReal, getImaginary, setReal, setImaginary
from validateModule import validateComplexNumber
from featureModule import featureAddComplexNumber, featureInsertAt, featureRemoveSimple, featureRemoveTo, featureReplaceWith

def testCreateComplexNumber():
    complexNumber = createComplexNumber(34, 87)
    assert getReal(complexNumber) == 34
    assert getImaginary(complexNumber) == 87
    setReal(complexNumber, 100)
    assert getReal(complexNumber) == 100
    setImaginary(complexNumber, -98)
    assert getImaginary(complexNumber) == -98

def testValidComplexNumber():
    complexNumber = createComplexNumber(34, 87)
    validateComplexNumber(complexNumber)
    complexNumber2 = createComplexNumber("as", "87.56")
    try:
        validateComplexNumber(complexNumber2)
        assert False
    except Exception as ex:
        assert str(ex) == "Invalid real part!\nInvalid imaginary part!\n"

def testAddComplexNumber():
    l = []
    complexNumber = createComplexNumber(34, 87)
    featureAddComplexNumber(l, complexNumber)
    assert len(l) == 1
    assert l == [complexNumber]

def testServiceAddComplexNumber():
    l = []
    serviceAddComplexNumber(l, 34, 87)
    assert len(l) == 1
    assert getReal(l[0]) == 34
    assert getImaginary(l[0]) == 87
    try:
        serviceAddComplexNumber(l, "34.56", "87as.56")
        assert False
    except Exception as ex:
        assert (str(ex) == "Invalid real part!\nInvalid imaginary part!\n")

def testInsertAt():
    l = [[0,0], [10,10], [20,20], [30,30], [40,40]]
    complexNumber = createComplexNumber(34, 87)
    position = 2
    featureInsertAt(l, complexNumber, position)
    assert len(l) == 6
    assert l[2] == complexNumber

def testServiceInsertAt():
    l = [[0,0], [10,10], [20,20], [30,30], [40,40]]
    serviceInsertAt(l, 34, 87, 2)
    assert len(l) == 6
    assert getReal(l[2]) == 34
    assert getImaginary(l[2]) == 87
    try:
        serviceInsertAt(l, "34.56", "87asd.56", 2)
        assert False
    except Exception as ex:
        assert (str(ex) == "Invalid real part!\nInvalid imaginary part!\n")

def testRemoveSimple():
    l = [[0,0], [10,10], [20,20], [30,30], [40,40]]
    featureRemoveSimple(l, 2)
    assert len(l) == 4
    assert l[2] == [30,30]

def testServiceRemoveSimple():
    l = [[0,0], [10,10], [20,20], [30,30], [40,40]]
    serviceRemoveSimple(l, 2)
    assert len(l) == 4
    assert getReal(l[2]) == 30
    assert getImaginary(l[2]) == 30
    try:
        serviceRemoveSimple(l, "2.5")
        assert False
    except Exception as ex:
        assert (str(ex) == "Invalid position!\n")

def testRemoveTo():
    l = [[0,0], [10,10], [20,20], [30,30], [40,40]]
    featureRemoveTo(l, 2, 4)
    assert len(l) == 2
    assert l[0] == [0,0]
    assert l[1] == [10,10]

def testServiceRemoveTo():
    l = [[0,0], [10,10], [20,20], [30,30], [40,40]]
    serviceRemoveTo(l, 2, 4)
    assert len(l) == 2
    assert getReal(l[0]) == 0
    assert getImaginary(l[0]) == 0
    assert getReal(l[1]) == 10
    assert getImaginary(l[1]) == 10   
    try:
        serviceRemoveTo(l, "2sX5", 34) 
        assert False
    except Exception as ex:
        assert (str(ex) == "Invalid position!\n")

def testReplaceWith():
    l = [[0,0], [10,10], [20,20], [30,30], [40,40]]
    featureReplaceWith(l, [10,10], [11,12])
    assert getReal(l[1]) == 11
    assert getImaginary(l[1]) == 12

def testServiceReplaceWith():
    l = [[0,0], [10,10], [20,20], [30,30], [40,40]]
    serviceReplaceWith(l, 10, 10, 11, 12)
    assert getReal(l[1]) == 11
    assert getImaginary(l[1]) == 12
    try:
        serviceReplaceWith(l, "12,2", "das", "d32", "e222")
        assert False
    except Exception as ex:
        assert str(ex) == "Invalid real part!\nInvalid imaginary part!\n"

def runAllTests():
    testCreateComplexNumber()
    testValidComplexNumber()
    testAddComplexNumber()
    testServiceAddComplexNumber()
    testInsertAt()
    testServiceInsertAt()
    testRemoveSimple()
    testServiceRemoveSimple()
    testRemoveTo()
    testServiceRemoveTo()
    testReplaceWith()
    testServiceReplaceWith()
    
