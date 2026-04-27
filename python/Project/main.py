print("chooose one option below")
print("1. Register")
print("2. Login")


i=input("choose one from above features")

if  int(i) == 1:
    from register import Register 
    name_input=input("enter yr name :-- ")
    acc_Num_input=input("enter yr ac_number here  :-- ")
    balance_input=input("enter fst_bal here :-- ")
    p_input=input("enter yr name :-- ")
    c_p_input=input("enter yr password again name :-- ")
    Register(name_input,acc_Num_input,balance_input,p_input,c_p_input)
elif int(i)==2:
    from login import Login
    ac_num_Login=input("enter yr account number :--  ")
    p_Login=input("enter login password here :-- ")
    Login(ac_num_Login,p_Login)
    