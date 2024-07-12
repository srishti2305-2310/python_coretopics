class Method:
    def __init__(self,attribute):
        self.attribute=attribute
    def __contains__(self,attribute):
        return attribute in self.attribute
instance=Method([4,6,8,9,1,6])
print("4 is contained in""attribute"":",4 in instance)
print("5 is contained in""attribute"":",5 in instance)      