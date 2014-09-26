# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:10:01 2014

@author: iryna
"""
import numpy as np
import math


def euclidean(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def opt_euclidean(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def np_euclidean(a, b):
    return np.hypot(a[0] - b[0], a[1] - b[1])
