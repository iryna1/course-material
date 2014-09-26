# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 13:11:00 2014

@author: iryna
"""


def is_alpha(mystring):
    if mystring.isalpha() and len(mystring) == 1:
        return True
    else:
        return False
