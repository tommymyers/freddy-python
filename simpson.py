#!/usr/local/bin/python

import math

def f(x):
    return math.sin(x) / (math.exp(x) + 4)

def simpson(a, b, n):
    dx = (b - a) / n
    sum_of_odds = sum([f(a + (dx * x)) for x in range(1, n, 2)])
    sum_of_evens = sum([f(a + dx * x) for x in range(2, n, 2)])
    return dx / 3 * (f(a) + 4 * sum_of_odds + 2 * sum_of_evens + f(b))

print(simpson(0, 10, 100))