#U.I. Module

from serviceModule import serviceAddComplexNumber, serviceInsertAt, serviceRemoveSimple, serviceRemoveTo, serviceReplaceWith, servicePrintList, servicePrintListReal, servicePrintListModuloEqual, servicePrintListModuloGreater, servicePrintListModuloLess, serviceSumComplexNumbers, serviceProductComplexNumbers, serviceFilterReal, serviceFilterModuloEqual, serviceFilterModuloGreater, serviceFilterModuloLess
from modelModule import checkStringIsComplex, modelStringRemoveString, modelStringToComplex, checkStringEmpty

def uiHelp():
    print("     1. To add a number to the list type:")
    print("         -'add <number>'; ")
    print("         -'insert <number> at <position>'; ")
    print("     2. To modify elements from the list type:")
    print("         -'remove <position>'; ")
    print("         -'remove <start position> to <end position>'; ")
    print("         -'replace <old number> with <new number>'; ")
    print("     3. To write numbers having different properties type: ")
    print("         -'list'; ")
    print("         -'list real <start position> to <end position>'; ")
    print("         -'list modulo [< | = | >] <number>'; ")
    print("     4. To obtain different characteristics of sub-lists type: ")
    print("         -'sum <start position> to <end position>'; ")
    print("         -'product <start position> to <end position>'; ")
    print("     5. To filter the list type: ")
    print("         -'filter real'; ")
    print("         -'filter modulo [ < | = | > ] <number>'; ")
    print("     6. To undo the last operation that modified program data type: ")
    print("         -'undo';")
    print("     7. To exit the app type: ")
    print("         -'exit'.")

def uiPrint(l):
    print(l)

def uiAdd(l, command, listHistory):
    complexString = modelStringRemoveString(command, "add")
    try:
        checkStringIsComplex(complexString)
    except Exception as ex:
        print(ex)
        return
    realPart, imagPart = modelStringToComplex(complexString)
    try:
        realPart = int(realPart)
        imagPart = int(imagPart)
    except ValueError:
        print("Invalid parts of complex number!")
        return
    serviceAddComplexNumber(l, realPart, imagPart)
    listHistory.append(copy.deepcopy(l))

def uiInsertAt(l, command, listHistory):
    commandParts = modelStringRemoveString(command, "insert")
    if checkStringEmpty(commandParts):
        print("Insert command is empty!")
        return
    parts = commandParts.split("at")
    for part in parts:
        if "i" in part:
            complexString = part
        else:
            position = part
    try:
        checkStringIsComplex(complexString)
    except Exception as ex:
        print(ex)
        return
    try:
        position = int(position)
    except ValueError:
        print("Invalid position")
        return
    realPart, imagPart = modelStringToComplex(complexString)
    try:
        realPart = int(realPart)
        imagPart = int(imagPart)
    except ValueError:
        print("Invalid parts of complex number!")
        return
    serviceInsertAt(l, realPart, imagPart, position)
    listHistory.append(copy.deepcopy(l))

def checkRemove(l, command, listHistory):
    if "to" in command:
        uiRemoveTo(l, command, listHistory)
    else:
        uiRemoveSimple(l, command, listHistory)

def uiRemoveSimple(l, command, listHistory):
    position = modelStringRemoveString(command, "remove")
    try:
        position = int(position)
    except ValueError:
        print("Invalid Position!")
        return
    serviceRemoveSimple(l, position)
    listHistory.append(copy.deepcopy(l))

def uiRemoveTo(l, command, listHistory):
    leftover = modelStringRemoveString(command, "remove")
    parts = leftover.split("to")
    position1 = parts[0]
    position2 = parts[1]
    if checkStringEmpty(position1) and checkStringEmpty(position2):
        print("Start positon empty!\nEnd position empty!")
        return
    if checkStringEmpty(position1):
        print("Start position empty!")
        return
    if checkStringEmpty(position2):
        print("End position empty!")
        return
    try:
        serviceRemoveTo(l, position1, position2)
    except Exception as ex:
        print(str(ex))
        return
    listHistory.append(copy.deepcopy(l))

