nums = [1, 1, 2, 2, 2, 3]

max_len = 1
current = 1

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        current += 1
        if current > max_len:
            max_len = current
    else:
        current = 1

print(max_len)