#3 блок 11 задание
import time

#РЕКУРСИЯ 
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

#ИТЕРАЦИЯ
def fib_iterative(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

#СРАВНЕНИЕ
print(" n | recursion (s) | iteration (s)")
print("----------------------------------")

for n in range(5, 45):
    start = time.perf_counter()
    fib_recursive(n)
    t_rec = time.perf_counter() - start

    start = time.perf_counter()
    fib_iterative(n)
    t_it = time.perf_counter() - start

    print(f"{n:2} | {t_rec:12.6f} | {t_it:12.6f}")