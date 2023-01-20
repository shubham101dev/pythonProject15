# class Number:
#     def sum(self):
#         return self.a+self.b
# num1=Number()
# num1.a=10
# num1.b=15
# c=num1.sum()
# print(c)
# class Company:
#     name="google"
#     def info(self,sign):
#         print(f"salary is 100k{self.name},{self.age},{sign}")
#     @staticmethod
#     def greet():
#         print("good morning sir")
# a=Company()
# sign="thanks"
# a.age=25
# a.address="pune"
# a.info(sign)
# a.greet()

# import time
# time=time.time()
# class Employee:
#     name="google"
#     def info(self,sign):
#         print(f"{self.name}{self.age},,{sign}")
#
#     @staticmethod
#     def greet():
#         print("good morning sir")
#     @staticmethod
#     def time():
#         print(f"{time}")
#
# a=Employee()
#
# a.age=25
# a.info("thanks")
# a.greet()
# a.time()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person("John", 30)
# p2 = Person("Alice", 25)
#
# print(p1.name)  # prints "John"
# print(p2.name)  # prints "Alice"
# print(p1.age)  # prints 30
# print(p2.age)  # prints 25
# p1.name="shubham"
# print(p1.name)

##init
# class Employee:
#     company="youtube"
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         print("thank you")
#     @staticmethod
#     def greet():
#         print("good morning sir")
#     def info(self):
#         print(f"employee name is{self.name}")
#         print(f"employee age is{self.age}")
#         print(f"employee salary is{self.salary}")
# a=Employee("shubham",25,5000)
# # a.greet()
# # a.info()



# class Employee:
#     def __init__(self):
#         print("thank you")
# a=Employee()

# class Programmer:
#     company="microsof"
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         print(self.name)
#         print(self.age)
#         print(self.salary)
#
# name=input('enter u name')
# salary=input('enter your salary')
# age=input('enter your age')
# a=Programmer(name, age, salary)

# class Programmer:
#     company="microsoft"
#     def info(self):
#      print(f"{self.name}{self.salary}{self.age}{self.company}")
# a=Programmer()
# a.name="shubham"
# a.salary=5000
# a.age=25
# a.info()


# class Programmer:
#     company="microsoft"
#     def info(self,age):
#      print(f"{self.name}{self.salary}{age}{self.company}")
# a=Programmer()
# a.name="shubham"
# a.salary=5000
# age=25
# a.info(age)

# square
# squareroot
# cube

class Calculator:
    def __init__(self,num):
        self.number=num
    def squareroot(self):
        print(f"{self.number**0.5}")
    def square(self):
        print(f"{self.number * self.number}")
    def cube(self):
        print(f"{self.number * self.number * self.number}")

n=int(input("enter a number"))
a=Calculator(n)
a.cube()
# a.squareroot()
# a.square()






