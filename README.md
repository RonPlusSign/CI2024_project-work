# CI2024 Project – Symbolic Regression

Final project for the Computational Intelligence course @ Politecnico di Torino

## Problem Statement

**Symbolic regression** is the task of discovering a mathematical expression that best fits a given dataset.  
Given samples of inputs $x \in \mathbb{R}^n$ and corresponding outputs $y \in \mathbb{R}$, the goal is to automatically find an analytic function  
$$
f(x)\quad\text{such that}\quad f(x_i)\approx y_i
$$  
with minimal error, without assuming any fixed parametric form in advance.

## Solution Approach

All of the core code and experiments live in the `project.ipynb`.  In brief:

1. **Data loading and preprocessing**  
   - Sample synthetic datasets with known ground‑truth functions.  
   - Normalize and split into training/test sets.

2. **Symbolic regression via evolutionary search**  
   - Define a grammar of mathematical operators (e.g. `+`, `-`, `*`, `/`, `sin`, `cos`, `exp`, `abs`, …).  
   - Use a genetic programming engine to evolve candidate expression trees:  
     - Initialize a population of random trees  
     - Iteratively apply selection, crossover and mutation  
     - Evaluate fitness by mean squared error (MSE) on training data  

3. **Post‑processing & evaluation**  
   - Simplify discovered expressions where possible.  
   - Compute MSE on held‑out test data.  
   - Compare with baseline functions $f_0, f_1, \dots, f_8$.


## Project Structure

```
CI2024_project-work/
├── data/ # raw datasets
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