class Method:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __repr__(self):
        return f"value of the attributeof the class method:\nx={self.x}\ny={self.y}\nz={self.z}"
instance=Method(4,6,2)
print(instance)        
