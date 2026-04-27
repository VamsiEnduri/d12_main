# heirarchial inhertance 
# single parent -> multiple childs 
class P:
    clName="ParentP"

    def __init__(self):
        print("init method of P class")

    def a(self):
        print("a defined method in P class")

    def height(self):
        print(5.6) 

class C1(P):
    def __init__(self):
        super().a()
        super().height()
o=C1()

class C2(P):
    def __init__(self):
        super().a()
        super().height()

o=C2()
