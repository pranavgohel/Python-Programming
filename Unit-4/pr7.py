class Product:
    def __init__(self, name):
        self.name = name

class Digitalitem:
    def delivery_type(self):
        return "Instant Download"

class EBook(Product, Digitalitem):
    def __init__(self, name, pages):
        super().__init__(name)
        self.pages = pages

    def __str__(self):
        return f"E-Book: '{self.name}' with {self.pages} pages"

    def __len__(self):
        return self.pages


print("--- MRO (Method Resolution Order) ---")
print(EBook.__mro__)

print("\n--- Magic Methods in Action ---")
my_book = EBook("Python Mastery", 300)

print(my_book)
print(len(my_book))