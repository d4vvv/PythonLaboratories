A = [1, 2, 12, 4]
B = [2, 4, 2, 8]

def scalar(A_, B_):
    out_ = 0

    for x in range(len(A_)):
        out_ += A_[x] * B_[x]

    return out_

print(scalar(A,B))