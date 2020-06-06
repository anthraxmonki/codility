#!"C:\Program Files (x86)\Python38-32"

import os
import sys


def IntToBin(number):
    binInt = bin(number).replace("0b", "")
    return binInt



def BinaryGapCounter(iBinaryInt):
    sBinaryInt = str(iBinaryInt)
    lOfConsecutiveZeroes = []
    iCounter = 0
    iMax = 0
    iIndexesToPop = 0
    iLength = 0  
    iLength = len(iBinaryInt)


    lNum = [int(n) for n in str(iBinaryInt)]
    for e in reversed(lNum):
        if int(e) == 0:
           lNum.pop()
        else:
            break

    lOfInts = [str(s) for s in lNum]
    iBinaryInt = int("".join(lOfInts))
    sBinaryInt = str(iBinaryInt)


    for number in sBinaryInt:
        if number == str(0):
            iCounter += 1
            lOfConsecutiveZeroes.append(iCounter)
        elif number == str(1):
            iCounter = 0
    try: 
        if ( max(lOfConsecutiveZeroes) > 0) :
            iMax = max(lOfConsecutiveZeroes)
            print(iMax)
        else:
            iMax = 0
    except:
        iMax = 0
        pass

    return iMax




if __name__ == '__main__':
    sUserInput = input("Enter a number: ")
    iUserInput = int(sUserInput)
    iConversion = IntToBin(iUserInput)
    print("%s converted to Binary is: %s"  % (iUserInput, iConversion) )

    iConsecutiveZeroes = BinaryGapCounter(iConversion)
    print("Max number of consecutive Zeroes with a 1 on each end, is: %s" % (str(iConsecutiveZeroes)) )