def uiReplaceWith(l, command, listHistory):
    leftover = modelStringRemoveString(command, "replace")
    if "with" in leftover:
        parts = leftover.split("with")
    else:
        print("No 'with' in 'replace' command!")
        return
    try:
        checkStringIsComplex(parts[0])
    except Exception as ex:
        print(ex)
        return
    try:
        checkStringIsComplex(parts[1])
    except Exception as ex:
        print(ex)
        return
    realPartOld, imagPartOld = modelStringToComplex(parts[0])
    realPartNew, imagPartNew = modelStringToComplex(parts[1])
    try:
        realPartOld = int(realPartOld)
        imagPartOld = int(imagPartOld)
        realPartNew = int(realPartNew)
        imagPartNew = int(imagPartNew)
        serviceReplaceWith(l, realPartOld, imagPartOld, realPartNew, imagPartNew)
    except Exception as ex:
        print(ex)
        return
    listHistory.append(copy.deepcopy(l))

def uiListSimple(l, command):
    if command == "list":
        servicePrintList(l)
    else:
        print("Invalid 'list' command!")
        return

def uiListReal(l, command):
    leftover = modelStringRemoveString(command, "list")
    leftover = modelStringRemoveString(leftover, "real")
    if leftover == "":
        print("'list real' command is empty!")
        return
    if "to" not in leftover:
        print("No 'to' in command 'list real'")
        return
    parts = leftover.split("to")
    # print(parts[0])
    try:
        position1 = int(parts[0])
        position2 = int(parts[1])
    except ValueError:
        print("Invalid positions!")
        return
    servicePrintListReal(l, position1, position2)

def uiListModuloEqual(l, command):
    leftover = modelStringRemoveString(command, "list")
    leftover = modelStringRemoveString(leftover, "modulo")
    leftover = modelStringRemoveString(leftover, "=")
    try:
        value = int(leftover)
    except ValueError:
        print("Invalid 'list modulo =' command!")
        return
    servicePrintListModuloEqual(l, value)

def uiListModuloGreater(l, command):
    leftover = modelStringRemoveString(command, "list")
    leftover = modelStringRemoveString(leftover, "modulo")
    leftover = modelStringRemoveString(leftover, ">")
    try:
        value = int(leftover)
    except ValueError:
        print("Invalid 'list modulo >' command!")
        return
    servicePrintListModuloGreater(l, value)

def uiListModuloLess(l, command):
    leftover = modelStringRemoveString(command, "list")
    leftover = modelStringRemoveString(leftover, "modulo")
    leftover = modelStringRemoveString(leftover, "<")
    try:
        value = int(leftover)
    except ValueError:
        print("Invalid 'list modulo <' command!")
        return
    servicePrintListModuloLess(l, value)

def checkListModulo(l, command):
    if "=" in command:
        uiListModuloEqual(l, command)
    elif ">" in command:
        uiListModuloGreater(l, command)
    elif "<" in command:
        uiListModuloLess(l, command)
    else:
        print("Invalid 'list modulo' command!")
        return

def checkListCommand(l, command):
    if "real" in command:
        uiListReal(l, command)
    elif "modulo" in command:
        checkListModulo(l, command)
    else:
        uiListSimple(l, command)

def uiSumComplexNumbers(l, command):
    if "to" not in command:
        print("No 'to' in 'sum' command!")
        return
    leftover = modelStringRemoveString(command, "sum")
    parts = leftover.split('to')
    try:
        position1 = int(parts[0])
        position2 = int(parts[1])
    except ValueError:
        print("Invalid positions!")
        return
    serviceSumComplexNumbers(l, position1, position2)

def uiProductComplexNumbers(l, command):
    if "to" not in command:
        print("no 'to' in 'product' command!")
        return
    leftover = modelStringRemoveString(command, "product")
    parts = leftover.split('to')
    try:
        position1 = int(parts[0])
        position2 = int(parts[1])
    except ValueError:
        print("Invalid positions!")
        return
    serviceProductComplexNumbers(l, position1, position2)

