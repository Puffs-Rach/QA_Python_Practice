# A class is a blueprint for creating objects (also known as instances). It defines the attributes (data) and methods (functions) that the objects will have.
# Create a BankAccount class with attributes account_number and balance. Add methods to deposit and withdraw money from the account.

class BankAccount:
    def __init__(self, account_number, balance):
        balance = 0
        self.account_number = account_number
        self.balance = balance

    def deposit(self, ):
        return self.length * self.width

    def withdrawing(self):
        return 2 * (self.length + self.width)

# create an instance of the bankAccount class
account = BankAccount("234567", 1056)
print(account.deposit(500))
print(account.withdrawing(250))

#Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes. 

# This line starts the definition of a new class named Car.
class Car:
    #This is a special method called the constructor (__init__) which initializes new instances of the class. It takes 
    # four parameters: self (a reference to the current instance of the class) and three attributes: make, model, and year. 
    # Inside the constructor, it assigns the values passed as arguments to the corresponding attributes of the instance.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    #This is a method named get_details defined within the Car class.
    #It takes one parameter, self, which refers to the current instance of the class.
    #Inside the method, it returns a formatted string representing the details of the car, including its make, model, and year.
    def get_details(self):
        return f"The car is a {self.year}, {self.make}, {self.model}."
# create two objects instances of the Car class, named car1 and car2, respectively.
# They pass arguments to the constructor (__init__) to initialize the attributes make, model, and year of each instance.
car1 = Car('Toyota', 'Corolla', 2018)
car2 = Car('Honda', 'Civic', 2019)
# These lines call the get_details method on each instance of the Car class (car1 and car2).
# They print the return value of the method, which is a formatted string representing the details of each car.
print(car1.get_details())  # Output: The car is a 2018 Toyota Corolla.
print(car2.get_details())  # Output: The car is a 2019 Honda Civic.


#Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        def calculate_total_value(self):
            return self.price * self.quantity