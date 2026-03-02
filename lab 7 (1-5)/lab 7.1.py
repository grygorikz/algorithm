def add(a, b):
    return a + b
def power(a, n=2):
    return a ** n
def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total
print("summa 5 i 3:", add(5, 3))
print("3 v kvadrate:", power(3))
print("2 v stepeni 4:", power(2, 4))
print("summa chisel 1, 2, 3, 4:", sum_all(1, 2, 3, 4))