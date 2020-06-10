#!/usr/bin/python python3

#print("hello world")


import random


aArray1 = []
iRotation = 0



def PopulateArray():
    aArray1 = []
    iCount = 0
    iRange = random.randint(0, 10)
#    iRange = random.randint(4, 4)

    while iCount <= iRange:
        aArray1.append(random.randint(-1000, 1000) )
        iCount += 1

    return aArray1


def RotateElements(A, K):
    iCount = 0
    iTemp = 0
    aArray1 = A
    aArray2 = []
    iRotation = int(K)
    iArrayLength = 0
    iFinalArray = []


    iArrayLength = len(aArray1)


    if int(iArrayLength) == 0:
 #       print("Array is empty. Return original array.")
        return A


    if iRotation >= iArrayLength:
        while iRotation >= iArrayLength:
            iRotation = iRotation - iArrayLength

#    print("New rotation to perform is: %d" % iRotation)
#    print("Array length is: %d" % iArrayLength)

    #if our array length == our rotation
    #the roation cancels itself out, we can jsut return the array
    #    if you rotate the alphabet 26 times, it's jsut the alphabet
    #if our rotation is longer than our actual array
    #the rotation - array length == full rotation
    if int(iArrayLength) == 1:
#        print("Array has only one element, nothing to rotate. Return original array")
        return A
    elif int(iArrayLength) == int(iRotation):
#        print("Length && Rot are the same. Return original array.")
        return A
    elif iArrayLength < iRotation:
        iRotation = (iRotation - iArrayLength)



    #grab last element:value of the array
    #append it as the First value in a new array
    #pop the last value in the first array
    #iterate until rot complete

    while iCount < iRotation:
        iTemp = aArray1[-1:]
#        print("iTemp is: %s" % iTemp)
        aArray2.insert(0, iTemp[0])
        aArray1.pop()
        iCount += 1


    for e in aArray2:
        iFinalArray.append(e)

    for e in aArray1:
        iFinalArray.append(e)


    return iFinalArray




if __name__ == '__main__':

#    aArray1 = []
    aArray2 = []
    iRotation = input("Enter number of array rotations to perform: ")
    aArray1 = PopulateArray()
    print("Number of rotations: " + iRotation )
    print("Array before rotation: " + str(aArray1) )
    aArray2 = RotateElements(aArray1, iRotation)
    print(aArray2)
