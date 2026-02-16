sensor_readings = [3, 4, 7, 8, 10, 12, 5]

valid_readings = []

for index, value in enumerate(sensor_readings):

    if value % 2 == 0:
        valid_readings.append((index, value))

print("Valid Sensor Readings (Hour, Value):")
print(valid_readings)
