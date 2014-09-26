# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 13:46:07 2014

@author: iryna
"""
fibminone = 1
fibmintwo = 0
for i in range(1, 10):
    i = fibmintwo + fibminone
    print(i, end=", ")
    fibmintwo = fibminone
    fibminone = i
i = fibmintwo + fibminone
print(i, end=". ")
