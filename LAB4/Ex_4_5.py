import random
import numpy

A = [[random.randint(-10, 10) for x in range(8)] for y in range(8)]
B = [[random.randint(-10, 10) for x in range(8)] for y in range(8)]


def matrix_multiply(A_, B_):
    out_ = [[0 for x in range(len(A_))] for y in range(len(A_))]

    for row in range(len(A_)):
        for col in range(len(B_[0])):
            for val in range(len(B_)):
                out_[row][col] += A_[row][val] * B_[val][col]

    return out_


print(matrix_multiply(A, B))
print(numpy.matmul(A, B))  # verification
