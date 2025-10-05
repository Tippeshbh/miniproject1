class student:
    def __init__(self,roll_no,name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = {}

    def get_marks(self):
        return self.__marks    

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks  

    def calculate_average(self):
        total = 0
        for mark in self.__marks.values():
            total += mark
        average =total/len(self.__marks)
        return average

    def is_passed(self):
        is_failed = any(mark<=35 for mark in self.__marks.values())
        if is_failed:
            print(f"{self.name} has failed")
        else:
            print(f"{self.name} has passed")    

    def calculate_grade(self):
        print("grade: ", end=" ")
        percentage = self.calculate_average()      
        if percentage >= 90:
          print("A")
        elif 60 <= percentage < 90:
          print("B")
        elif 45 <= percentage < 60:
         print("C")
        else:
          print("D")

class ReportCard:
    def generate(self, student:student):
        student_marks = student.get_marks()
        print(f"Name: {student.name} \t Roll No. {student.roll_no}")
        print("-----Marks-------")
        for subject, marks in student_marks.items():
            print(f"{subject} - {marks}")
        print("-----------")
        print(f"Average: {student.calculate_average()}")    
        student.is_passed()
        student.calculate_grade()
class ClassRoom:
    def __init__(self, grade,section):
        self.grade =grade
        self.section = section
        self.__students =[]

    def add_student(self, student):
        self.__students.append(student) 

    def calculate_class_average(self):
        pass

    def get_student_list(self):
        for student in self.__students:
            print(f"{student.roll_no}.{student.name}")
                                 
a = student(1, "Akash")        
a.add_marks("math",65)
a.add_marks("science",34)

report = ReportCard()
report.generate(a)       


c = ClassRoom("10", "B")

c.add_student(a)
b = student(2, "Bharat")
c.add_student(b)
c.get_student_list()
