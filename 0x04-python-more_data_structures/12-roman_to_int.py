#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5,
                  "I": 1}
    n = []
    s = 0
    if roman_string and isinstance(roman_string, str):
        for i in reversed(roman_string):
            for k, v in roman_dict.items():
                if i == k:
                    n.append(v)
        for i, num in enumerate(n):
            if i > 0 and num < n[i - 1]:
                s -= num
            else:
                s += num
        return abs(s)
    else:
        return 0

