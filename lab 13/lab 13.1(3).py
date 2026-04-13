REPEATS = 1000

# Линейный поиск
start = time.time()
for _ in range(REPEATS):
    linear_search(arr, target)
linear_times.append((time.time() - start) / REPEATS)

# Бинарный поиск
start = time.time()
for _ in range(REPEATS):
    binary_search(arr, target)
binary_times.append((time.time() - start) / REPEATS)