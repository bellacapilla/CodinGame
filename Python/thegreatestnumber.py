import sys
import math

n = int(raw_input())
input = raw_input()

def create_newNumber_object(dataInput, n):
    numberObject = newNumber()
    
    numberObject.stringSeq = ''.join(dataInput)
    numberObject.hasMinus = verifyMinus(dataInput)
    numberObject.hasPoint = verifyPoint(dataInput)
    numberObject.valuesList = getValuesInt(dataInput)
    numberObject.sortedValuesList = sorted(numberObject.valuesList)
    numberObject.desSortedValuesList = sorted(numberObject.valuesList, reverse=True)
    numberObject.maxVal = max(numberObject.valuesList)
    numberObject.minVal = min(numberObject.valuesList)
    numberObject.length = n
    numberObject.hasZeros = verifyZeros(dataInput)
    
    return numberObject

def verifyZeros(stringInput):
    if stringInput.find('0') != -1:
        return True
    else:
        return False    

def sortNewNumber(myNumObject):
    
    if myNumObject.length <= 0:
        return None

    else:
    
        sortedVals = myNumObject.sortedValuesList
        desSortedVals = myNumObject.desSortedValuesList
        
        newSortedString = []
        
        if myNumObject.hasMinus == True:
            newSortedString.append(chr(45))
            newSortedString.append(myNumObject.minVal)
            
            if myNumObject.hasPoint == True:
                newSortedString.append(chr(46)) 
                newSortedString.append(''.join(map(str, sortedVals[1:])))
                
            else:
                newSortedString.append(''.join(map(str, sortedVals[1:])))
                
        else:
            if myNumObject.hasPoint == True:
                newSortedString.append(''.join(map(str, desSortedVals[:myNumObject.length-2])))
                newSortedString.append(chr(46))
                newSortedString.append(desSortedVals[myNumObject.length-2])
                
            else:
                newSortedString.append(''.join(map(str, desSortedVals[:])))
                
        finalNum = (''.join(map(str, newSortedString))).rstrip('0').rstrip('.')
        
        if finalNum[0] == '-' and len(finalNum)<=2:
            return finalNum.lstrip('-')
            
        else:
            return finalNum
        
def verifyMinus(stringInput):
    if stringInput.find('-') != -1:
        return True
    else:
        return False
    
def verifyPoint(stringInput):
    if stringInput.find('.') != -1:
        return True
    else:
        return False
    
def getValuesInt(stringInput):
    newStringOfValues = []
    
    for i in stringInput:
        if ord(i) >= 48 and ord(i) <= 57:
            newStringOfValues.append(int(i))
        else:
            continue
        
    return newStringOfValues

class newNumber:
    stringSeq = ""
    hasMinus = None
    hasPoint = None
    valuesList = []
    sortedValuesList = []
    desSortedValuesList = []
    maxVal = None
    minVal = None
    length = 0
    hasZeros = None

dataForSorting = create_newNumber_object(input, n)
finalNumCalc = sortNewNumber(dataForSorting)

print(finalNumCalc)
