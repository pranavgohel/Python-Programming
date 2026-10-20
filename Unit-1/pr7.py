user_info={}

user_name=input("Enter the name of user")
user_age=int(input("enter age of user:"))
user_city=input("enter the city of user:")
user_info['Name']=user_name
user_info['age']=user_age
user_info['City']=user_city
print("full dictionary : ",user_info)

print("\nKeys : ",user_info.keys())
print("\nAfter pop :",user_info.pop('Name'))

print("After clear :",user_info.clear())
