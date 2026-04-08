import mysql.connector

# print(mysql.connector)
# after connection, need to create connect Obj
dbC = mysql.connector.connect( #dbc object
host="localhost",
user="root",
database="d12_pdbc",
password="10000Coders"
)


tableCreationQuery="""
create table if not exists employees(
    id int primary key ,
    name varchar(50) not null,
    age int,
    email varchar(50) not null unique,
    salary decimal(10,2) not null 
)
"""


# print(dbC,"13th line")
print("db connected successfully....")


cursor__=dbC.cursor() # cursor method is having excute method #cursor object

# print(cursor__,"cusror__")
cursor__.execute(tableCreationQuery)

# print("table created successfully.....")


while True:
    
    print("1. add employee")
    print("2. read employees")
    print("3. update employee")
    print("4. delete employee")
    print("5. exit")

    o=int(input("enter your choice here :-- "))

    if o == 1:
        i=int(input("enter id here :-- "))
        n =input("enter name here :-- ")
        a = int(input("enter age here :-- "))
        e =input("enter email here :-- ")
        s = float(input("enter salary here  :--  "))
        queryInsertingEmp="insert into employees (id,name,age,email,salary) values (%s,%s,%s,%s,%s)"#query of inserting
        data=(i,n,a,e,s) # data to be into insert query
        cursor__.execute(queryInsertingEmp,data) # executing the query and inserting data to table
        dbC.commit() # making insrting opeartion chnages to save permanantly
        print("emp addedd successfully.....")

    elif o == 2: 
        queryReadingEmp="select * from employees"
        cursor__.execute(queryReadingEmp)
        data=cursor__.fetchall()
        for i in data:
            print(i[1],i[2],i[3],i[4])
        # print("got all emps",data)

    elif o == 3:

        queryReadingEmp="select * from employees"
        cursor__.execute(queryReadingEmp)
        data=cursor__.fetchall()
        for i in data:
            print(i[0],i[1],i[2],i[3],i[4])

        id=int(input("enter emp id to update the details of emp :-- "))
        idTobeUpdated=int(input("enter id here to update:-- "))
        ag=int(input("enter age here :-- "))
        sal=float(input("enter slaary here :--   "))

        queryUpdateEmp ="update employees set salary=%s,age=%s,id=%s where id = %s"
        data=(sal,ag,idTobeUpdated,id)   
        cursor__.execute(queryUpdateEmp,data)
        dbC.commit()

        print("emp updated successfyully....")

    elif o == 4:
        queryReadingEmp="select * from employees"
        cursor__.execute(queryReadingEmp)
        data=cursor__.fetchall()
        for i in data:
            print(i[0],i[1],i[2],i[3],i[4])

        print("choose id to dlete emp")   
        id=int(input("enter id to dleete emp :--  "))
        queryDeleteEmp="delete from employees where id =%s"
        data=(id,)
        cursor__.execute(queryDeleteEmp,data)
        dbC.commit()


        print("emp deleted successfully....") 
    else:
        break;


# update
# delete 
# create 
# insert
# select 


# if-elif-else 
# while 
# print()
# varaibles
# input()
# int(),float()
# import 
# list 
# for loop 

