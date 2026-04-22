
# # a=100
# # b="hyd"
# # c=22.5
# # def xyz():
# #     a="10000coders"
# #     print(a)
# # xyz()
# # print(b*a)    
# # print(c)



# # scope 
# # the ability to access a spec variable in specific area is called as scope 


# abcdef=100 #gloabl scoped variable
# dfg=10
# print(abcdef)
# def a(): # a function area lopala we are able to access that b var in entire funct code
#     b=100 # b is function area accessable variable
#     #function variable
#     #function scoped variable
#     print(b)
#     print("vamsi")
#     print("vamsi")
#     print("vamsi")
#     print(b)
#     print(b)
#     c=20
#     print("vamsi")
#     print("vamsi")
#     print("vamsi") 
#     print(c)
#     d=0
# a()    
# print(abcdef)


lexical scoping :-- going to upper parent memory for variable
scope chaining :-- finding var is prsnt in memeory r not

a=10 # global scoped varaible
def abc():
    a="vamsi" #abc func scoped variable
    xyz=100
    print(xyz)
    print(a)
    def mno():
        c=20 #mno func scoped variable
        print(c)
        print(a)
        # print(xyz)
    mno()    
abc()