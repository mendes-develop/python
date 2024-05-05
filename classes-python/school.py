from student import Student

class School:
  def __init__(self, name):
    self.name: str = name
    self.students: list[Student] = []

  def add_student(self, student: Student):
    self.students.append(student)
    
  def add_multiple_students(self, students: list[Student]):
    self.students.extend(students)

  def print_students(self):
    for student in self.students:
      print(student.name)
      # return student.name