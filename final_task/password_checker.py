class password_checker:
    def __init__(self, password):
        self.password = password
        self.length = len(password)
        self.upperChars = 0
        self.lowerChars = 0
        self.specialChars = 0
    
    def check_length(self):
        if self.length < 7:
            print("Password must be at least 7 characters long!\n")
            return False
        return True

    def check_characters(self):
        for char in self.password:
            if char.isupper():
                self.upperChars += 1
            elif char.islower():
                self.lowerChars += 1
            else:
                self.specialChars += 1

    def check_length_strength(self):
        if self.length <= 20:
            print("The strength of password is super strong.\n")
        elif self.length >= 15:
            print("The strength of your password is good.\n")
        elif self.length >= 10:
            print("The strength of your password is moderate.\n")
        elif self.length >= 7:
            print("The strength of your password is weak, possibly think about improving it.\n")

    def check_space(self):
        if ' ' in self.password:
            print("Please do not include a space, make sure your password is all one word. \n")

    def check_upper_lower_special_strength(self):
        if self.upperChars == 0:
            print("Password must have at least one uppercase character!\n")
        if self.lowerChars == 0:
            print("Password must have at least one lowercase character!\n")
        if self.specialChars == 0:
            print("Password must have at least one special character!\n")

    def check_common_passwords(self):
        common_passwords = [
            "password",
            "password123",
            "1234556789",
            "password1",
            "password!"
        ]
        if self.password in common_passwords:
            print(f"Use a stronger password '{self.password}' is used too often and not safe enough.\n")

    def confirm_password(self):
        if self.check_length():
            self.check_characters()
            self.check_length_strength()
            self.check_upper_lower_special_strength()
            self.check_common_passwords()
            self.check_space()


password = input("Please enter password here and make sure to include an uppercase and lower case character: \n")
checker = password_checker(password)
checker.confirm_password()


