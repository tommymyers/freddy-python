#!/usr/bin/env python3

import math

def simpson(f, a, b, n):
    dx = (b - a) / n
    sum_of_odds = sum([f(a + dx * x) for x in range(1, n, 2)])
    sum_of_evens = sum([f(a + dx * x) for x in range(2, n, 2)])
    return dx / 3 * (f(a) + 4*sum_of_odds + 2*sum_of_evens + f(b))

f = lambda x: math.sin(x) / (math.exp(x) + 4)

print(simpson(f, 0, 10, 100))