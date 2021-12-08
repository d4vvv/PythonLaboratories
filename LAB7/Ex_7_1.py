import random
import threading
import numpy
import matplotlib.pyplot as plt

random_list = []
for x in range(0, 1000000):
    random_list.append(random.randint(0,50))

left_side = random_list[:len(random_list) // 2]
right_side = random_list[len(random_list) // 2:]

left_hist = {}
right_hist = {}


def thread_A():
    for v in left_side:
        left_hist[v] = left_hist.get(v, 0) + 1 # we increment the number of occurrences of a given number


def thread_B():
    for l in right_side:
        right_hist[l] = right_hist.get(l, 0) + 1


thread_1 = threading.Thread(target=thread_A())
thread_2 = threading.Thread(target=thread_B())

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

result_hist = {}

for x in range(0, len(right_hist)):
    result_hist[x] = right_hist[x] + left_hist[x]

print(result_hist)

plt.bar(result_hist.keys(), result_hist.values(), 1.0, color = 'b')
plt.show()