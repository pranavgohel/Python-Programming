class Student:
    school_name="Marwadi university"
    
    def __init__(self,student_name,student_id):
        self.student_name=student_name
        self.student_id=student_id
        
    def display(self):
        print("Student Info")
        print("ID:",self.student_id)
        print("Name:",self.student_name)
        
        
print("Class variable access using class :",Student.school_name)

student1=Student("Pranav",101)
student2=Student("Hum",102)

student1.display()
student2.display()