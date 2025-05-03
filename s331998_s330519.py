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
    #return (((x[0] / (x[1] / (x[2] + x[2]))) - ((np.sin(x[1]) + np.cos(x[2])) + np.tan((x[2] - x[2])))) + np.log(np.exp((np.sin(x[1]) / 4.62))))
    #return np.multiply(np.multiply(73.05, np.multiply(np.abs(23.51), 7.13)), np.multiply(x[0], 93.4))
    #return 1_000_000 * np.add(np.add(np.divide(np.add(x[2], np.add(np.add(x[1], x[1]), np.add(x[2], np.exp(x[0])))), np.exp(np.abs(x[0]))), x[0]), np.sin(np.multiply(np.sin(np.cos(np.cos(-4.82))), x[0])))
    # return np.power(np.exp(np.log(np.subtract(np.subtract(26.87, x[0]), np.subtract(x[1], np.sin(x[1]))))), x[0])
    # return 56465.10655809015 + 5441856.124013525 * (np.sin(np.sin((np.tan(np.abs(np.sin(np.sin(np.sin((np.cos(np.sin(np.sin(0.422))) + (0.414 * np.sin((np.cos((x[0] - (np.exp(x[2]) ** np.log(np.sin(0.085))))) - x[0]))))))))) * (x[0] * np.cos(np.exp(((x[2] * (0.596 ** x[0])) * (np.tan(-0.018) * np.sin(x[0]))))))))))
    # return 76430.20544814717 * ((((((((16.107 + np.sin(np.abs(x[0]))) + np.sin(np.abs(x[0]))) + (x[1] / x[0])) + (x[2] / ((x[0] - np.sin(x[0])) - np.abs(-6.335)))) + ((x[2] / x[0]) - (x[2] * x[1]))) + np.sin((x[1] / np.exp(np.sin(x[0]))))) * x[0]))
    return 56465.10655809015 + 54418.561240135256 * (((np.tanh(66.643) - (-78.956 * np.arcsin(np.tanh((((x[1] + x[2]) + (x[0] + (x[0] + x[0]))) - x[0]))))) - ((x[2] + (x[2] + (x[0] + x[1]))) * np.abs(((x[1] + x[0]) * np.arcsin(np.tanh(x[0])))))))


def f3(x: np.ndarray) -> np.ndarray:
    #return (np.cos(2.24) + ((x[1] * x[1]) * (x[1] * np.cos(2.24))))
    #return np.multiply(np.divide(np.abs(x[1]), np.sin(34.82)), x[1])
    # return np.add(np.add(np.abs(np.multiply(np.abs(x[0]), 2.19)), np.subtract(np.subtract(np.exp(np.subtract(np.abs(np.sin(np.exp(x[1]))), x[1])), np.exp(x[1])), -8.93)), np.multiply(np.abs(x[0]), 2.19))
    # return 21.20757039569563 + 50.61161179521197 * (((np.tan(np.sin(x[1])) - (np.cos(np.cos(np.exp(np.cos(np.abs(x[1]))))) * x[1])) * np.tan(0.352)))
    # return (((np.arctan(np.cosh(np.cosh((((x[2] - np.sinh(x[1])) - (x[1] - x[2])) - (np.cosh(np.abs(np.abs(-50.2))) - (np.cosh(x[0]) - (x[2] + x[0]))))))) + ((((((np.cosh(x[0]) - x[2]) - np.sinh(x[1])) - x[1]) - np.sinh(x[1])) + (13.84 - 10.748)) - x[2])) - x[2]) + np.arctan(((np.cosh(np.abs(-50.2)) - (np.cosh(x[0]) - (x[2] + x[0]))) - ((((((np.tanh(np.tanh(x[1])) * x[1]) + ((np.cosh(x[0]) - x[2]) - np.sinh(x[1]))) - (x[1] - np.tanh((np.cosh(x[0]) - x[2])))) - np.sinh(np.sinh(x[1]))) + x[0]) - (np.sinh(np.sinh(x[1])) - np.sinh(np.cosh(x[0])))))))
    return (((((((x[0] * x[0]) - x[2]) - x[2]) - (x[1] * np.abs(((x[1] * x[1]) + (x[2] / (x[1] + x[1])))))) + np.abs((x[0] * x[0]))) - -3.547) - x[2])


