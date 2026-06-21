password = input("Enter password: ")

has_upper = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True

    if ch.isdigit():
        has_digit = True

    if ch in "!@#$%^&*":
        has_special = True

if len(password) >= 8 and has_upper and has_digit and has_special:
    print("Password accepted!")
else:
    print("Password rejected!")