#!/usr/bin/python python3
#Jesse Krizenesky

'''"Write a program that prints the numbers from 1 to 100.
    But for multiples of three print “Fizz” instead of the number 
    and for the multiples of five print “Buzz”. 
    For numbers which are multiples of both three and five print “FizzBuzz”
'''

sFizz = "Fizz"
sBuzz = "Buzz"
iNum = 1

while (iNum <= 100):

    if iNum % 3 == 0 and iNum % 5 == 0:
        print("%s%s" % (sFizz,sBuzz) )
    elif iNum % 3 == 0:
        print(sFizz)
    elif iNum % 5 == 0:
        print(sBuzz)
    else:
        print(iNum)

    iNum += 1

exit(0)
