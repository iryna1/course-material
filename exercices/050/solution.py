# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 18:29:09 2014

@author: iryna
"""
sum = 0
for i in range(1, 7):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i
print(sum)
