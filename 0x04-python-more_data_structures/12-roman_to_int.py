#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ini_result = 0
    ini_pre = 0
    for i in reversed(roman_string):
        value = roman_dict[i]
        if value < ini_pre:
            ini_result -= value
        else:
            ini_result += value
        ini_pre = value
    return ini_result
