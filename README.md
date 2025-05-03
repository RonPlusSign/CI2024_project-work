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

| Function | MSE          | Expression |
|:--------:|:------------:|------------|
| **f1**   | $3.921 \cdot 10^{-34}$  | `np.sin(x[0])` |
| **f2**   | $2.241 \cdot 10^{12}$  | `56465.10655809015 + 54418.561240135256 * (((np.tanh(66.643) - (-78.956 * np.arcsin(np.tanh((((x[1] + x[2]) + (x[0] + (x[0] + x[0]))) - x[0]))))) - ((x[2] + (x[2] + (x[0] + x[1]))) * np.abs(((x[1] + x[0]) * np.arcsin(np.tanh(x[0])))))))` |
| **f3**   | $8.404 \cdot 10^{-1}$  | `(((((((x[0] * x[0]) - x[2]) - x[2]) - (x[1] * np.abs(((x[1] * x[1]) + (x[2] / (x[1] + x[1])))))) + np.abs((x[0] * x[0]))) - -3.547) - x[2])` |
| **f4**   | $1.797 \cdot 10^{-1}$ | `(np.cos((np.cos(x[1]) - (np.exp(((((x[0] * 29.294) - (-40.218 - 29.294)) / x[0]) / ((x[0] + (-40.218 - x[1])) * -47.89))) ** x[0]))) * np.abs(np.exp(np.exp(np.cos(np.sin(np.cos(np.sin(np.cos(x[1])))))))))` |
| **f5**   | $1.917 \cdot 10^{-22}$ | `2.8520706810421615e-10 * ((((x[0] ** x[1]) - ((((np.tan(-39.724) - np.cos((-20.187 + np.log(x[0])))) / 4.38) - np.log(x[1])) - (-18.065 - np.log(np.abs(np.abs((np.sin(-18.339) * np.sin(x[1])))))))) / (4.484 + (np.abs(np.log(19.817)) + -36.106))))` |
| **f6**   | $5.736 \cdot 10^{-5}$  | `((x[1] + x[1]) - (x[0] + ((x[0] / (np.cos(np.tan(-3.547)) - np.tan(np.abs(-20.187)))) - (x[1] / (np.cos((-12.357 + np.abs(np.tan(20.446)))) - np.tan(np.abs(np.tan(20.446))))))))` |
| **f7**   | $1.503 \cdot 10^{2}$   | `(np.abs((np.tan(np.exp(np.cos(-5.523))) * np.exp((np.tan(np.cos(((x[1] - x[0]) * -4.419))) + (x[0] * x[1]))))) - (x[1] * x[0]))` |
| **f8**   | $1.055 \cdot 10^{6}$   | `(((-49.684 * np.exp(np.abs(x[5]))) + ((np.abs(np.exp(x[5])) + np.log(0.578)) * (np.exp(4.718) + 15.38))) / np.cos(np.cos(np.abs(np.exp((x[5] / np.exp(x[5])))))))` |


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