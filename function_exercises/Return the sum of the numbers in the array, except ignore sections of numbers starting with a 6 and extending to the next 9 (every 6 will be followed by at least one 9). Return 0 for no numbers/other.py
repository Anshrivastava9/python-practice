#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:44:52 2019

@author: sandeep
"""

def summer_69(arr):
    total = 0 
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
                
        while not add:
            if num !=9:
                break
            else:
                add = True
                
    return total

# Check
print(summer_69([1, 3, 5]))

# Check
print(summer_69([4, 5, 6, 7, 8, 9]))

# Check
print(summer_69([2, 1, 6, 9, 11]))