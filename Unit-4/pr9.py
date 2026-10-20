with open("./data.txt", "w") as file:
    file.write("1. Welcome to Marwadi University!\n")

with open("./data.txt", "a") as file:
    file.write("2. The department of FOCA.\n")

with open("./data.txt", "r") as file:
    content = file.read()

print("== File Content ==")
print(content)