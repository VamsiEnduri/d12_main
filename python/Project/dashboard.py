class Dashboard:

    def __init__(self,i):
        print(f" welcome to dashboard dear {i[1]}")

        print("choose below features to experience our bank")
        print("1. withdraw")
        print("2. Deposit")
        print("3. check_balance")
        print("4. logout")

        o=input("choose one from above features")

        if  int(o) == 1: # with
            def withdraw(p,iAmt):
                nonlocal i
                if p == i[len(i)-1]:
                    if iAmt <0:
                        print("enter valid amount")
                    else:
                        if iAmt < i[len(i)-2]: # 12000 < 15000
                            i=list(i)
                            i[len(i)-2]-= iAmt  # 3000
                            print( i[len(i)-2],"amount")
                            q="update users set balance = %s where account_number = %s and password = %s"
                            d=(i[len(i)-2],i[2],i[len(i)-1])
                            from db_connection import cur_obj,db_con_obj
                            cur_obj.execute(q,d)
                            db_con_obj.commit()
                            print("amount updated successfully....")
                        else:
                            print("insufficient funds")       
                else:
                    print("invalid validation ")    
            withdraw(input("enter password here to draw the amt :-- "),int(input("enter withdraw amount here :-- ")))    
        elif int(o)==2: # deposit
            def deposit(p,dAmt):
                nonlocal i
                if p == i[len(i)-1]:
                    if dAmt > 0 :
                        i=list(i)
                        i[len(i)-2] += dAmt
                        q="update users set balance = %s where account_number = %s and password = %s"
                        d=(i[len(i)-2],i[2],i[len(i)-1])
                        from db_connection import cur_obj,db_con_obj
                        cur_obj.execute(q,d)
                        db_con_obj.commit()
                        print("amount updated successfully as crediting....")
                        print(f"amount after deposit {i[len(i)-2]}")

            deposit(input("enter password here to deposit the amt :-- "),int(input("enter deposit amount here :-- ")))    
        elif int(o) ==3: # check bal
            def check_bal(password_check_bal):
                if password_check_bal == i[len(i)-1]: #"" == 
                    print(i[len(i)-2])
                else:
                    print("validation not done")    
            check_bal(input("enter password to chekc the bal"))       
        else: #logout
            pass     


# fri + sat
# file handling
# abstraction

# list_dict_methods crud
# comprehensions
# lamda 