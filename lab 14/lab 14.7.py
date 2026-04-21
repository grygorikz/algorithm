a = [1, 2, 3]
b = [2, 3, 4]

result = []

for num in a:
    if num in b and num not in result:
        result.append(num)

print(result)