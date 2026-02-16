numbers = [45, 22, 89, 10, 66]
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("List:", numbers)
print("Max:", maximum)
print("Min:", minimum)
