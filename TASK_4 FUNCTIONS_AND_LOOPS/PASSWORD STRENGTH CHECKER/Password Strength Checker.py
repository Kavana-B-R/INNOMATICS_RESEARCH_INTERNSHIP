def check_password_strength(password):
    has_digit = False
    has_special = False
    special_chars = "@#$"

    if len(password) < 8:
        return "Weak Password (Minimum 8 characters required)"

    for char in password:
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True

    if has_digit and has_special:
        return "Strong Password"
    else:
        return "Weak Password (Must contain at least one digit and one special character @#$)"

pwd = input("Enter password: ")
print(check_password_strength(pwd))
