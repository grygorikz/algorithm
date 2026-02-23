import random

SIZE = 4

field = [[0]*SIZE for _ in range(SIZE)]

for _ in range(4):
    i = random.randint(0, SIZE-1)
    j = random.randint(0, SIZE-1)
    field[i][j] = 2

def print_field():
    for row in field:
        print(*row)
    print()

def move_right():
    for i in range(SIZE):
        row = field[i]

        row = [x for x in row if x != 0]

        j = len(row) - 1
        while j > 0:
            if row[j] == row[j-1]:
                row[j] *= 2
                row.pop(j-1)
                j -= 1
            j -= 1
            
        while len(row) < SIZE:
            row.insert(0, 0)

        field[i] = row

print("До хода:")
print_field()

move_right()

print("После хода вправо:")
print_field()