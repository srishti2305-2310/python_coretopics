class Method:
    def __init__(self,start_value,stop_value):
        self.start=start_value
        self.stop=stop_value
    def __iter__(self):
        for num in range(self.start,self.stop+1):
            yield num**2
instance=iter(Method(3,8))
print(next(instance))
print(next(instance))  
print(next(instance))
print(next(instance))
print(next(instance))
print(next(instance))              