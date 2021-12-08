import random
import numpy

def determinant_recursive(A, total=0):
    indices = list(range(len(A)))

    # When we get to 2x2 matrix we return the value
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        # We remove certain rows and columns
        As = A
        As = As[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = pow(-1,fc % 2)

        # We split the resultant matrix into smaller ones recursively
        sub_det = determinant_recursive(As)
        total += sign * A[0][fc] * sub_det

    return total


width = 5
height = 5
ExampleMatrix = [[random.randint(-20,20) for x in range(width)] for y in range(height)]

print(determinant_recursive(ExampleMatrix))
print(numpy.linalg.det(ExampleMatrix)) # Verification of the result

# Code based on integratedmlai.com
