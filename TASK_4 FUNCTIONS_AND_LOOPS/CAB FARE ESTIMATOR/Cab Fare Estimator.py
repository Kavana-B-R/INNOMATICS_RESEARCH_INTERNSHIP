def calculate_fare(distance, peak):
    base_fare = 50
    fare = base_fare + (12 * distance)

    if peak:
        fare += fare * 0.25  # 25% extra

    return fare


def cab_fare_system():
    while True:
        distance = float(input("Enter distance in km: "))
        peak_input = input("Is it peak hour? (yes/no): ").lower()

        peak = True if peak_input == "yes" else False

        total_fare = calculate_fare(distance, peak)
        print("Total Fare: ₹", total_fare)

        retry = input("Do you want to calculate again? (yes/no): ").lower()
        if retry != "yes":
            break

cab_fare_system()
