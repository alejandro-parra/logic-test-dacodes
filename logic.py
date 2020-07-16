#Alejandro Parra

import sys

numLines = input("Please type number of test cases: ")
caseList = []

for i in range(int(numLines)):
    caseList.append(input("Please type coordinate #%d in the form 'X Y': "%(i+1)))


print("---------Output---------")
#Cases:
#rows>cols, cols even, is up
#rows>cols cols odd, down
#rows<=cols rows even, left
#rows<=cols rows odd, right

for i in range(int(numLines)):
    casePair = caseList[i].split()
    rows = int(casePair[0])
    columns = int(casePair[1])

    if rows>columns and (columns % 2 == 0):
        print("U")
    elif rows>columns and (columns % 2 == 1):
        print("D")
    elif rows<=columns and (columns % 2 == 0):
        print("L")
    elif rows<=columns and (columns % 2 == 1):
        print("R")








