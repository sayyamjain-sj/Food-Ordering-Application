'''add date and time
filter by date
graphmonth x sales and via product
'''
from tkinter import *
from tkinter import messagebox
import sqlite3
import pdb
import random
import time
import os
if os.path.exists("test1.db"):
  os.remove("test1.db")
  print("Existing Database Deleted")
else:
  print("The file does not exist")

#Linking/Creating Database
conn = sqlite3.connect('test1.db')
cursor=conn.cursor()
print("Database Connected")

#Creating Table Customer
try:
        conn.execute('''CREATE TABLE customers (fname VARCHAR(255), lname VARCHAR(255),
             passwd VARCHAR(255), email VARCHAR(255),address VARCHAR(255) ,
             city VARCHAR(50),mobno VARCHAR(10) Unique , points VARCHAR(255));''')
        print("Table Customer Created")
except:
        print("Table Customer Exists")

#Creating Table Admin
try:
        conn.execute('''CREATE TABLE admin (userid VARCHAR(255) Unique,passwd VARCHAR(255) , addedby VARCHAR(255) );''')
        print("Table Admin Created")
except:
        print("Table Admin Exists")
        

#Creating Table Sold
try:
    conn.execute('''CREATE TABLE sold( mobno VARCHAR(10) , total VARCHAR(255),
        payment VARCHAR(255),cardno VARCHAR(16),cookinginstructions VARCHAR(255),points VARCHAR(10),solddata VARCHAR(255),
        dateoforder VARCHAR(30),billno VARCHAR(10),currenttime VARCHAR(10));''')
    print("Table Sold Created")
except:
    print("Table Sold Exists")

#Creating Table Feedback
try:
        conn.execute('''CREATE TABLE feedback (mobno VARCHAR(10), feedback VARCHAR(500));''')
        print("Table Feedback Created")
except:
        print("Table Feedback Exists")

try:
        conn.execute('''CREATE TABLE menuitems (itemname VARCHAR(256), price int(5));''')
        print("Table menuitems Created")
except:
        print("Table menuitems Exists")
    
sql = "INSERT INTO customers (fname , lname , passwd , email , address , city , mobno,points) VALUES (?,?,?,?,?,?,?,?)"
val = ("Sameer" , "Dewani" , "qwerty" , "sameer@gmail.com" ,  "borivali" , "Mumbai" , "8268281964" , "100")
conn.execute(sql, val)
conn.commit()

sql = "INSERT INTO customers (fname , lname , passwd , email , address , city , mobno , points) VALUES (?,?,?,?,?,?,?,?)"
val = ("Prabhat" , "Singh" , "abcdefg" , "prabhat@mymail.com" ,  "Kandivali" , "Mumbai" , "1234567890","100")
conn.execute(sql, val)
conn.commit()

sql = "INSERT INTO customers (fname , lname , passwd , email , address , city , mobno,points) VALUES (?,?,?,?,?,?,?,?)"
val = ("ram" , "singh" , "lollol" , "2sam@mymail.com" ,  "Home" , "Mumbai" , "1234567895","20")
conn.execute(sql, val)
conn.commit()

sql = "INSERT INTO admin (userid , passwd , addedby) VALUES (?,?,?)"
val = ("admin" , "admin" , "default")
conn.execute(sql, val)
conn.commit()

sql = "INSERT INTO menuitems (itemname , price) VALUES (?,?)"
val = ("admin" , 50)
conn.execute(sql, val)
conn.commit()

'''
sql = "INSERT INTO sold( mobno ,total ,payment ,cardno ,cookinginstructions,points,solddata,) VALUES (?,?,?,?,?,?,?)"
val = ("1234567890" , "550" , "cash" , "1234567891123456" ,  "abc defg" , "55" , "[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]" )
sql = "INSERT INTO sold (mobno , total , payment , cardno, cookinginstructions ,points,solddata,dateoforder,currenttime,billno) VALUES (?,?,?,?,?,?,?,?,?,?)"
val = ("8268281963" , "5000" , "Cash on Delivery" , "NA", "Make it Crispy","500","[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]",DateofOrder,current_time,billno)
conn.execute(sql, val)
conn.commit()

for i in range(30):
  sql = "INSERT INTO feedback( mobno ,feedback) VALUES (?,?)"
  val = ("1234567890" , "The Food was very nice and fast delivery time" )
  conn.execute(sql, val)
  conn.commit()
'''

conn.close()
print("success")


