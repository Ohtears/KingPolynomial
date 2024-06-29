import numpy as np
import random
from sympy import sympify, simplify
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations, 
    implicit_multiplication,
)
import time

class KingPolynomial:
    def __init__(self, matrix):
        self.matrix = matrix
        self.C1s = []
        self.coefficients = []

    def is_filled_with_ones(self, matrix):
        return np.all(matrix == 1)

    def create_C1(self, i, j, matrix):
        rows, cols = matrix.shape
        new_matrix = matrix.copy()
        
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    new_matrix[ni, nj] = 1

        return new_matrix

    def create_C2(self, i, j, matrix):
        matrix[i, j] = 1
        return matrix

    def recursive_formula(self):
        matrix = self.matrix
        generating_function = ["1"]

        while not self.is_filled_with_ones(matrix):
            zero_tiles = [(i, j) for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) if matrix[i, j] == 0]
            if not zero_tiles:
                return "0"

            selected_tile = random.choice(zero_tiles)
            i, j = selected_tile

            C1 = self.create_C1(i, j, matrix)
            matrix = self.create_C2(i, j, matrix)

            self.C1s.append(C1)

        for c1_matrix in self.C1s:
            kp_c1 = KingPolynomial(c1_matrix)
            c1_function = kp_c1.recursive_formula()
            generating_function.append(f"x({c1_function})")

        if not generating_function:
            return "1" 

        return self.simplify_generating_function(generating_function)

    def simplify_generating_function(self, generating_function):
        term_counts = {}
        for term in generating_function:
            if term in term_counts:
                term_counts[term] += 1
            else:
                term_counts[term] = 1
        
        simplified_terms = []
        for term, count in term_counts.items():
            if count == 1:
                simplified_terms.append(term)
            else:
                simplified_terms.append(f"{count}{term}")
        
        return " + ".join(simplified_terms)

    def run(self):
        generating_function = self.recursive_formula()
        elapsed_time = time.time() - start_time
        generating_function = parse_expr(generating_function, transformations=standard_transformations + (implicit_multiplication,))
        expr = sympify(generating_function)
        simplified_expr = simplify(expr)


        print("Generating Function (King Polynomial):")
        print(f"R(C, x) = {simplified_expr}")
        print(f"Elapsed time: {elapsed_time:.4f} seconds")


def main():
    print("Enter matrix dimensions and elements, line by line (press Enter twice to finish):")
    global start_time
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    start_time = time.time()

    input_data = "\n".join(lines)

    input_lines = input_data.strip().split("\n")

    dimensions = input_lines[0].split()
    rows = int(dimensions[0])
    cols = int(dimensions[1])

    matrix = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        row_elements = input_lines[i + 1].split()
        for j in range(cols):
            matrix[i, j] = int(row_elements[j])

    kp = KingPolynomial(matrix)
    kp.run()

main()
