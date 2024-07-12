class Method:
    def __init__ (self,argument):
        self.attribute=argument
    def __add__(self,object1):
        return self.attribute+object1.attribute
class Method_2:
    def __init__ (self,argument):
        self.attribute=argument
    def __add__(self,object1):
        return self.attribute+object1.attribute        
instance_1=Method("Attribute")
print(instance_1)
instance_2=Method_2("27")  
print(instance_2)
print(instance_2+instance_1)  
