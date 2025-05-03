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
    return 56465.10655809015 + 54418.561240135256 * (((np.tanh(66.643) - (-78.956 * np.arcsin(np.tanh((((x[1] + x[2]) + (x[0] + (x[0] + x[0]))) - x[0]))))) - ((x[2] + (x[2] + (x[0] + x[1]))) * np.abs(((x[1] + x[0]) * np.arcsin(np.tanh(x[0])))))))


def f3(x: np.ndarray) -> np.ndarray:
    return (((((((x[0] * x[0]) - x[2]) - x[2]) - (x[1] * np.abs(((x[1] * x[1]) + (x[2] / (x[1] + x[1])))))) + np.abs((x[0] * x[0]))) - -3.547) - x[2])


def f4(x: np.ndarray) -> np.ndarray: 
    return (np.cos((np.cos(x[1]) - (np.exp(((((x[0] * 29.294) - (-40.218 - 29.294)) / x[0]) / ((x[0] + (-40.218 - x[1])) * -47.89))) ** x[0]))) * np.abs(np.exp(np.exp(np.cos(np.sin(np.cos(np.sin(np.cos(x[1])))))))))


def f5(x: np.ndarray) -> np.ndarray: 
    return 2.8520706810421615e-10 * ((((x[0] ** x[1]) - ((((np.tan(-39.724) - np.cos((-20.187 + np.log(x[0])))) / 4.38) - np.log(x[1])) - (-18.065 - np.log(np.abs(np.abs((np.sin(-18.339) * np.sin(x[1])))))))) / (4.484 + (np.abs(np.log(19.817)) + -36.106))))


def f6(x: np.ndarray) -> np.ndarray:
    return ((x[1] + x[1]) - (x[0] + ((x[0] / (np.cos(np.tan(-3.547)) - np.tan(np.abs(-20.187)))) - (x[1] / (np.cos((-12.357 + np.abs(np.tan(20.446)))) - np.tan(np.abs(np.tan(20.446))))))))


def f7(x: np.ndarray) -> np.ndarray: 
    return (np.abs((np.tan(np.exp(np.cos(-5.523))) * np.exp((np.tan(np.cos(((x[1] - x[0]) * -4.419))) + (x[0] * x[1]))))) - (x[1] * x[0]))


def f8(x: np.ndarray) -> np.ndarray: 
    return (((x[5] * (21.67 * (np.exp(np.abs(x[5])) + (-23.543 / x[5])))) - (np.exp(x[4]) * np.abs(x[4]))) - (np.exp(x[4]) / np.cos(-30.641)))


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
        print(f"f{i} MSE: {mse:.3e} " + ('✅' if mse < 1e-3 else '❌'))
