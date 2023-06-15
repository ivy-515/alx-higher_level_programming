#!/usr/bin/python3

def roman_to_int(roman_string):
    dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    num = 0
    roman = roman_string
    if type(roman) is not str or len(roman) is 0:
        return 0
    for i in range(len(roman)):
        if i < len(roman) - 1 and dic[roman[i]] < dic[roman[i + 1]]:
            num -= dic[roman[i]]
        else:
            num += dic[roman[i]]
    return (num)
