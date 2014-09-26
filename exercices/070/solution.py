# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 18:48:45 2014

@author: iryna
"""
import string
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        if i != j:
            print(i+j)
