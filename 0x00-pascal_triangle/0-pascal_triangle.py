#!/usr/bin/env python 3
"""Create a function def pascal_triangle(n):
that returns a list of lists of integers"""

def pascal_triangle(n):
    list1 = [] #an empty list
    for i in range(n):
        list1.append([])
        list1[i].append(1)
        for j in range(1, i):
            list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
        if(n <= 0):
            list1[i].append(1)
    for i in range(n):
        print(" " * (n - i), end = " ", sep = " ")
        for j in range(0, i + 1):
            print('{0:6}'.format(list1[i][j]), end = " ", sep = " ")

