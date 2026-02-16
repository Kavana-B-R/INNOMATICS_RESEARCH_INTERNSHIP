# Problem 7: Count Character Frequency

string = "python"

char_count = {}

# Counting each character
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

