class Student:
  grade = int()
  
  def __init__(self, name: str):
    self.name = name
    self.grade = int(10)
        
  def say_hello(self):
    print("Hello my name is " + self.name)
    
    
  def increase_grade(self, num:int):
    self.grade = self.grade + num
    print(f"My grade is now {self.grade}")
    