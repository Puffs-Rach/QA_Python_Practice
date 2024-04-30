

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_details(self):
        return f"The car is a {self.year}, {self.make}, {self.model}."

car1 = Car('Toyota', 'Corolla', 2018)
car2 = Car('Honda', 'Civic', 2019)

print(car1.get_details())  # Output: The car is a 2018 Toyota Corolla.
print(car2.get_details())  # Output: The car is a 2019 Honda Civic.