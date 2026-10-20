def display():
    print("Inside the display function")
display()

print("function with (positional argument)")
def add(num1,num2):
    return num1+num2
addition=add(10,20)
print('Addition:',addition)

print("function with (keyword argument)")
name=input('Enter your name:')
age=input("Enter age:")
def user_info(name,age):
    print('Name:',name)
    print('Age:',age)
user_info(name,age)
user_info(name,age=20)

print("function with (variable length argument)")
def emp_info(*name,dept):
    print("name:",name)
    print("department:",dept)

emp_info("pranav","harsh",dept="sales")