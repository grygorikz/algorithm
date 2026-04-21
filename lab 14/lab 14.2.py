nums = [1, 2, 2, 3, 3, 3]

max_count = 0
result = None

for num in nums:
    count = nums.count(num)
    if count > max_count:
        max_count = count
        result = num

print(result)