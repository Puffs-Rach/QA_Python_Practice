Final Task notes to self

# write an application that checks the strength of a password.
# Requirements:
# 
# Write a class that has a method that checks the password strength.
# Use factors like length, upper/lower case and if it has a number and special character.
# ratings should be very weak - weak - moderate - strong - very strong 
# Check against a list of common passwords 10-20 common password = very weak
# User input that loops until the user quits

checking weak passwords

counter, go through and is it over a certain length do a plus one, upper lower case plus one and two. Levels then saying if its
elif or ifs

if password contains = very strong 

just do it in if statements 
user input loops until theuser quits


input for password

then logic. how to give it a rating. 



def check_password():
    common_passwords = [
        "password",
        "password123",
        "1234556789",
        "password1",
        "password!"
    ]

    user_password = input("What is your password? ")

    if user_password in common_passwords:
        print(f"Use a stronger password '{user_password}' is not safe enough.")
    else:
        print("Password is strong.")

check_password()

password = input("")



length = len(password)
    if (length < 7):
        print("Password must be at least 7 characters long!\n")
    else:
        for x in range(0, length):
            if (x.isupper())
                upperChars +- 1



class PasswordChecker:
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
        if self.length >= 20:
            print("The strength of password is super strong.\n")
        elif self.length >= 15:
            print("The strength of your password is strongish.\n")
        elif self.length >= 10:
            print("The strength of your password is moderate.\n")
        elif self.length >= 7:
            print("The strength of your password is weak.")

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
            print(f"Use a stronger password '{self.password}' is used too often and not safe enough.")

    def confirm_password(self):
        if self.check_length():
            self.check_characters()
            self.check_length_strength()
            self.check_upper_lower_special_strength()
            self.check_common_passwords()


password = input("Please enter password here: ")
checker = PasswordChecker(password)
checker.confirm_password()


# current output issues: outputing all of them??
# 


