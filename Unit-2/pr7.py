lst=[10,20,30,40]
lst_square=[i**2 for i in lst]
print(" li (square)",lst_square)

d1_cubes={i:i**3 for i in lst}
print(" dict comprehensions (cubes)",d1_cubes)

s1_modulo3={i % 3 for i in lst}
print(" set comprehensions (reminders modulo 3)",s1_modulo3)