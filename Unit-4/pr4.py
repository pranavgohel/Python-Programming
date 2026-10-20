class Car:
    brand_name = "AUDI"
    total_cars_manufactured = 0

    def __init__(self, color):
        self.color = color
        Car.total_cars_manufactured += 1

    def display(self):
        print("\nCar info")
        print("Name:",self.brand_name)
        print("Color:",self.color)

    @classmethod
    def change_brand_name(cls, new_name):
        cls.brand_name = new_name
        print(f"Factory Update: All cars are now branded as '{cls.brand_name}'.")

    @staticmethod
    def is_speeding(current_speed, speed_limit):
        return current_speed > speed_limit


mycar=Car("black")
mycar1=Car("blue")
print("--- 1. Testing Instance Methods ---")
mycar.display()
mycar1.display()

print("\n--- 2. Testing Static Methods ---")
warning = Car.is_speeding(85, 90)
print(f"Is the driver speeding? {warning}")

print("\n--- 3. Testing Class Methods ---")
Car.change_brand_name("BMW")
print(f"\nTotal cars made by factory: {Car.total_cars_manufactured}")

mycar.display()
mycar1.display()