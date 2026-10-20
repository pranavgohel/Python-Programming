print("\n--------------------------")
print("\n---Multiple Inheritance---")
# Multiple Inheritance
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

class SalaryManager:
    def calculate_total(self, base_pay, bonus):
        self.total_pay = base_pay + bonus
        print(f"Total compensation calculated: {self.total_pay}")

class LeaveManager:
    def request_leave(self, days):
        print(f"Leave requested for {days} days.")

class Developer(Employee, SalaryManager, LeaveManager):
    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Total Pay: {self.total_pay}")

dev1 = Developer("E102", "Pranav")
dev1.calculate_total(75000, 10000)
dev1.request_leave(3)
dev1.show_details()

print("\n--------------------------")
print("\n--Multilevel Inheritance--")
# Multilevel Inheritance
class Animal:
    def eat(self):
        print("This animal eats food.")

class Mammal(Animal):
    def walk(self):
        print("This mammal walks on land.")

class Dog(Mammal):
    def bark(self):
        print("The dog barks.")

my_dog = Dog()
my_dog.eat()
my_dog.walk()
my_dog.bark()

print("\n--------------------------")
print("\n----Single Inheritance----")
# single Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} engine started.")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} is now driving.")

my_car = Car("BMW M4")
my_car.start()
my_car.drive()