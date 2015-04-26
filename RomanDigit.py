__author__ = 'WangZhe'
# File: RomanDigit.py
# Description: This module can transform a Roman numerals to Arabic numerals
# Derive from: http://www.diveintopython3.net/regular-expressions.html
# 04/26/2015 at SJTU library

RomanDictionary = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'Z': 0}


def Rm2Ab(Rm):
    Rnummeral = [Rm[i] for i in range(len(Rm))]
    result = 0
    inver = ['Z' for i in range(len(Rnummeral))]
    j = 0
    for i in range(1, len(Rnummeral)):
        if RomanDictionary[Rnummeral[i]] > RomanDictionary[Rnummeral[i-1]] and Rnummeral[i-1] != 'Z':
            inver[j] = Rnummeral[i-1]
            inver[j+1] = Rnummeral[i]
            j += 2
            Rnummeral[i-1] = 'Z'
            Rnummeral[i] = 'Z'

    numInver = j//2
    for i in range(len(Rnummeral)):
        result += RomanDictionary[Rnummeral[i]]

    j = 0
    for i in range(numInver):
        result += RomanDictionary[inver[j+1]] - RomanDictionary[inver[j]]
        j += 2

    return result


print(Rm2Ab('MDCCCLXXXVIII'))
print(Rm2Ab('MCMXLVI'))
print(Rm2Ab('CI'))
print(Rm2Ab('DCCC'))
print(Rm2Ab('DCI'))