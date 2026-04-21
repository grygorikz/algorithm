students = [("Иван", 80), ("Анна", 95), ("Олег", 78)]

best = students[0]

for student in students:
    if student[1] > best[1]:
        best = student

print(best)