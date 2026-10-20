import shutil
import os

with open("./original.txt", "w") as file:
    file.write("Hello using shutil!")

shutil.copy("./original.txt", "./copied.txt")
print("File copied to 'copied.txt'")

shutil.move("./original.txt", "./moved.txt")
print("File moved and renamed to 'moved.txt'")

os.remove("./copied.txt")
os.remove("./moved.txt")
print("Files Deleted Successfully!")