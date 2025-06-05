# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])


def f2(x: np.ndarray) -> np.ndarray:
    return (((((17.976 + (13.556 + 98.991)) + ((34.785 + np.cos(x[2])) - (x[0] * (x[0] + x[0])))) * (((7.68 + np.cos(x[2])) + (x[2] + 98.991)) + (((x[0] * x[2]) - (x[0] * x[1])) - (x[0] * (x[1] + x[0]))))) * (((((x[1] * x[2]) - np.exp(x[2])) + (98.991 + 84.959)) + ((90.002 / x[0]) * (x[1] + x[2]))) + ((((11.47 * x[2]) + (x[1] + x[0])) + ((x[1] + x[0]) + (x[1] + x[0]))) * (((x[0] + x[0]) / (x[0] * 5)) - (x[1] + x[0]))))) * ((np.tanh(((x[0] - (x[0] - x[1])) + 6)) * x[0]) / (((np.exp(np.sin(x[2])) + np.abs((x[1] + x[0]))) + (((x[0] - x[1]) + np.exp(x[1])) - np.tanh((x[0] / x[2])))) ** ((((x[2] + x[2]) + (x[1] + x[0])) * x[2]) / (((x[2] - 34.785) + (x[2] + 350)) + (np.abs(x[0]) * (x[0] * x[1])))))))


def f3(x: np.ndarray) -> np.ndarray:
    return ((((x[0] * x[0]) + (x[0] * x[0])) + 4) - (((x[2] * 14) / 4) + (x[1] * (x[1] * x[1]))))


def f4(x: np.ndarray) -> np.ndarray: 
    return (np.tan((((x[0] / -7.911) * np.cos(-13.373)) - np.tan(np.exp(-5.089)))) + (((np.cos(x[1]) + np.cos(-13.44)) * 7) + np.tan(-4.021)))


def f5(x: np.ndarray) -> np.ndarray: 
    return 2.8520706810421615e-10 * ((((x[0] ** x[1]) - ((((np.tan(-39.724) - np.cos((-20.187 + np.log(x[0])))) / 4.38) - np.log(x[1])) - (-18.065 - np.log(np.abs(np.abs((np.sin(-18.339) * np.sin(x[1])))))))) / (4.484 + (np.abs(np.log(19.817)) + -36.106))))


def f6(x: np.ndarray) -> np.ndarray:
    return ((x[1] + x[1]) - (x[0] + ((x[0] / (np.cos(np.tan(-3.547)) - np.tan(np.abs(-20.187)))) - (x[1] / (np.cos((-12.357 + np.abs(np.tan(20.446)))) - np.tan(np.abs(np.tan(20.446))))))))


def f7(x: np.ndarray) -> np.ndarray:
    return (((((x[1] + ((10 / 92.147) + np.sin(x[1]))) + (x[1] / (np.tanh(x[0]) / x[1]))) + (np.sin((x[1] - (x[0] - x[1]))) + (np.sin(x[0]) + (np.sin(x[0]) + (x[1] + x[1]))))) * (x[0] / np.cos(np.cos((x[1] - x[0]))))) + np.exp(((2 + ((x[0] * x[1]) + ((9 - x[0]) / (20.038 + x[0])))) * np.cos(((200 / (24.951 - 60.469)) * np.tanh((x[0] - x[1])))))))


def f8(x: np.ndarray) -> np.ndarray: 
    return ((np.exp(x[3]) - (((36.419 - (((-48.79 + -40.34) - (((33.294 + (36.419 - x[5])) / np.exp(np.cos(x[5]))) ** np.cos(x[4]))) * (np.cos(np.sin(np.exp((x[4] + -40.34)))) - (np.sin((x[4] + (-11.033 + x[4]))) - (np.abs(np.cos((x[5] - 27.598))) + np.sin(x[5])))))) + ((((x[4] + np.sin(x[3])) - ((np.sin((np.exp(-1.663) - (x[4] + x[4]))) - ((x[4] + x[4]) + x[4])) * (-1.663 - (x[4] + (x[4] + x[4]))))) + (np.exp(np.tan(np.sin(x[3]))) - ((x[3] - 41.92) * (np.cos(x[4]) - x[3])))) - ((np.sin((np.tan(np.cos(-1.663)) - (x[4] + x[4]))) - (x[4] + (np.cos(np.log(26.12)) + (x[4] + x[4])))) * ((np.sin((np.tan(np.cos(-1.663)) - (x[4] + x[4]))) - (x[4] + np.sin(43.067))) - x[4])))) - ((-48.79 * np.sin(x[5])) + x[5]))) + (np.abs(-21.878) * ((((np.abs(np.abs(33.294)) - ((np.exp(-1.663) - (x[4] + x[4])) * (np.cos(-1.663) - x[4]))) + -22.214) * np.exp(np.exp((np.exp((np.abs(-16.989) - ((np.sin(x[4]) - (x[4] + x[4])) * ((41.697 ** -11.033) - (x[4] + x[4]))))) * -26.183)))) + (np.exp(np.abs(x[5])) * x[5]))))


# Compute the MSE of the functions
if __name__ == "__main__":
    for i in range(1, 9):
        # Load the function
        f = eval(f"f{i}")

        # Load the data
        data = np.load(f"data/problem_{i}.npz")
        x = data["x"]
        y = data["y"]

        # Compute the MSE
        mse = np.mean((f(x) - y) ** 2)
        print(f"f{i} MSE: {mse:.5e} ")
