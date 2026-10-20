class Student:
    def __init__(self,name,rno,course):
        self.name=name
        self.rno=rno
        self.course=course
        
    def display(self):
        print("Student Info")
        print("Name:",self.name)
        print("Roll No:",self.rno)
        print("Course:",self.course)
        

s1=Student("Pranav",101,"MCA")
s1.display()