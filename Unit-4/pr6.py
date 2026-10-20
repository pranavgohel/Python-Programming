class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks: Woof!")
class Cat(Animal):
    def speak(self):
        print("Cat meows")

    
animal1=Animal()
animal1.speak()

animal2=Dog()
animal2.speak()

animal3=Cat()
animal3.speak()