user_name=input("Enter User name:")
user_pass=int(input("Enter Password"))

if user_pass == 1234:
    print("Login successfully....")

    print("Enter marks between 1-100")
    sub1=int(input("Enter Python marks:"))
    sub2=int(input("Enter AI/ML marks:"))
    sub3=int(input("Enter DBMS marks:"))
    sub4=int(input("Enter OS marks:"))
    
    total_marks=sub1+sub2+sub3+sub4
    per=(total_marks/400)*100
    
    print(f"{per}%") 
    if per<35:
        print(f"{user_name} failed in exam")
    elif per>35 and per<=50:
        print(f"{user_name} got 'D Grade' in exam")
    elif per>50 and per<=70:
        print(f"{user_name} got 'C Grade' in exam")
    elif per>70 and per<=80:
        print(f"{user_name} got 'B Grade' in exam")
    elif per>80 and per<=90:
        print(f"{user_name} got 'A Grade' in exam")
    elif per>90 and per<=100:
        print(f"{user_name} got 'A+ Grade' in exam")
    else:
        print("Invalid error")
else:
    print("Invalid password")