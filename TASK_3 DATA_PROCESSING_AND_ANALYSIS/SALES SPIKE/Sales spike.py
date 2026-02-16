sales = [1200, 1500, 900, 2200, 1400, 3000]

average_sales = sum(sales) / len(sales)

threshold = average_sales * 1.30

for index, value in enumerate(sales):
    if value > threshold:
        print(f"Day {index + 1}: {value}")
