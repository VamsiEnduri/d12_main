# a=10
# print(type(a))

# import math
# print(type(math))

# def abc():
#     pass

# print(type(abc))


# class syntax "-- "

# class Cl_name: # defining blueprint
#     #code
#     # varaibles
#     # functions / methods

# Cl_name() # object creation


class Student:
    abc=10 #class var 
    xyz="vamsi" # class var

    def __init__(self,n,a,c,l): # default method  default constructor method
        # print(n,a,c,l)
        self.name = n
        print(self,"28")

    def studentDetails___(self,n,a): # defined method
        print(n,a)

    def collegeDetails(self): #  defined method
        cName="10000Coders" # local var
        loc="Hyd" # local var
        print(cName,loc)    

o=Student("vamsi",27,"10000Coders","Hyd") #creating obj
o.studentDetails___("ravi",27)
o.collegeDetails()
