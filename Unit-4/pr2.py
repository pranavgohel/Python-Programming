class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: wooof!")
        
    def bark2(self):
        print(f"{self.name} says: foow!")

dog1 = Dog("chihuahua", 3)
dog1.bark()

dog2 = Dog("German Shepard",5)
dog2.bark2()