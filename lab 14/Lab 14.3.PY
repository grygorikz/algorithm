arr = [2, 7, 11, 15]
target = 9

seen = []

for num in arr:
    if target - num in seen:
        print(target - num, "+", num, "=", target)
        break
    seen.append(num)