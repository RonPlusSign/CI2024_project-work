# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


# Notez bien: No need to include f0 -- it's just an example!
def f0(x: np.ndarray) -> np.ndarray:
    return x[0] + np.sin(x[1]) / 5


def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: 
    return (((x[0] / (x[1] / (x[2] + x[2]))) - ((np.sin(x[1]) + np.cos(x[2])) + np.tan((x[2] - x[2])))) + np.log(np.exp((np.sin(x[1]) / 4.62))))


def f3(x: np.ndarray) -> np.ndarray:
    return (np.cos(2.24) + ((x[1] * x[1]) * (x[1] * np.cos(2.24))))

def f4(x: np.ndarray) -> np.ndarray: 
    return (np.cos(x[1]) + (np.exp(np.cos(x[1])) * np.exp(np.cos(x[1]))))


def f5(x: np.ndarray) -> np.ndarray: 
    return np.sin((np.sin(np.tan(x[0])) * np.log(((x[1] * x[0]) / (x[0] + x[0])))))


def f6(x: np.ndarray) -> np.ndarray: 
    return (x[1] + (np.sin(np.sin(((x[1] / x[1]) + np.tan(4.91)))) * ((np.cos((x[0] - x[0])) - x[0]) + (x[1] - np.exp((4.91 / x[1]))))))


def f7(x: np.ndarray) -> np.ndarray: 
    return (np.exp((x[0] * x[1])) + 2.23)


def f8(x: np.ndarray) -> np.ndarray: 
    return ((x[5] * (x[5] + x[5])) * (x[5] * (x[5] * x[5])))

