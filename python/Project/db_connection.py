# python + mysql 
# third party package :--
# mysql-connector-python 
import mysql.connector

db_con_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    database="d12_oops_project",
    password="10000Coders"
)

cur_obj=db_con_obj.cursor()

print("db connected successfully...")