n=int(input("Enter number to get "))

def fact(n):
    if(n<0):
        return
    if(n<2):
        return 1
    return n*fact(n-1)
factorial=fact(n)
print(factorial)

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return fibonacci(n - 1) + fibonacci(n - 2)

terms = 9
for i in range(terms):
   print(fibonacci(i), end=" ")