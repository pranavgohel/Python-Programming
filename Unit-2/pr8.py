g_var="global variable"

def display():
    l_var="local variable"
    print("inside function")
    print("printing local variable",l_var)
display()
print("outside the function")
print("printing global variable",g_var)

def outer():
    count=0

    def inner():
        nonlocal count  # Refers to 'count' in outer()
        count+=1
        print("Inner count:",count)

    inner()
    inner()
    print("Outer count:",count)

outer()
