import string

query = "Buy mobile phone buy phone online"

query = query.lower()

for char in string.punctuation:
    query = query.replace(char, "")

words = query.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

repeated_words = {}

for word, count in frequency.items():
    if count > 1:
        repeated_words[word] = count

print(repeated_words)
