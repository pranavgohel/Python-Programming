num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))

print("\n-------Arithmetic operations-------")
print(f"sum of {num1} and {num2} is ",num1+num2)
print(f"sub of {num1} and {num2} is ",num1-num2)
print(f"mul of {num1} and {num2} is ",num1*num2)
print(f"div of {num1} and {num2} is ",num1/num2)

print("\n-------Relational operations-------")
print(f"{num1} is greater than {num2} =",num1>num2)
print(f"{num2} is greater than {num1} =",num1<num2)

print("\n-------Logical operations-------")
print(f"{num1} is greater than {num2} and {num1} is greater than {num3} = {num1 > num2 and num1 > num3}")
print(f"{num1} is greater than {num2} or {num1} is greater than {num3} = {num1 < num2 or num1 > num3}")