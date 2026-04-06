text = "python is great and python is easy"
words = text.lower().split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

most_common = max(count, key=count.get)

print(most_common)