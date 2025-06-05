# CI2024 Project – Symbolic Regression

Final project for the Computational Intelligence course @ Politecnico di Torino. This project was entirely developed in collaboration with my colleague [Giorgia Modi](https://github.com/GiorgiaModi).

## Problem Statement

**Symbolic regression** is the task of discovering a mathematical expression that best fits a given dataset.  
Given samples of inputs $x \in \mathbb{R}^n$ and corresponding outputs $y \in \mathbb{R}$, the goal is to automatically find an analytic function $f(x)$ such that $f(x_i)\approx y_i$ with minimal error, without assuming any fixed parametric form in advance.

## Solution Approach

All of the core code and experiments live in the `project.ipynb`. This notebook implements a genetic programming approach for symbolic regression, aiming to find mathematical expressions that best fit given datasets. The main steps and functions are:

1. **Initialization**: The algorithm starts by generating a population of random expression trees using `generate_random_tree`. Each tree represents a candidate mathematical expression.

2. **Evaluation**: Each individual is evaluated on the dataset using the `fitness` function, which computes the mean squared error (MSE) between the predicted and true values.

3. **Selection**: Parents for the next generation are chosen using one of several strategies: tournament, rank, or fitness-proportional selection, implemented in `parent_selection` and its helper functions.

4. **Genetic Operators**:
- **Crossover:**  
  The `crossover` function swaps random subtrees between two parent trees to create offspring.
- **Mutation:**  
  Two types of mutation are implemented:
  - `subtree_mutation`: Replaces a subtree with a new random subtree.
  - `point_mutation`: Alters a node’s content or its children.
  - The `mutation` function randomly applies one of these mutations.

5. **Elitism**: The best-performing individuals (elite) are carried over to the next generation to ensure that good solutions are not lost.

6. **Termination**: The process repeats for a fixed number of generations or until a solution with sufficiently low error is found.


## Project Structure

```
CI2024_project-work/
├── data/ # datasets
├── plots/ # predicted vs real plots
├── project.ipynb # core symbolic regression notebook
├── s331998.py # solution functions
├── .gitignore
└── README.md # this file
```


## Results

Mean Squared Error (MSE) and full expressions for each target function:

| Function |            MSE           | Expression                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :------: | :----------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  **f1**  |  0.000  | `np.sin(x[0])`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|  **f2**  |  5.88066e+11 | `(((((17.976 + (13.556 + 98.991)) + ((34.785 + np.cos(x[2])) - (x[0] * (x[0] + x[0])))) * (((7.68 + np.cos(x[2])) + (x[2] + 98.991)) + (((x[0] * x[2]) - (x[0] * x[1])) - (x[0] * (x[1] + x[0]))))) * (((((x[1] * x[2]) - np.exp(x[2])) + (98.991 + 84.959)) + ((90.002 / x[0]) * (x[1] + x[2]))) + ((((11.47 * x[2]) + (x[1] + x[0])) + ((x[1] + x[0]) + (x[1] + x[0]))) * (((x[0] + x[0]) / (x[0] * 5)) - (x[1] + x[0]))))) * ((np.tanh(((x[0] - (x[0] - x[1])) + 6)) * x[0]) / (((np.exp(np.sin(x[2])) + np.abs((x[1] + x[0]))) + (((x[0] - x[1]) + np.exp(x[1])) - np.tanh((x[0] / x[2])))) ** ((((x[2] + x[2]) + (x[1] + x[0])) * x[2]) / (((x[2] - 34.785) + (x[2] + 350)) + (np.abs(x[0]) * (x[0] * x[1])))))))`                                                                                                                                                                                                                                                                                                            |
|  **f3**  | 3.31370e-29 | `((((x[0] * x[0]) + (x[0] * x[0])) + 4) - (((x[2] * 14) / 4) + (x[1] * (x[1] * x[1]))))`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|  **f4**  |  2.13754e-05 | `(np.tan((((x[0] / -7.911) * np.cos(-13.373)) - np.tan(np.exp(-5.089)))) + (((np.cos(x[1]) + np.cos(-13.44)) * 7) + np.tan(-4.021)))`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|  **f5**  | 1.91664e-22 | `2.8520706810421615e-10 * ((((x[0] ** x[1]) - ((((np.tan(-39.724) - np.cos((-20.187 + np.log(x[0])))) / 4.38) - np.log(x[1])) - (-18.065 - np.log(np.abs(np.abs((np.sin(-18.339) * np.sin(x[1])))))))) / (4.484 + (np.abs(np.log(19.817)) + -36.106))))`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|  **f6**  |  5.73586e-05 | `((x[1] + x[1]) - (x[0] + ((x[0] / (np.cos(np.tan(-3.547)) - np.tan(np.abs(-20.187)))) - (x[1] / (np.cos((-12.357 + np.abs(np.tan(20.446)))) - np.tan(np.abs(np.tan(20.446))))))))`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|  **f7**  |  5.02807e+01  | `(((((x[1] + ((10 / 92.147) + np.sin(x[1]))) + (x[1] / (np.tanh(x[0]) / x[1]))) + (np.sin((x[1] - (x[0] - x[1]))) + (np.sin(x[0]) + (np.sin(x[0]) + (x[1] + x[1]))))) * (x[0] / np.cos(np.cos((x[1] - x[0]))))) + np.exp(((2 + ((x[0] * x[1]) + ((9 - x[0]) / (20.038 + x[0])))) * np.cos(((200 / (24.951 - 60.469)) * np.tanh((x[0] - x[1])))))))`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|  **f8**  |  2.33539e+04  | `((np.exp(x[3]) - (((36.419 - (((-48.79 + -40.34) - (((33.294 + (36.419 - x[5])) / np.exp(np.cos(x[5]))) ** np.cos(x[4]))) * (np.cos(np.sin(np.exp((x[4] + -40.34)))) - (np.sin((x[4] + (-11.033 + x[4]))) - (np.abs(np.cos((x[5] - 27.598))) + np.sin(x[5])))))) + ((((x[4] + np.sin(x[3])) - ((np.sin((np.exp(-1.663) - (x[4] + x[4]))) - ((x[4] + x[4]) + x[4])) * (-1.663 - (x[4] + (x[4] + x[4]))))) + (np.exp(np.tan(np.sin(x[3]))) - ((x[3] - 41.92) * (np.cos(x[4]) - x[3])))) - ((np.sin((np.tan(np.cos(-1.663)) - (x[4] + x[4]))) - (x[4] + (np.cos(np.log(26.12)) + (x[4] + x[4])))) * ((np.sin((np.tan(np.cos(-1.663)) - (x[4] + x[4]))) - (x[4] + np.sin(43.067))) - x[4])))) - ((-48.79 * np.sin(x[5])) + x[5]))) + (np.abs(-21.878) * ((((np.abs(np.abs(33.294)) - ((np.exp(-1.663) - (x[4] + x[4])) * (np.cos(-1.663) - x[4]))) + -22.214) * np.exp(np.exp((np.exp((np.abs(-16.989) - ((np.sin(x[4]) - (x[4] + x[4])) * ((41.697 ** -11.033) - (x[4] + x[4]))))) * -26.183)))) + (np.exp(np.abs(x[5])) * x[5]))))` |



## Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/RonPlusSign">
        <img src="https://github.com/RonPlusSign.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>Andrea Delli</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/GiorgiaModi">
        <img src="https://github.com/GiorgiaModi.png" width="50px" style="border-radius: 50%; border: none;" alt=""/>
        <br />
        <sub>Giorgia Modi</sub>
      </a>
    </td>
  </tr>
</table>
