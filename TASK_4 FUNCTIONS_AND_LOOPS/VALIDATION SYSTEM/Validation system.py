def validate_recharge():
    valid_plans = [199, 299, 399, 599]

    while True:
        amount = int(input("Enter recharge amount: ₹"))

        if amount < 50:
            print("Recharge amount must be at least ₹50.")
            continue

        if amount not in valid_plans:
            print("Invalid plan selected. Valid plans are:", valid_plans)
            continue

        print("Recharge successful!")
        break

validate_recharge()
