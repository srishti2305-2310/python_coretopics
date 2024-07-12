class Method(object):
    def __new__ (cls):
        print("new magic method")
        return super(Method,cls).__new__(cls)
    def __init__ (self):
        print("init method is called here")
Method()        