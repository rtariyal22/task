#!/usr/bin/python


def printNumbers():
    '''
    This function prints natural numbers from 1 to 100.
    But for multiples of three it prints "Three" instead of the number and for the multiples of five prints "Five".
    For numbers that are multiples of both three and five it prints "ThreeFive". 
    Arguments: None
    Return: None
    '''
    # Iterating each number from 1 to 100.
    for eachNumber in range(1, 101):
        # Initializing text to be printed as empty string before each iteration.
        # textToPrint changes if eachNumber is either divisible by 3, 5 or both.
        textToPrint = ''

        # Checking if number is divisible by 3. 
        if eachNumber % 3 == 0:
            textToPrint = 'Three'
        
        # Checking if number is divisible by 5. 
        if eachNumber % 5 == 0:
            # if number is also divisible by 3 then textToPrint will be appended by Three else ''
            textToPrint += 'Five'
        
        # This condition is satisfied only when number is eithier divisible by 3,5 or both.
        if textToPrint:
            print(textToPrint)
        else:
            print(eachNumber)


if __name__ == '__main__':
    printNumbers()