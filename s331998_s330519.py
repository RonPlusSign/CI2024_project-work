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
    return ((np.exp(x[3]) - (((43.635 - (((-48.79 + -24.454) - (((np.abs(-22.214) + (36.419 - x[4])) / np.exp(np.cos(43.061))) ** np.cos(x[4]))) * (np.cos(np.sin(np.abs(np.cos(np.exp(-10.171))))) - (np.sin((x[4] + (-11.033 + x[4]))) - (np.abs(np.cos(np.tan(-15.991))) + np.sin(x[5])))))) + (((41.194 - ((np.sin((np.exp(-1.663) - (x[4] + x[4]))) - ((x[4] + x[4]) + x[4])) * (-1.663 - (x[4] + (x[4] + x[4]))))) + (np.tan(np.abs(np.abs(np.cos(np.tan(-15.991))))) - ((x[3] - 36.419) * (np.cos(x[4]) - x[3])))) - ((np.exp(np.cos(np.exp(-1.663))) - (x[4] + (x[4] + (x[4] + x[4])))) * ((np.sin((np.tan(np.cos(-1.663)) - (x[4] + x[4]))) - (x[4] + np.sin(x[5]))) - x[4])))) - ((-48.79 * np.sin(x[3])) + x[2]))) + (np.abs(-21.878) * ((((np.abs(np.abs(33.294)) - ((np.exp(-1.663) - (x[4] + x[4])) * (np.cos(-1.663) - x[4]))) + -22.214) * np.exp(np.exp((np.exp((np.abs(-16.989) - ((np.sin(x[5]) - (x[4] + x[4])) * ((41.697 ** -11.033) - (x[4] + x[4]))))) * np.tan((np.abs(-21.878) + np.tan(np.cos(-1.663)))))))) + (np.exp(np.abs(x[5])) * x[5]))))

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
