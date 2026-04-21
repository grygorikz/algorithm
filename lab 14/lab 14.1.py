nums = [1, 2, 3, 2, 4, 1]

seen = []
duplicates = []

for num in nums:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.append(num)

print(duplicates)