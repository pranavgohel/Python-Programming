def counter_up_to(maxv):
    count=1
    while count <= maxv:
        yield count
        count+=1
counter=counter_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))