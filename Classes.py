# classes is a part of the object orientated programming
# key concepts:
# class - a blueprint - of attrubes (vars/args) and methods (functions) object.method 
# use class against an object
# object is an instance of the class
# allows us to easily make multiple objects of the same type.
# Classes need to be a capital letter
# methods (def speak) tha only can all
# needs to create an object of the class

class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    
    def my_method(self):
        return self.attribute1 + self.attribute2

obj1 = MyClass(10, 20)
obj2 = MyClass(30, 40)

print(obj1.attribute1)
print(obj2.attribute2)
print(obj1.my_method())
print(obj2.my_method())


class Dog: # class name start with a capitol. 
    energy = "high" # setting an attribute to the class

    def speak(self):# refers to the object we build
        print("bark")

fido = Dog() # makes an object called fido of the dog class

fido.speak()

fido.energy

class Students:
    pass

student1 = Students()
student2 = Students()

student1.first = "john"
student1.last = "smith"
student1.age = "10"

print(student1.age, student1.first)

class Student: 
    def __init__(x, first, last, age):
        x.first = first #the x parameter (self) referes to the object self.
        x.last = last # x maps the class data to the object
        x.age = age
    
    #__init__ method is called a dunder backgrond task and python is doing something for us. x can be anything. init method initialises the object (x) with the attributes

student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.age, student2.age)


class Student: 
    def __init__(x, first, last, age):
        x.first = first
        x.last = last
        x.age = age
        x.full = first + " " + last

student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.full, student2.full)

class Student: 
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # self.full = first + " " + last

    def fullname(self): #object calls full name. 
          return(self.first + " " + self.last)

student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.fullname())
print(Student.fullname(student2))#this is an argument

# change an attribute with a method

class Student: 
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        # self.full = first + " " + last

    def fullname(self): #object calls full name. 
          return(self.first + " " + self.last)

    def change_age (self) #change age function
        self.age + int(self.age + 1)


student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.age, student2.age)
# this is the object 
student1.change_age()
Student.change_age(student2)

# making a self class variable

class Student: 

    age_increase_amount = 25 #put variables at the top in a class. This means 

    def __init__(self, first, last, age): #functions
        self.first = first
        self.last = last
        self.age = age
       

    def fullname(self): #object calls full name. 
          return(self.first + " " + self.last)

    def change_age (self) #change age function
        self.age + int(self.age + self.age_increase_amount)


student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)

print(student1.age)
student1.change_age
print(student1.age)

print(student1.age_increase_amount)
print(student2.age_increase_amount)

# __dict___

print(student1.__dict__)
print(Student.__dict__) # will return first, hohn, last, smith, age, 35. 

#change to variable

student1.age_increase_amount = 20
print(student1.__dict__) # this then prints back ge increase amount into variable but doesnt for student 2, has to be outside of hte functions


# non-self class variable



# creating a counter 

class Student: 

    age_increase_amount = 25 #put variables at the top in a class. referenced through the object
    num_of_students = 0 # referenced through the class

    def __init__(self, first, last, age): #functions
        self.first = first
        self.last = last
        self.age = age

        Student.num_of_students
       

    def fullname(self): #object calls full name. 
          return(self.first + " " + self.last)

    def change_age (self) #change age function
        self.age + int(self.age + self.age_increase_amount)


print(Student.num_of_students)
student1 = Student("john", "smith", 10)
student2 = Student("katy", "smith", 12)
print(Student.num_of_students)


# parent - child classes

class Animal: 
    def __init__(self#(object)# mname, species):
        self.name = name # map
        self.species = species 
# mehtod
    def eat(self):
        print(f"{self.name} is eating.")

        ## now child class. super is refering to the parent class. super class of these classes(the one above it) calling something from parent class.

class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
# this is a method just for the cat class
    def meow(self):
        print("meow"
my_cat = Cat("w", "t", "i" ))
 #string method, printing the object of hte class 
 
my_cat.meow()
my_cat.eat()


class Animal: 
    def __init__(self, name, species, breed):
        self.name = name # map
        self.species = species 
# mehtod
    def eat(self):
        print(f"{self.name} is eating.")
   def__str__(self):
            return f"{self.name} - {self.species} - {self.__class__.__name__}"
        ## now child class. super is refering to the parent class. super class of these classes(the one above it) calling something from parent class.

class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
# this is a method just for the cat class
    def meow(self):
        print("meow"

def __str__(self):
    return super().__str__() + f" - {self.breed}"

my_cat = Cat("w", "t", "i" ))
 #string method, printing the object of hte class 
 
my_cat.meow()
my_cat.eat()

what we need to do
classes lab: 

# leading underscore for python key words
# 400p principles in the learner guide


# Create a rectangle class with attributes length and width. Add methods to calculate the area and perimeter of the rectangle.

write class
define init

class Rectangle:
    de__init__(self,length, width):
        selflegnth
        self.width

# create an object and pass through length and witdth
rect = Rectangle(5,10)
print(rect.area())

class Recatangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Recatangle(5, 10)
print(rect.area())


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

 class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year





class Students:                #default values
    def __init__(self, name, age, class_="maths"):
        self.name = name
        self.age = age
        self.class_ = class_

        def average_test_score(self, scores): #object calls full name. 
          total_score = sum(scores)
          average_percentage = total_score / (len(scores) * 100) * 100
          return f"{self.name} - average test score is {average_percentage}"

student_1 = Students("john", 18)

print(student_1.average_test_score([40, 60, 80]))

class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with wingspan of {self.wingspan} cm")

    def __str__(self):
        return f"{self.name} {self.__class__.__name__}, {id(self)}, {self.__dict__}"

class Owl(Bird):
    nocturnal = True
    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)

    def speak(self):
        print(f"{self.name} hoots")

    def __str__(self):
        return super().__str__() + f"- nocturnal: {self.nocturnal}"

class Dodo(Bird)
        exti = True
    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)


mostof it can go in a method in a class.
