#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        sh = 0
        a = roman_string
        b = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for j in range(len(a)):
            for i, k in b.items():
                if i == a[j]:
                    if j + 1 < len(a) and b[a[j + 1]] > b[a[j]]:
                        sh -= k
                    else:
                        sh += k
        return sh
    return 0
