# encapsulation :
# is a technique in oops
# and it is used to hide r private the sensite data 


class Bank:
    bankName="HDFC"

    def __init__(self):
        self.accNumber=123456789 # public
        self.ifcsCode="hdfc00123" #public
        self.branchCode="HydKKP123" #public
        # self._bal = 1234 # protected
        self.__balance=1599 # private varaible
        self.__pin=1310
        print(self.__balance,"14th line")

    def accessing(self):
        print(self.__balance,"17th line")

    def withdraw(self,incomingAmt,incomingPin): # 2000
        if incomingPin == self.__pin:
            if incomingAmt <  self.__balance  : # if incomingPin < self.__balance
                # print("abc vamsi")
                self.__balance -= incomingAmt
                print(f"withdrawan amount is :-- {incomingAmt}")
                print(f"main bal :-- {self.__balance}")
            else:
                print("insufficient funds")
        else:
            print("invalid pin")     

    def check_bal(self,incomingPin):
        if incomingPin == self.__pin:
            print(self.__balance)
        else:
            print("wrong pin entered")    

o=Bank() 
o.withdraw(int(input("enter amount here :-- ")),int(input("enter pin here :-- ")))
# o.check_bal(int(input("enter pin here :-- ")))  #"1310"  1310
# print(o.accNumber  )
# print(o.ifcsCode  )
# o.accessing() # 

# private varaibles outside of class access avvav

# if we wanna access, is there any way :-- yes 
# what is that way :-- name mangling
# print(o._Bank__balance)


ploymorphism
abstraction

oops project 
pdbc with oops 
role based 

pm 
notes
recording
task
student
view
submitting tasks



pdbc with oops :-- 
oops 
functions
conditions
while loop
for loop 
sql crud 
modules
connector module 
sql queries python file how to write 
"""

"""