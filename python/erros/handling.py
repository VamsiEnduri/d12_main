# try:
#     a=10
#     b="vamsi"+b
#     c=a/b
#     print(c)
# except :
#     print("issue with conating the int + str")


# print("vamsi")        
# print("vamsi")        
# print("vamsi")        
# print("vamsi")        
# print("vamsi")        
# print("vamsi")        
# print("vamsi")        
# print("vamsi")        


# # a=10
# # b=0
# # c=a/b
# # print(c)


try :
    a=10
    b="vamsi"+"aa"
    c=a/10
    d={"id":1}
    print(d["id"])
except TypeError:
    print("try to concatenate str + str")
except  ZeroDivisionError:
    print("cant divide anything by zero")
except NameError:
    print("try to access the identifiers which has been defined") 
except KeyError:
    print("give proper valid key in accessing")              
else:
    print("all exected fine")
finally :
    print("i will execute not depneding any any error r else")    