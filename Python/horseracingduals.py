import sys
import math

# Creates new empty list for input values
newList = []
n = int(raw_input())
for i in xrange(n):
    pi = int(raw_input())
    newList.append(pi) # Adds values into the list

# Function for list evaluation
def getSmallerInterval(inputList):
    tempVal = 0
    idx = 0
    sortedList = sorted(newList, reverse=True) # Sorst the list and reverses it for non-negative results
    
    for i in sortedList:
        # Checks if there are equal horses' strength
        # If there are two horses with the same strength, it returns immediately '0', the smallest possible value
        if sortedList[idx] == sortedList[idx+1]:
            return 0
        
        # If the strength is not equal, then compares the substraction with the tempVal
        # If the substraction resulting value 'newVal' is smaller than the 'tempVal', then the value is substituted for the new one
        # If the newVal is greater, than the smallest value is kept
        else:
            newVal = sortedList[idx] - sortedList[idx+1]
            
            if tempVal == 0:
                tempVal = newVal
                
            elif tempVal > newVal:
                tempVal = newVal
                
            else:
                idx += 1
                
    return tempVal
                
resultVal = getSmallerInterval(newList)

print resultVal
