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
    return 56465.10655809015 + 5441856.124013525 * (np.sin(np.sin((np.tan(np.abs(np.sin(np.sin(np.sin((np.cos(np.sin(np.sin(0.422))) + (0.414 * np.sin((np.cos((x[0] - (np.exp(x[2]) ** np.log(np.sin(0.085))))) - x[0]))))))))) * (x[0] * np.cos(np.exp(((x[2] * (0.596 ** x[0])) * (np.tan(-0.018) * np.sin(x[0]))))))))))

def f3(x: np.ndarray) -> np.ndarray:
    #return (np.cos(2.24) + ((x[1] * x[1]) * (x[1] * np.cos(2.24))))
    #return np.multiply(np.divide(np.abs(x[1]), np.sin(34.82)), x[1])
    # return np.add(np.add(np.abs(np.multiply(np.abs(x[0]), 2.19)), np.subtract(np.subtract(np.exp(np.subtract(np.abs(np.sin(np.exp(x[1]))), x[1])), np.exp(x[1])), -8.93)), np.multiply(np.abs(x[0]), 2.19))
    return 21.20757039569563 + 50.61161179521197 * (((np.tan(np.sin(x[1])) - (np.cos(np.cos(np.exp(np.cos(np.abs(x[1]))))) * x[1])) * np.tan(0.352)))


def f4(x: np.ndarray) -> np.ndarray: 
    #return (np.cos(x[1]) + (np.exp(np.cos(x[1])) * np.exp(np.cos(x[1]))))
    return 1.9997861267141543 + 4.649946409222459 * (np.tan(np.cos((np.cos(np.sin(np.abs(np.log((np.sin(np.abs(np.sin((-0.056 / x[1])))) ** 0.73))))) * x[1]))))

def f5(x: np.ndarray) -> np.ndarray: 
    #return np.sin((np.sin(np.tan(x[0])) * np.log(((x[1] * x[0]) / (x[0] + x[0])))))
    return np.power(np.abs(np.cos(np.sin(np.sin(np.sin(np.sin(np.abs(np.abs(x[0])))))))), np.abs(np.subtract(np.cos(np.multiply(np.divide(np.tan(x[1]), np.add(np.add(np.exp(np.divide(x[1], x[0])), np.abs(np.cos(x[1]))), np.abs(np.divide(np.tan(x[0]), np.multiply(x[0], x[1]))))), np.tan(x[0]))), np.multiply(np.multiply(np.cos(x[0]), np.add(np.abs(np.exp(np.exp(np.log(34.82)))), x[1])), x[1]))))

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
