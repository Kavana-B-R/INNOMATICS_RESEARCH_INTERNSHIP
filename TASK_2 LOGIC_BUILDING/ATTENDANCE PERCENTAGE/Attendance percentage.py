attendance = ["P", "P", "A", "P", "P"]

present_count = attendance.count("P")

percentage = (present_count / len(attendance)) * 100

print("Attendance Percentage:", percentage)
