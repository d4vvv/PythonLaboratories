import random
import numpy

A = [[random.randint(-10, 10) for x in range(128)] for y in range(128)]
B = [[random.randint(-10, 10) for x in range(128)] for y in range(128)]


def matrix_add(A_, B_):
    out_ = [[0 for x in range(len(A_))] for y in range(len(A_))]

    for row in range(len(A_)):
        for col in range(len(A_[row])):
            out_[row][col] = A_[row][col] + B_[row][col]

    return out_


print(matrix_add(A, B))
print(numpy.add(A, B))  # verification
