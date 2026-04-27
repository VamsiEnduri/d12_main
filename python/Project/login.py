class Login:

    def __init__(self,an,p):
        from db_connection import cur_obj
        fetchQuery="select * from users"
        cur_obj.execute(fetchQuery)
        usersData=cur_obj.fetchall()
        for i in usersData:
            if i[2] == an and i[4] == p:
                print(f"login success ful {i[1]}")
                from dashboard import Dashboard
                Dashboard(i)
                break
            else:
                print("invalid credentials")     