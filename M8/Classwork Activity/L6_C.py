class Student:
    def __init__(self,score):
        self.score = score
    
    def __add__(self, other):
        return self.score + other.score
    
    def __eq__(self, other):
        return self.score == other.score
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score
    
stu1=Student(50)
stu2=Student(60)
print(stu1 + stu2)
print(stu1 == stu2)
print(stu1 < stu2)
print(stu1 > stu2)
