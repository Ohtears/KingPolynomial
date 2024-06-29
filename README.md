# King's Polynomial Generating Function Calculator

## Overview
This Python program calculates the generating function for the King's polynomial using a recursive approach. The generating function is represented by the recursive formula:

\[ R(C, r) = x \cdot R(C_1, r) + R(C_2, r) \]

where:
- \( R(C, r) \) is the generating function for the King's polynomial.
- \( C \) represents the shape we are working on.


## Usage
### Input
1. **Provide Input Dimensions**:
   - First, specify the dimensions (rows and columns) of your shape. For example, `3 3` indicates a shape with 3 rows and 3 columns.

2. **Shape Representation**:
   - Input your shape matrix:
     ```
     0 0 0
     0 0 0
     0 0 0
     ```
     - Use `0` to denote places where kings are allowed and `1` where they are not.

### Execution
- Run the Python script to compute the generating function. The program will output the result of \( R(C, x) \).

### Example
- Define the dimensions and shape matrix within the script as per your problem requirements.
- Execute the script to compute the generating function using the recursive relation provided.

## Notes
- Ensure Python is installed on your system.
- The program uses symbolic computation and recursion to compute the generating function.
- Customize the program structure and input handling based on your specific problem setup.
