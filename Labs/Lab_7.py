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
