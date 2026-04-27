#  multiple inheritance 
# muktiple inheritance means more than one parent in the chain and single child will be there and that child acquires attrib and methods from both parents


class A:
    clName="ParentA"

    def __init__(self):
        print("init method of A class")

    def a(self):
        print("a defined method in A class")

    def height(self):
        print(5.6)        

class B:
    clName="ParentB"

    def __init__(self):
        print("init method of B class")

    def b(self):
        print("b defined method in B class")  

    def height(self):
        print(5.2)       
    

class C(A,B):
    clName="childC"

    def __init__(self,name,age):
        self.n=name
        self.a=age
        print("init method of C class")

    def c(self):
        print("c defined method in C class")  
        print(A.clName) # parentA 
        super().a() #a defined method in A class
        super().b() # b defined method in B class
        print(B.clName) #parentB
        B.height(self)
    
o=C("srilekha",29)  # object creation
o1=C("vamsi",27)
o.c()           

# is it possible to create multiple objects for a single class ?