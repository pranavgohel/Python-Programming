l1=[10,13,17,20,30,40,50,60,70,80,90,100]

print
for i in l1:
    if(i%2==0):
        continue
    if(i==30):
        pass
    if(i==80):
        break;
    print(i)