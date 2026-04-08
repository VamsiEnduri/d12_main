# # # function ""
# # def fn_name(): #defining a function / creating function
# #     #block code to execute
# # fn_name() #calling / invoke
# # fn_name()
# # fn_name()


# # def add():
# #     a=10
# #     b=20
# #     print(a+b)
# # add()    

# # def mul():
# #     a=10
# #     b=2
# #     print(a*b)
# # mul()       



# # register dashboard
# def register():
#     n=input("enter name here :--- ")
#     e=input("enter email here :--  ")
#     p=input("enter password :-- ")
#     cp=input("enter cp passwpord :--   ")

#     if p == cp :
#         print("resgistration successful......")
#     else:
#         print("p and cp doesnt matched") 
# # register()           
# # login


# def login():
#     er="vamsi@gmail.com"
#     pr="12345678"
#     e=input("enter email here :--  ")
#     p=input("enter password :-- ")

#     if e == er and p == pr :
#         print("login successful")
#         dashboard()
#     else:
#         print("invalid credentails")
# login()            


# # dashboard access

# def dashboard():
#     print("welocme to dashboard")


def dashboard():
    print("welocme to dashboard")
    dashboard()



def login():
    er="vamsi@gmail.com"
    pr="12345678"
    e=input("enter email here :--  ")
    p=input("enter password :-- ")

    if e == er and p == pr :
        print("login successful")
        dashboard()
    else:
        print("invalid credentails")
           
login() 