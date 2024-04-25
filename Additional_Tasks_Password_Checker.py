def check_password():
    common_passwords = [
        "password",
        "password123",
        "1234556789"
    ]

    user_password = input("What is your password? ")

    if user_password in common_passwords:
        print(f"Use a stronger password '{user_password}' is not safe enough.")
    else:
        print("Password is strong.")

check_password()
