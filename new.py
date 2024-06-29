import numpy as np
import random

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
        generating_function = []

        while not self.is_filled_with_ones(matrix):
            zero_tiles = [(i, j) for i in range(matrix.shape[0]) for j in range(matrix.shape[1]) if matrix[i, j] == 0]
            if not zero_tiles:
                return "0"  

            
            selected_tile = random.choice(zero_tiles)
            i, j = selected_tile

            C1 = self.create_C1(i, j, matrix)
            matrix = self.create_C2(i, j, matrix)

            self.C1s.append(C1)

            generating_function.append(f"x * R(C1, r) + R(C2, r)")

        return generating_function

    def run(self):
        generating_function = self.recursive_formula()
        print("Generating Function (King Polynomial):")
        print("R(matrix, r) =", " + ".join(generating_function))

        # for c1_matrix in self.C1s[:]: 
        #     kp_c1 = KingPolynomial(c1_matrix)
        #     kp_c1.recursive_formula()
        #     self.C1s.extend(kp_c1.C1s)

def main():
    print("Enter matrix dimensions and elements, line by line (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
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