def uiFilterReal(l, command, listHistory):
    leftover = modelStringRemoveString(command, "filter")
    leftover = modelStringRemoveString(leftover, "real")
    if leftover != "":
        print("Invalid 'filter real' command!")
        return
    serviceFilterReal(l)
    listHistory.append(copy.deepcopy(l))

def uiFilterModuloEqual(l, command, listHistory):
    leftover = modelStringRemoveString(command, "filter")
    leftover = modelStringRemoveString(leftover, "modulo")
    leftover = modelStringRemoveString(leftover, "=")
    try:
        value = int(leftover)
    except ValueError:
        print("Invalid 'filter modulo =' command!")
        return
    serviceFilterModuloEqual(l, value)
    listHistory.append(copy.deepcopy(l))

def uiFilterModuloGreater(l, command, listHistory):
    leftover = modelStringRemoveString(command, "filter")
    leftover = modelStringRemoveString(leftover, "modulo")
    leftover = modelStringRemoveString(leftover, ">")
    try:
        value = int(leftover)
    except ValueError:
        print("Invalid 'filter modulo >' command!")
        return
    serviceFilterModuloGreater(l, value)
    listHistory.append(copy.deepcopy(l))

def uiFilterModuloLess(l, command, listHistory):
    leftover = modelStringRemoveString(command, "filter")
    leftover = modelStringRemoveString(leftover, "modulo")
    leftover = modelStringRemoveString(leftover, "<")
    try:
        value = int(leftover)
    except ValueError:
        print("Invalid 'filter modulo <' command!")
        return
    serviceFilterModuloLess(l, value)
    listHistory.append(copy.deepcopy(l))

def checkFilterModulo(l, command, listHistory):
    if "=" in command:
        uiFilterModuloEqual(l, command, listHistory)
    elif ">" in command:
        uiFilterModuloGreater(l, command, listHistory)
    elif "<" in command:
        uiFilterModuloLess(l, command, listHistory)
    else:
        print("Invalid 'filter modulo' command!")
        return
    
def checkFilterCommand(l, command, listHistory):
    if "real" in command:
        uiFilterReal(l, command, listHistory)
    if "modulo" in command:
        checkFilterModulo(l, command, listHistory)
    
import copy

def undoFeature(l, listHistory):
    if len(listHistory) == 1:
        return l
    del listHistory[-1]
    l = copy.deepcopy(listHistory[-1])
    return l

def checkCommand(l, command, listHistory):
    if "add" in command:
        uiAdd(l, command, listHistory)
    elif "insert" in command:
        uiInsertAt(l, command, listHistory)
    elif "remove" in command:
        checkRemove(l, command, listHistory)
    elif "replace" in command:
        uiReplaceWith(l, command, listHistory)
    elif "list" in command:
        checkListCommand(l, command)
    elif "sum" in command:
        uiSumComplexNumbers(l, command)
    elif "product" in command:
        uiProductComplexNumbers(l, command)
    elif "filter" in command:
        checkFilterCommand(l, command, listHistory)
    else:
        print("Invalid command!")

def run():
    complexNumberList = [[10,0], [10,10], [20,20], [30,30], [40,40], [-50,-50], [-60,60], [70,-70], [80,10], [90,10]]
    listHistory = [[[10,0], [10,10], [20,20], [30,30], [40,40], [-50,-50], [-60,60], [70,-70], [80,10], [90,10]]]

    while True:
        print("")
        print("Please type a command. Type 'help' for command list!")
        command = input(">>>")
        if command == "exit":
            return
        elif command == "help":
            uiHelp()
        elif command == "print":
            uiPrint(listHistory)
        elif command == "undo":
            complexNumberList = undoFeature(complexNumberList, listHistory)
        else:
            checkCommand(complexNumberList, command, listHistory)