def f4(x: np.ndarray) -> np.ndarray: 
    #return (np.cos(x[1]) + (np.exp(np.cos(x[1])) * np.exp(np.cos(x[1]))))
    # return 1.9997861267141543 + 4.649946409222459 * (np.tan(np.cos((np.cos(np.sin(np.abs(np.log((np.sin(np.abs(np.sin((-0.056 / x[1])))) ** 0.73))))) * x[1]))))
    # return (np.sinh((np.sinh(np.cos(x[1])) - (np.arctan(np.tanh(-92.033)) - np.cos(np.exp(np.tanh(-555.634)))))) - ((np.abs(np.cos(x[1])) - np.sinh(np.cos(x[1]))) - np.sinh(np.cos(x[1]))))
    return (np.cos((np.cos(x[1]) - (np.exp(((((x[0] * 29.294) - (-40.218 - 29.294)) / x[0]) / ((x[0] + (-40.218 - x[1])) * -47.89))) ** x[0]))) * np.abs(np.exp(np.exp(np.cos(np.sin(np.cos(np.sin(np.cos(x[1])))))))))


def f5(x: np.ndarray) -> np.ndarray: 
    #return np.sin((np.sin(np.tan(x[0])) * np.log(((x[1] * x[0]) / (x[0] + x[0])))))
    # return -5.794871983107769e-10 + 2.2884503096224875e-11 * ((x[1] - np.exp(x[1])))
    return 2.8520706810421615e-10 * ((((x[0] ** x[1]) - ((((np.tan(-39.724) - np.cos((-20.187 + np.log(x[0])))) / 4.38) - np.log(x[1])) - (-18.065 - np.log(np.abs(np.abs((np.sin(-18.339) * np.sin(x[1])))))))) / (4.484 + (np.abs(np.log(19.817)) + -36.106))))


def f6(x: np.ndarray) -> np.ndarray:
    # return ((x[1] + np.tanh(x[1])) - x[0])
    # return (x[1] + (x[1] + (np.arctan(np.abs((np.cosh(np.arctan(np.cosh(x[1]))) ** x[0]))) - x[0])))
    return ((x[1] + x[1]) - (x[0] + ((x[0] / (np.cos(np.tan(-3.547)) - np.tan(np.abs(-20.187)))) - (x[1] / (np.cos((-12.357 + np.abs(np.tan(20.446)))) - np.tan(np.abs(np.tan(20.446))))))))


def f7(x: np.ndarray) -> np.ndarray: 
    # return (np.exp((x[0] * x[1])) + 2.23)
    # return (np.abs(np.cosh(np.log2(np.exp((x[1] + x[0]))))) + (np.exp(x[1]) ** (x[0] - (np.tanh(-109.166) / np.log2(np.abs(-852.452))))))
    return (np.abs((np.tan(np.exp(np.cos(-5.523))) * np.exp((np.tan(np.cos(((x[1] - x[0]) * -4.419))) + (x[0] * x[1]))))) - (x[1] * x[0]))


def f8(x: np.ndarray) -> np.ndarray: 
    # return ((x[5] * (x[5] + x[5])) * (x[5] * (x[5] * x[5])))
    # return ((x[5] * (np.cosh(np.abs(x[5])) - -716.414)) + (-716.414 + np.sinh((x[5] + x[5]))))
    return (((-49.684 * np.exp(np.abs(x[5]))) + ((np.abs(np.exp(x[5])) + np.log(0.578)) * (np.exp(4.718) + 15.38))) / np.cos(np.cos(np.abs(np.exp((x[5] / np.exp(x[5])))))))



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
