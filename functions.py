# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:27:55 2018

@author: cluel
"""

from Polynomial_Class import *

f = Polynomial([1, 0, -4])

def Newtons_Iteration(f, x_guess):
    return x_guess - (f(x_guess)/f.derivative()(x_guess))

def Newtons_Method(f, x_guess, epsilon):
    x = x_guess
    while abs(f(x)) > epsilon:
        x = Newtons_Iteration(f, x)
    return x

def find_extrema(f, x_guess, epsilon):
    x = Newtons_Method(f.derivative(), x_guess, epsilon)
    return (x, f(x))

print(find_extrema(f, 4, 0.00000001))