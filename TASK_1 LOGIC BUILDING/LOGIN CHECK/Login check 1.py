
username = "admin"
password = "1234"

input_username = input("Enter Username: ")
input_password = input("Enter Password: ")

if input_username == username and input_password == password:
    print("Login Successful")
else:
    print("Invalid Credentials")
