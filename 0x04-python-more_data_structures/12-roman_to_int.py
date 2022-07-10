#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        r_s = roman_string
        numero = 0
        for x in range(len(r_s)):
            if x > 0 and (rom[r_s[x]] > rom[r_s[x - 1]]):
                numero += rom[r_s[x]] - (2 * rom[roman_string[x - 1]])
            else:
                numero += rom[r_s[x]]
        return numero
    return (0)
