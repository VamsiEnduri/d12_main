# class A:
#     def __init__(self,*x):# method overloading with *arg
#         print(x)
#         print("init method")

# o=A(1,2)  # 2 args     
# o1=A(1,2,3,4,5)  # 5 args 
# o2=A(1,2,3,4,5,6,7,8,9,10)

# *arg :-- varaible length args


# method overriding
class Animal:
    a=10
    def __init__(self):# method overloading with *arg
        print("init method")

    def sound(self):
        print("every animal has its own sound making")    

class Dog(Animal) :
    def __init__(self):
        print("animal init method")

    def sound(self):
        print("bow bow")

o=Dog()
o.sound()
