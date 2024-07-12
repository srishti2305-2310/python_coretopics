class methods():
    def __init__ (self,*args):
        print("init magic method")
        self.name=args[0]
        self.std=args[1]
        self.marks=args[2]
Student=methods("monika",11,98)
print(Student)
print("name,standard,and marks of the students is:\n",Student.name,"\n",Student.std,"\n",Student.marks)        