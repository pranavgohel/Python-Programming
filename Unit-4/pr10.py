with open("./data.txt", "r") as file:
    print("Starting Position of pointer:", file.tell())

    print("Read data:", file.read(32))

    print("Pointer after reading:", file.tell())

    file.seek(15)
    print("Pointer position after using seek(15):", file.tell())