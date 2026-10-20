import regex

print("----------Regex Module----------")
str=input("Enter a string: ")
print("The string is:",str)
print("The string after removing all the digits is:",regex.sub(r'\d','',str))
print("The string after removing all the special characters is:",regex.sub(r'[^a-zA-Z0-9]','',str))