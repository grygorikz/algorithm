text = "hello world hello python world hello"

words = text.split()
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)

print(sorted_words[:3])