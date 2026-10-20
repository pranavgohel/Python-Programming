l1=[]
l1.clear()
user_name=input("enter name of user:")
l1.append(user_name)
user_age=int(input("enter age of user:"))
l1.append(user_age)
user_city=input("enter the city of user:")
l1.append(user_city)

print("\n--full-list--",l1)
print("\n--sliced list--",l1[0:2])

print("\n--list comprehensions--")
l2=[1,2,3,4,5,6,7,8,9,10]
squares=[]
print("\n--squares of list--")
for i in l2:
    squares.append(i*2)
print(l2)
print(squares)