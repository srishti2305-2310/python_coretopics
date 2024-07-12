class Method:
    def __init__(self,a):
        self.a=a
    def __call__(self,number):
        return self.a*number
instance=Method(7)
print(instance.a)
print(instance(5))       