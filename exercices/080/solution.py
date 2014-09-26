# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 18:50:40 2014

@author: iryna
"""

import string
counti = 0
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase[counti + 1::]:
        if i != j:
            print(i+j)
    counti += 1
