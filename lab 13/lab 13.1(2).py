#1 блок 1 задание
import time
import random
import matplotlib.pyplot as plt

def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


sizes = [100, 1000, 10000, 100000, 500000, 1000000]

linear_times = []
binary_times = []

for n in sizes:
    arr = list(range(n))
    target = random.choice(arr)

    start = time.time()
    linear_search(arr, target)
    linear_times.append(time.time() - start)

    start = time.time()
    binary_search(arr, target)
    binary_times.append(time.time() - start)

# График
plt.plot(sizes, linear_times, label='Linear Search')
plt.plot(sizes, binary_times, label='Binary Search')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('n')
plt.ylabel('time')
plt.legend()
plt.grid()

plt.show()