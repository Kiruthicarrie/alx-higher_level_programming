#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        n = max(a_dictionary.values())
        for i, j in a_dictionary.items():
            if j == n:
                return i
    return None
