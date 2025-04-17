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
    return np.add(-0.7, np.add(-3.49, x[1]))

def f7(x: np.ndarray) -> np.ndarray: 
    return (np.exp((x[0] * x[1])) + 2.23)

def f8(x: np.ndarray) -> np.ndarray: 
    return ((x[5] * (x[5] + x[5])) * (x[5] * (x[5] * x[5])))


# Compute the MSE of the functions
if __name__ == "__main__":
    for i in range(9):
        # Load the function
        f = eval(f"f{i}")

        # Load the data
        data = np.load(f"data/problem_{i}.npz")
        x = data["x"]
        y = data["y"]

        # Compute the MSE
        mse = np.mean((f(x) - y) ** 2)
        print(f"f{i} MSE: {mse:.6f} " + ('✅' if mse < 1e-3 else '❌'))
