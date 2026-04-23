class A:
    clName="A" # class variable

    def __init__(self): # def method
        self.name="srinu" # instance varaible
        print("a class init method")

    def height_A(self): # instance #instance varaibles
        self.height=5.6 # instance variables
        print(self.height)

    def land_A(self):
        self.land="2acre"
        print(self.land) 


class B(A):
    clName="B"

    def __init__(self):
        print("b class init method") 

    def acquireChars(self):
        print("acquireChars method")  
        print(super().clName) # acquiring r accessing r using parent class attr
        super().height_A()  #acquiring r accessing r using parent class defined method :-- using :-- 
        super().height_A() # :-- reusability
        super().land_A()

    def bmethod(self):
        print("b is parent for c and b is child for a")    

class C(B):
    clName="C"

    def __init__(self):
        print("c class init method")

    def acquireChars_C(self):
        xyz=super().clName 
        print(xyz)
        super().acquireChars()   
        super().bmethod()

o=C()     # init call   
print(o.clName)
o.acquireChars_C()