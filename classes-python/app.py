from student import Student
from school import School


students = [Student("Juan"), Student("Maria"), Student("Pedro")]


Pueri   = School("Pueri")
Pueri.add_multiple_students(students)
Pueri.print_students()