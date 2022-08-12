from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import pdb
import random
import time
import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Linking/Creating Database
conn = sqlite3.connect('test1.db')
print("Database Connected")
cursor=conn.cursor()

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
   conn.execute('''CREATE TABLE sold( mobno VARCHAR(10) , total VARCHAR(255),payment VARCHAR(255),cardno VARCHAR(16),
                cookinginstructions VARCHAR(255),points VARCHAR(10),solddata VARCHAR(255),dateoforder VARCHAR(30),billno VARCHAR(10),currenttime VARCHAR(10));''')
   print("Table Sold Created")
except:
    print("Table Sold Exists")

#Creating Table Feedback
try:
        conn.execute('''CREATE TABLE feedback (mobno VARCHAR(10), feedback VARCHAR(500));''')
        print("Table Feedback Created")
except:
        print("Table Feedback Exists")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

def signup():
        def reset():
                fname.set("")
                lname.set("")
                passwd.set("")
                email.set("")
                address.set("")
                city.set("")
                mobno.set("")            
        def submit():
                if(fname.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Name")
                elif(lname.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Name")
                elif(passwd.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Password")
                elif(email.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Email Address")
                elif(len(mobno.get())!=10):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Mobile Number")
                elif(address.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Address")
                elif(city.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid City")
                elif(passwd.get().lower()==fname.get().lower() or passwd.get().lower()==lname.get().lower() or passwd.get()==mobno.get()):
                        passwd.set("")
                        messagebox.showinfo("Burger Therapy", "Enter a Strong Password")
                else:
                        try:
                                a=mobno.get()
                                a=int(a)
                                if (a>1000000000 and a<=9999999999):
                                        try:
                                                point="0"
                                                sql = "INSERT INTO customers (fname , lname , passwd , email , address , city , mobno,points) VALUES (?,?,?,?,?,?,?,?)"
                                                val = (fname.get() , lname.get() , passwd.get() , email.get() ,  address.get() , city.get() , mobno.get() , point)
                                                conn.execute(sql, val)
                                                conn.commit()
                                                print("success")
                                                messagebox.showinfo("Burger Therapy", "Registration Successful")
                                                s2.destroy()
                                                startscreen()
                                        except:
                                                mobno.set("")
                                                messagebox.showinfo("Burger Therapy", "Account Already Exists with Following MObile Number")
                                else:
                                        mobno.set("")
                                        messagebox.showinfo("Burger Therapy", "Invalid Mobile Number")
                        except:
                                mobno.set("")
                                messagebox.showinfo("Burger Therapy", "Invalid Mobile Number")
                        
                        
                        
        s2=Tk()
        s2.geometry("1080x720")
        s2.title("Burger Therapy - SignUp")

        fname=StringVar()
        lname=StringVar()
        passwd=StringVar()
        email=StringVar()
        mobno=StringVar()
        address=StringVar()
        city=StringVar()
        
        c = Canvas(s2, width=1080, height=720, bg="red")
        filename = PhotoImage(file = "background.png")

        label1 = Label(s2, image = filename)
        label1.place(x = 0, y = 0 , relwidth=1, relheight=1)
        
        frame=LabelFrame(s2,text="Welcome to Burger Therapy",font=("cooper black",28) , padx=50 , pady=50 ,bg="#d1b493" )
        frame.grid( padx=125 , pady=150)
        
        lab1=Label(frame,text="REGISTRATION",fg="white",bg="#78543c",width=20,font=("cooper black",30))
        lab1.grid(row=0 , column=2)

        lab2=Label(frame,bg="#d1b493")
        lab2.grid(row=1 , column=0)
        
        lab3=Label(frame,text="FirstName",bg="#d1b493",fg="black",font=("cooper black",18))
        lab3.grid(row=2 , column=1)
        e1=Entry(frame,textvariable=fname,bg="white",width=15,font=("cooper black",18))
        e1.grid(row=2 , column=2)
        
        lab4=Label(frame,text="LastName",bg="#d1b493",fg="black",font=("cooper black",18))
        lab4.grid(row=3 , column=1)
        e2=Entry(frame,textvariable=lname,bg="white",width=15,font=("cooper black",18))
        e2.grid(row=3 , column=2)
        
        lab5=Label(frame,text="Password",bg="#d1b493",fg="black",font=("cooper black",18))
        lab5.grid(row=4 , column=1)
        e3=Entry(frame,textvariable=passwd,show='*',bg="white",width=15,font=("cooper black",18))
        e3.grid(row=4 , column=2)

        def on_press(event):
                e3.config(show='')

        def on_release( event):
                e3.config(show='*')
                
        b4image = PhotoImage(file = "visible.png")
        b4=Button(frame,image = b4image ,fg="#d5b493" ,anchor="w", bg="#d5b493" ,activebackground="#d5b493" , bd=4 )
        b4.grid(row=4 , column=2,sticky="e")
        b4.bind("<ButtonPress>", on_press)
        b4.bind("<ButtonRelease>", on_release)
        

        lab6=Label(frame,text="Email",bg="#d1b493",fg="black",font=("cooper black",18))
        lab6.grid(row=5 , column=1)
        e4=Entry(frame,bg="white",textvariable=email,width=15,font=("cooper black",18))
        e4.grid(row=5 , column=2)
        
        lab7=Label(frame,text="Mobile No.",bg="#d1b493",fg="black",font=("cooper black",18))
        lab7.grid(row=6 , column=1)
        e5=Entry(frame,bg="white",textvariable=mobno,width=15,font=("cooper black",18))
        e5.grid(row=6 , column=2)

        lab8=Label(frame,text="Address" ,bg="#d1b493",fg="black",font=("cooper black",18))
        lab8.grid(row=7 , column=1)
        e6=Entry(frame,bg="white",textvariable=address,width=15,font=("cooper black",18))
        e6.grid(row=7 , column=2)

        lab9=Label(frame , text="City" ,bg="#d1b493",fg="black",font=("cooper black",18))
        lab9.grid(row=8 , column=1)
        e7=Entry(frame,bg="white",textvariable=city,width=15,font=("cooper black",18))
        e7.grid(row=8 , column=2)
        
        lab10=Label(frame,bg="#d1b493")
        lab10.grid(row=9 , column=0)

        b1=Button(frame,text=" Back ",command=lambda:[s2.destroy(),startscreen()],bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b1.grid(row=10 , column=1)
        b2=Button(frame,text=" Reset ",command=reset,bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b2.grid(row=10, column=2)
        b3=Button(frame,text=" Submit ",command=submit,bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b3.grid(row=10, column=3)
        s2.resizable(False, False)
        s2.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

def editcustomer(useridd):
    def delete(mobno1):
            mobno1 = int(e1.get())
            cursor.execute("delete from customers where mobno = ?" , (mobno1,))
            conn.commit()
            for widget in bottomframe.winfo_children():
                        widget.destroy()
            messagebox.showinfo("Burger Therapy", "User Deleted Succesfully")
    
    def searchcustomer():
        def update(mobno1):
                if(fname.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Name")
                elif(lname.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Name")
                elif(passwd.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Password")
                elif(email.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Email Address")
                elif(int(e8.get())!=int(mobno1)):
                        messagebox.showinfo("Burger Therapy", "Check Mobile Number")
                elif(address.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Address")
                elif(city.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid City")
                elif(points.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter Valid Points")
                elif(passwd.get().lower()==fname.get().lower() or passwd.get().lower()==lname.get().lower() or passwd.get()==mobno.get()):
                        passwd.set("")
                        messagebox.showinfo("Burger Therapy", "Enter a Strong Password")
                else:
                    try:
                        temp=int(points.get())
                        cursor.execute("delete from customers where mobno = ?" , (mobno1,))
                        conn.commit()
                        sql = "INSERT INTO customers (fname , lname , passwd , email , address , city , mobno , points) VALUES (?,?,?,?,?,?,?,?)"
                        val = (fname.get() , lname.get() , passwd.get() , email.get() ,  address.get() , city.get() , mobno1 , points.get())
                        conn.execute(sql, val)
                        conn.commit()
                        messagebox.showinfo("Burger Therapy", "Update Successful")
                    except:
                        messagebox.showinfo("Burger Therapy", "Enter Valid Points")
                    
                   
        
        if(e1.get()==""):
                messagebox.showinfo("Burger Therapy", "Enter a Valid Mobile Number")
                for widget in bottomframe.winfo_children():
                        widget.destroy()
        else:
            try:
                mobno1 = int(e1.get())
                cursor.execute("select * from customers where mobno = ?" , (mobno1,))                   
                details=cursor.fetchall()
                if(details==None or details==[]):
                    mobno.set("")
                    for widget in bottomframe.winfo_children():
                        widget.destroy()
                    messagebox.showinfo("Burger Therapy", "Invalid Mobile Number")

                else:
                    for widget in bottomframe.winfo_children():
                        widget.destroy()
                        
                    cursor.execute("PRAGMA table_info(customers)")
                    detail=cursor.fetchall()
                    i=0
                    for k in range(len(detail)):
                        abc=list(detail[k])
                        label1= Label(bottomframe,width=10,font=('cooper black', 15, 'bold') ,text=abc[1],borderwidth=2,relief='ridge', anchor="c") 
                        label1.grid(row=i, column=0)
                        label2 = Label(bottomframe,width=5,font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493') 
                        label2.grid(row=i, column=1)
                        i=i+1
                    
                    cursor.execute("select * from customers where mobno = ?" , (mobno1,))                   
                    details=cursor.fetchall()
                    details=list(details[0])
                    #print(details)
                    
                    fname=StringVar()
                    lname=StringVar()
                    passwd=StringVar()
                    email=StringVar()
                    address=StringVar()
                    city=StringVar()
                    mobno1=StringVar()
                    points=StringVar()

                    e2=Entry(bottomframe,textvariable=fname,bg="white",width=20,font=("cooper black",18))
                    e2.grid(row=0 , column=2)
                    e2.insert(END, details[0])

                    e3=Entry(bottomframe,textvariable=lname,bg="white",width=20,font=("cooper black",18))
                    e3.grid(row=1 , column=2)
                    e3.insert(END, details[1])
                    
                    e4=Entry(bottomframe,textvariable=passwd,bg="white",width=20,font=("cooper black",18))
                    e4.grid(row=2 , column=2)
                    e4.insert(END, details[2])

                    e5=Entry(bottomframe,textvariable=email,bg="white",width=20,font=("cooper black",18))
                    e5.grid(row=3 , column=2)
                    e5.insert(END, details[3])
                    
                    e6=Entry(bottomframe,textvariable=address,bg="white",width=20,font=("cooper black",18))
                    e6.grid(row=4 , column=2)
                    e6.insert(END, details[4])

                    e7=Entry(bottomframe,textvariable=city,bg="white",width=20,font=("cooper black",18))
                    e7.grid(row=5 , column=2)
                    e7.insert(END, details[5])

                    e8=Entry(bottomframe,textvariable=mobno1,bg="white",width=20,font=("cooper black",18))
                    e8.grid(row=6 , column=2)
                    e8.insert(END, details[6])
                    
                    e9=Entry(bottomframe,textvariable=points,bg="white",width=20,font=("cooper black",18))
                    e9.grid(row=7 , column=2)
                    e9.insert(END, details[7])
                    
                    
                    label3 = Label(bottomframe,width=5,font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493') 
                    label3.grid(row=8, column=1)
                    b3=Button(bottomframe, font=('cooper black', 15, 'bold'), text="Delete",command=lambda:[delete(e1.get())], bd=4)
                    b3.grid(row=9, column=0)
                    b4=Button(bottomframe, font=('cooper black', 15, 'bold'), text="Update",command=lambda:[update(e1.get())], bd=4)
                    b4.grid(row=9, column=2)
        
            except:
                mobno.set("")
                messagebox.showinfo("Burger Therapy", "InValid Mobile Number")

                
    s5=Tk()
    s5.geometry("1080x720")
    s5.configure(background="#d5b493")
    s5.title("Burger Therapy - Admin - Update Customer Details")

    lbl3 = Label(s5,bg='#d5b493',fg='#d5b493')
    lbl3.pack()

        
    topframe = Frame(s5,bg='#d5b493')
    topframe.pack(side=TOP)
    lbl1 = Label(topframe, font=('cooper black', 24, 'bold'), text="aaaaa",bg='#d5b493',fg='#d5b493')
    lbl1.grid(row=0, column=0)
    lblInfo = Label(topframe, font=('cooper black', 45, 'bold'), text="Update Customer Details", bd=12, relief="raise")
    lblInfo.grid(row=0, column=1)
    lbl2 = Label(topframe, font=('cooper black', 24, 'bold'), text="aaa",bg='#d5b493',fg='#d5b493')
    lbl2.grid(row=0, column=2)
    b1=Button(topframe, font=('cooper black', 20, 'bold'), text="Back",command=lambda:[s5.destroy(),adminloggedin(useridd)], bd=8, relief="raise")
    b1.grid(row=0, column=3)
        
    lbl3 = Label(s5,bg='#d5b493',fg='#d5b493')
    lbl3.pack()
    lbl4 = Label(s5,bg='#d5b493',fg='#d5b493')
    lbl4.pack()

    mobno=StringVar()
    middleframe = Frame(s5,bg='#d5b493')
    middleframe.pack()
    l1= Label(middleframe,text="Customer Mobile Number ",font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w",fg='#000000') 
    l1.grid(row=0, column=0)
    l2= Label(middleframe,text="N",font=('cooper black', 15, 'bold'), anchor="w",bg='#d5b493',fg='#d5b493') 
    l2.grid(row=0, column=1)
    e1 = Entry(middleframe,textvariable=mobno, width=11,font=('cooper black', 15, 'bold'), fg='#000000',borderwidth=2,relief='ridge') 
    e1.grid(row=0, column=2)
    #e1.insert(END, "1234567890")
    l3= Label(middleframe,text="be",font=('cooper black', 15, 'bold') , anchor="w",bg='#d5b493',fg='#d5b493') 
    l3.grid(row=0, column=3)
    b2=Button(middleframe, font=('cooper black', 15, 'bold'), text="Search",command=searchcustomer, bd=4,fg='#000000')
    b2.grid(row=0, column=4)
    l4= Label(middleframe,text="be",font=('cooper black', 15, 'bold') , anchor="w",bg='#d5b493',fg='#d5b493') 
    l4.grid(row=1, column=0)

    bottomframe = Frame(s5,bg='#d5b493')
    bottomframe.pack()
                    
    s5.resizable(False, False)
    s5.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

def customerdetails(useridd):
        s5 = Tk()
        s5.geometry("1080x720")
        s5.title("Burger Therapy - Admin - View Customer Details")

        topframe = Frame(s5, bg="#d5b493")
        topframe.pack(side=TOP,fill=BOTH)
        lbl = Label(topframe,bg='#d5b493',fg='#d5b493')
        lbl.grid(row=0, column=0)
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="aaaaai",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=0)
        lblInfo = Label(topframe, font=('cooper black', 45, 'bold'), text="Customer Details", bd=10, relief="raise")
        lblInfo.grid(row=1, column=1)
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="aaai",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=2)
        b2=Button(topframe, font=('cooper black', 25, 'bold'), text="Back",command=lambda:[s5.destroy(),adminloggedin(useridd)], bd=6 )
        b2.grid(row=1, column=3)
        lblInfo1 = Label(topframe,bg='#d5b493',fg='#d5b493')
        lblInfo1.grid(row=2, column=1)


        main_frame = Frame(s5, bg="#d5b493")
        main_frame.pack(fill=BOTH , expand=1)

        my_canvas = Canvas(main_frame ,bg="#d5b493")
        my_canvas.pack(side =LEFT , fill=BOTH , expand=1)

        my_scrollbar1 = ttk.Scrollbar(s5 , orient = HORIZONTAL , command = my_canvas.xview)
        my_scrollbar1.pack(side =BOTTOM , fill=X )

        my_scrollbar = ttk.Scrollbar(main_frame , orient = VERTICAL , command = my_canvas.yview)
        my_scrollbar.pack(side =RIGHT , fill=Y)

        my_canvas.configure(xscrollcommand=my_scrollbar1.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = Frame(my_canvas , bg="#d5b493")
        my_canvas.create_window((0,0), window=second_frame , anchor = "nw")
        #--------------

        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493' ) 
        l1.grid(row=0, column=0)
        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold') ,bg='#d5b493',fg='#d5b493') 
        l1.grid(row=0, column=10)


        #fname
        cursor.execute("SELECT MAX(LENGTH(fname)) FROM customers") 
        details=cursor.fetchall()
        fname=list(details[0])
        fname=int(fname[0])
        if(fname<10):
            fname=10

        #lname
        cursor.execute("SELECT MAX(LENGTH(lname)) FROM customers") 
        details=cursor.fetchall()
        lname=list(details[0])
        lname=int(lname[0])
        if(lname<10):
            lname=10

        #passwd
        cursor.execute("SELECT MAX(LENGTH(passwd)) FROM customers") 
        details=cursor.fetchall()
        passwd=list(details[0])
        passwd=int(passwd[0])
        if(passwd<10):
            passwd=10

        #email
        cursor.execute("SELECT MAX(LENGTH(email)) FROM customers") 
        details=cursor.fetchall()
        email=list(details[0])
        email=int(email[0])
        if(email<10):
            email=10

        #address
        cursor.execute("SELECT MAX(LENGTH(address)) FROM customers") 
        details=cursor.fetchall()
        address=list(details[0])
        address=int(address[0])
        if(address<10):
            address=10

        #city
        cursor.execute("SELECT MAX(LENGTH(city)) FROM customers") 
        details=cursor.fetchall()
        city=list(details[0])
        city=int(city[0])
        if(city<10):
            city=10

        #Table Heading
        l1= Label(second_frame,text="Sr No. ",width=5,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=1)
        l1= Label(second_frame,text="First Name",width=fname,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=2)
        l1= Label(second_frame,text="Last Name",width=lname,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=3)
        l1= Label(second_frame,text="Password",width=passwd,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=4)
        l1= Label(second_frame,text="Email ID",width=email,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=5)
        l1= Label(second_frame,text="Address",width=address,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=6)
        l1= Label(second_frame,text="City",width=city,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=7)
        l1= Label(second_frame,text="Mobile No.",width=10,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=8)
        l1= Label(second_frame,text="Points",width=6,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=9)


        cursor.execute("SELECT * FROM customers") 
        details=list(cursor.fetchall())
        abc=[]
        i=2
        for k in range(len(details)):
            abc=list(details[k])
            l1= Label(second_frame,text=k+1,width=5,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
            l1.grid(row=k+2, column=1)
            e = Label(second_frame,width=fname,font=('cooper black', 15, 'bold'), text=abc[0],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=2)
            e = Label(second_frame,width=lname,font=('cooper black', 15, 'bold'), text=abc[1],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=3)
            e = Label(second_frame,width=passwd,font=('cooper black', 15, 'bold'), text=abc[2],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=4)
            e = Label(second_frame,width=email,font=('cooper black', 15, 'bold'), text=abc[3],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=5)
            e = Label(second_frame,width=address,font=('cooper black', 15, 'bold'), text=abc[4],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=6)
            e = Label(second_frame,width=city,font=('cooper black', 15, 'bold'), text=abc[5],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=7)
            e = Label(second_frame,width=10,font=('cooper black', 15, 'bold'), text=abc[6],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=8)
            e = Label(second_frame,width=6,font=('cooper black', 15, 'bold'), text=abc[7],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=9)
            i=i+1

        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493') 
        l1.grid(row=i, column=0)
        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493') 
        l1.grid(row=i, column=10)

        s5.resizable(False, False)
        s5.mainloop()    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

def viewsales(useridd):
        def salesgraph():
            yaxis=[]
            xaxis=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/01/22'") 
            details=list(cursor.fetchall())
            jan=details[0][0]
            if jan == None:
                jan=0
                jan=int(jan)
            yaxis.append(jan)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/02/22'") 
            details=list(cursor.fetchall())
            feb=details[0][0]
            if feb == None:
                feb=0
                feb=int(feb)
            yaxis.append(feb)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/03/22'") 
            details=list(cursor.fetchall())
            march=details[0][0]
            if march == None:
                march=0
                march=int(march)
            yaxis.append(march)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/04/22'") 
            details=list(cursor.fetchall())
            april=details[0][0]
            if april == None:
                april=0
                april=int(april)
            yaxis.append(april)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/05/22'") 
            details=list(cursor.fetchall())
            may=details[0][0]
            if may == None:
                may=0
                may=int(may)
            yaxis.append(may)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/06/22'") 
            details=list(cursor.fetchall())
            june=details[0][0]
            if june == None:
                june=0
                june=int(june)
            yaxis.append(june)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/07/22'") 
            details=list(cursor.fetchall())
            july=details[0][0]
            if july == None:
                july=0
                july=int(july)
            yaxis.append(july)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/08/22'") 
            details=list(cursor.fetchall())
            aug=details[0][0]
            if aug == None:
                aug=0
                aug=int(aug)
            yaxis.append(aug)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/09/22'") 
            details=list(cursor.fetchall())
            sept=details[0][0]
            if sept == None:
                sept=0
                sept=int(sept)
            yaxis.append(sept)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/10/22'") 
            details=list(cursor.fetchall())
            october=details[0][0]
            if october == None:
                october=0
                october=int(october)
            yaxis.append(october)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/11/22'") 
            details=list(cursor.fetchall())
            nov=details[0][0]
            if nov == None:
                nov=0
                nov=int(nov)
            yaxis.append(nov)
            cursor.execute("SELECT sum(total) FROM sold WHERE dateoforder LIKE '%/12/22'") 
            details=list(cursor.fetchall())
            dec=details[0][0]
            if dec == None:
                dec=0
                dec=int(dec)
            yaxis.append(dec)
            
            fig = plt.figure()
            plt.bar(xaxis, yaxis, color ='maroon',width = 0.4)
            plt.xlabel("Sales 2022")
            plt.ylabel("Amount in Rs.")
            plt.title("Month")
            plt.show()
            
            
            
        
        s5 = Tk()
        s5.geometry("1080x720")
        s5.title("Burger Therapy - Admin - View Sales")

        topframe = Frame(s5, bg="#d5b493")
        topframe.pack(side=TOP,fill=BOTH)
        lbl = Label(topframe,bg='#d5b493',fg='#d5b493')
        lbl.grid(row=0, column=0)
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="aaaaaaaaaaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=0)
        lblInfo = Label(topframe, font=('cooper black', 45, 'bold'), text="Sales", bd=10, relief="raise")
        lblInfo.grid(row=1, column=1)
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="aaaaaaaaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=2)
        b2=Button(topframe, font=('cooper black', 20, 'bold'), text="Back",command=lambda:[s5.destroy(),adminloggedin(useridd)], bd=6 )
        b2.grid(row=1, column=3)
        b3=Button(topframe, font=('cooper black', 20, 'bold'), text="Graph",command=salesgraph, bd=6 )
        b3.grid(row=2, column=3)
        lblInfo1 = Label(topframe,bg='#d5b493',fg='#d5b493')
        lblInfo1.grid(row=3, column=1)


        main_frame = Frame(s5, bg="#d5b493")
        main_frame.pack(fill=BOTH , expand=1)

        my_canvas = Canvas(main_frame ,bg="#d5b493")
        my_canvas.pack(side =LEFT , fill=BOTH , expand=1)

        my_scrollbar1 = ttk.Scrollbar(s5 , orient = HORIZONTAL , command = my_canvas.xview)
        my_scrollbar1.pack(side =BOTTOM , fill=X )

        my_scrollbar = ttk.Scrollbar(main_frame , orient = VERTICAL , command = my_canvas.yview)
        my_scrollbar.pack(side =RIGHT , fill=Y)

        my_canvas.configure(xscrollcommand=my_scrollbar1.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = Frame(my_canvas , bg="#d5b493")
        my_canvas.create_window((0,0), window=second_frame , anchor = "nw")
        

        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493' ) 
        l1.grid(row=0, column=0)
        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold') ,bg='#d5b493',fg='#d5b493') 
        l1.grid(row=0, column=10)


        #instructions
        cursor.execute("SELECT MAX(LENGTH(cookinginstructions)) FROM sold") 
        details=cursor.fetchall()
        instructions=list(details[0])
        print(instructions)
        instructions=int(instructions[0])
        print(instructions)
        if(instructions<20):
            instructions=20

        

        #Table Heading
        l1= Label(second_frame,text="Sr No.",width=5,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(rowspan=2, column=1)
        l1= Label(second_frame,text="Bill No.",width=15,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(rowspan=2, column=2)
        l1= Label(second_frame,text="Date of Order",width=15,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=3)
        l1= Label(second_frame,text="Time",width=7,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=4)
        l1= Label(second_frame,text="Mobile No.",width=10,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=5)
        l1= Label(second_frame,text="Total",width=10,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=6)
        l1= Label(second_frame,text="Payment",width=15,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=7)
        l1= Label(second_frame,text="Card No",width=20,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=8)
        l1= Label(second_frame,text="Cooking Instructions",width=instructions,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=9)
        l1= Label(second_frame,text="Points",width=12,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=10)
        l1= Label(second_frame,text="Sold Data",width=75,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=11)
        l1= Label(second_frame,text="Sold Data",width=75,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=2, column=11)
        
        
        
        cursor.execute("SELECT * FROM sold") 
        details=list(cursor.fetchall())
        abc=[]
        i=2
        for k in range(len(details)):
            abc=list(details[k])
            print(abc)
            l1= Label(second_frame,text=k+1,width=5,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
            l1.grid(row=k+3, column=1)
            e = Label(second_frame,width=15,font=('cooper black', 15, 'bold'), text=abc[8],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=2)
            e = Label(second_frame,width=15,font=('cooper black', 15, 'bold'), text=abc[7],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=3)
            e = Label(second_frame,width=7,font=('cooper black', 15, 'bold'), text=abc[9],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=4)
            e = Label(second_frame,width=10,font=('cooper black', 15, 'bold'), text=abc[0],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=5)
            e = Label(second_frame,width=10,font=('cooper black', 15, 'bold'), text=abc[1],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=6)
            e = Label(second_frame,width=15,font=('cooper black', 15, 'bold'), text=abc[2],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=7)
            e = Label(second_frame,width=20,font=('cooper black', 15, 'bold'), text=abc[3],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=8)
            e = Label(second_frame,width=instructions,font=('cooper black', 15, 'bold'), text=abc[4],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=9)
            e = Label(second_frame,width=12,font=('cooper black', 15, 'bold'), text=abc[5],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=10)
            e = Label(second_frame,width=75,font=('cooper black', 15, 'bold'), text=abc[6],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i+1, column=11)
            
            i=i+1

        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493') 
        l1.grid(row=i, column=0)
        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493') 
        l1.grid(row=i, column=10)

        s5.resizable(False, False)
        s5.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

def addadmin(useridd):
        def submit():
            if(userid.get()==""):
                    messagebox.showinfo("Burger Therapy", "Enter a Valid User ID")
            elif(passwd.get()==""):
                    messagebox.showinfo("Burger Therapy", "Enter a Valid Password")
            elif(passwd.get().lower()==userid.get().lower() or passwd.get().upper()==userid.get().upper()):
                    passwd.set("")
                    messagebox.showinfo("Burger Therapy", "Enter a Strong Password")
            else:
                    try:
                        sql = "INSERT INTO admin (userid , passwd , addedby) VALUES (?,?,?)"
                        val = (userid.get() , passwd.get() , useridd)
                        conn.execute(sql, val)
                        conn.commit()
                        messagebox.showinfo("Burger Therapy", "Admin Registration Successful")
                        userid.set("")
                        passwd.set("")
                    except:
                        userid.set("")
                        passwd.set("")
                        messagebox.showinfo("Burger Therapy", "Account Already Exists with Following User ID")
                        
        s5=Tk()
        s5.configure(background="#d5b493")
        s5.geometry("1080x720")
        s5.title("Burger Therapy - Admin - Add Admin")

        topframe = Frame(s5, bg="#d5b493")
        topframe.pack(side=TOP)
        lbl = Label(topframe,bg='#d5b493',fg='#d5b493')
        lbl.grid(row=0, column=0)
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="aaaaaaaaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=0)
        lblInfo = Label(topframe, font=('cooper black', 45, 'bold'), text="Add Admin", bd=12, relief="raise")
        lblInfo.grid(row=1, column=1)
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="aaaaaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=2)
        b1=Button(topframe, font=('cooper black', 25, 'bold'), text="Back",command=lambda:[s5.destroy(),adminloggedin(useridd)], bd=6)
        b1.grid(row=1, column=3)
        
            
        lblInfo1 = Label(s5,bg='#d5b493',fg='#d5b493')
        lblInfo1.pack()
        lblInfo2 = Label(s5,bg='#d5b493',fg='#d5b493')
        lblInfo2.pack()

        userid=StringVar()
        passwd=StringVar()
        
        bottomframe = Frame(s5,bg='#d5b493')
        bottomframe.pack()
        lab1=Label(bottomframe,text="User ID: ",width=13,anchor="w" , font=("cooper black",16))
        lab1.grid(row=1 , column=1)
        e1=Entry(bottomframe,textvariable=userid, bg="white",width=15,font=("cooper black",18))
        e1.grid(row=1 , column=2)

        lab3=Label(bottomframe,text="Password ",width=13,anchor="w" , font=("cooper black",16))
        lab3.grid(row=2 , column=1)
        e2=Entry(bottomframe,textvariable=passwd, show='*', bg="white",width=15,font=("cooper black",18))
        e2.grid(row=2 , column=2)
        
        def on_press(event):
                e2.config(show='')

        def on_release( event):
                e2.config(show='*')
                
        b2image = PhotoImage(file = "visible.png")
        b2=Button(bottomframe,image = b2image ,fg="#d5b493" ,anchor="e", bg="#d5b493" ,activebackground="#d5b493" , bd=4 )
        b2.grid(row=2 , column=3 , sticky="e")
        b2.bind("<ButtonPress>", on_press)
        b2.bind("<ButtonRelease>", on_release)

        lab5=Label(bottomframe,text="Added By: ",width=13,anchor="w" , font=("cooper black",16))
        lab5.grid(row=3 , column=1)
        lab6=Label(bottomframe,text=useridd ,  width=16,anchor="w",font=("cooper black",16))
        lab6.grid(row=3 , column=2)

        lab7=Label(bottomframe,bg='#d5b493',fg='#d5b493')
        lab7.grid(row=4 , column=2)
        
        b1=Button(bottomframe, font=('cooper black', 15, 'bold'), text="Add",width=20,command=submit, bd=4, relief="raise")
        b1.grid(row=5, column=2)
        
        s5.resizable(False, False)
        s5.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            


def payment(TC,finalnumber,solddata):
    print(type(billno))
    print(type(current_time))
    print(type(DateofOrder))
    solddata=solddata
    TC=TC
    finalnumber=finalnumber
    print("PAYMENT",TC,finalnumber,solddata)        
    
    def submit():
        nonlocal TC
        if(CheckVar1.get()==0):
            if(lev1.get()=="Credit Card"):
                    def on_closing():
                            s7.deiconify()
                            s8.destroy()
                    def verify():
                            if(len(e1.get())>=16 and len(e1.get())<=19 and len(e2.get())==3):
                                    try:
                                            cc=int(e1.get())
                                            ps=int(e2.get())
                                            print("finalnumber,cc,ps",finalnumber,cc,ps)
                                            paid="Credit Card"
                                            solddataa=str(solddata)
                                            
                                            cursor.execute("SELECT points from customers where mobno = ?" , (finalnumber,))
                                            details=cursor.fetchall()
                                            a=int(details[0][0])
                                            totalpoints=a
                                            
                                            sql = "INSERT INTO sold (mobno , total , payment , cardno, cookinginstructions ,points,solddata,dateoforder,currenttime,billno) VALUES (?,?,?,?,?,?,?,?,?,?)"
                                            val = (finalnumber , TC , paid , e1.get(), instructions.get(),totalpoints,solddataa,DateofOrder,current_time,billno)
                                            conn.execute(sql, val)
                                            conn.commit()

                                            
                                            a=totalpoints+int(TC*0.07)
                                            conn.execute("UPDATE customers set points=? WHERE mobno =?",(a,finalnumber))
                                            conn.commit()

                                            aa=('%.2f' %TC)

                                            s8.destroy()
                                            s7.deiconify()

                                            finel="Order Placed \n"+"Total Amount: Rs."+str(aa)       
                                            messagebox.showinfo("Burger Therapy", finel)
                                            
                                            s7.destroy()
                                            login(finalnumber)
                                                    
                                    except:
                                            messagebox.showinfo("Burger Therapy", "InValid Input")
                                            e1.delete(0,END)
                                            e1.insert(0,"")
                                            e2.delete(0,END)
                                            e2.insert(0,"")
                            else:
                                    messagebox.showinfo("Burger Therapy", "InValid Input")
                                    e1.delete(0,END)
                                    e1.insert(0,"")
                                    e2.delete(0,END)
                                    e2.insert(0,"")
                    s7.withdraw()
                    s8 = Tk()
                    s8.geometry("325x90")
                    s8.title("Burger Therapy - Payment")
                    Label(s8, text="Credit Card",bd=2).grid(row=0, column=1)
                    Label(s8, text="Pin",bd=2).grid(row=1, column=1)


                    e1 = Entry(s8,bd=2)
                    e2 = Entry(s8,bd=2,show='*')
                    
                    e1.grid(row=0, column=2)
                    e2.grid(row=1, column=2)
                    b1=Button(s8,text=" Back ",command=lambda:[s7.deiconify(),s8.destroy()],bd=4)
                    b1.grid(row=2 , column=1)
                    b2=Button(s8,text=" Submit ",command=verify,bd=4)
                    b2.grid(row=2 , column=2)
                    
                    s8.protocol("WM_DELETE_WINDOW", on_closing)
                    s8.resizable(False, False)
                    s8.mainloop()
                            
            elif(lev1.get()=="Cash on Delivery"):
                    c=messagebox.askyesno("Burger Therapy","Are You Sure?")
                    if(c==True):
                            print(finalnumber , TC)
                            paid="Cash on Delivery"
                            solddataa=str(solddata)
                            
                            cursor.execute("SELECT points from customers where mobno = ?" , (finalnumber,))
                            details=cursor.fetchall()
                            a=int(details[0][0])
                            totalpoints=a
                            
                            sql = "INSERT INTO sold (mobno , total , payment , cardno, cookinginstructions ,points,solddata,dateoforder,currenttime,billno) VALUES (?,?,?,?,?,?,?,?,?,?)"
                            val = (finalnumber , TC , paid , "NA", instructions.get(),totalpoints,solddataa,DateofOrder,current_time,billno)
                            conn.execute(sql, val)
                            conn.commit()

                            a=totalpoints+int(TC*0.07)
                            conn.execute("UPDATE customers set points=? WHERE mobno =?",(a,finalnumber))
                            conn.commit()

                            aa=('%.2f' %TC)
                            
                            finel="Order Placed \n"+"Total Amount: Rs."+str(aa)       
                            messagebox.showinfo("Burger Therapy", finel)
                            
                            s7.destroy()
                            login(finalnumber)
                    else:
                            pass
                            
            elif(lev1.get()=="Debit Card"):
                    def on_closing():
                            s7.deiconify()
                            s8.destroy()
                    def verify():
                            if(len(e1.get())>=16 and len(e1.get())<=19 and len(e2.get())==3):
                                    try:
                                            cc=int(e1.get())
                                            ps=int(e2.get())
                                            print("finalnumber,cc,ps",finalnumber,cc,ps)
                                            paid="Debit Card"
                                            solddataa=str(solddata)
                                            
                                            cursor.execute("SELECT points from customers where mobno = ?" , (finalnumber,))
                                            details=cursor.fetchall()
                                            a=int(details[0][0])
                                            totalpoints=a
                                            sql = "INSERT INTO sold (mobno , total , payment , cardno, cookinginstructions ,points,solddata,dateoforder,currenttime,billno) VALUES (?,?,?,?,?,?,?,?,?,?)"
                                            val = (finalnumber , TC , paid , e1.get(), instructions.get(),totalpoints,solddataa,DateofOrder,current_time,billno)
                                            conn.execute(sql, val)
                                            conn.commit()

                                            a=totalpoints+int(TC*0.07)
                                            conn.execute("UPDATE customers set points=? WHERE mobno =?",(a,finalnumber))
                                            conn.commit()
                                            aa=('%.2f' %TC)

                                            s8.destroy()
                                            s7.deiconify()

                                            finel="Order Placed \n"+"Total Amount: Rs."+str(aa)     
                                            messagebox.showinfo("Burger Therapy", finel)
                                            
                                            s7.destroy()
                                            login(finalnumber)
                                            
                                    except:
                                            messagebox.showinfo("Burger Therapy", "InValid Input")
                                            e1.delete(0,END)
                                            e1.insert(0,"")
                                            e2.delete(0,END)
                                            e2.insert(0,"")
                            else:
                                    messagebox.showinfo("Burger Therapy", "InValid Input")
                                    e1.delete(0,END)
                                    e1.insert(0,"")
                                    e2.delete(0,END)
                                    e2.insert(0,"")
                    s7.withdraw()
                    s8 = Tk()
                    s8.geometry("325x90")
                    s8.title("Burger Therapy - Payment")
                    Label(s8, text="Debit Card",bd=2).grid(row=0, column=1)
                    Label(s8, text="Pin",bd=2).grid(row=1, column=1)


                    e1 = Entry(s8,bd=2)
                    e2 = Entry(s8,bd=2,show='*')
                    
                    e1.grid(row=0, column=2)
                    e2.grid(row=1, column=2)
                    b1=Button(s8,text=" Back ",command=lambda:[s7.deiconify(),s8.destroy()],bd=4)
                    b1.grid(row=2 , column=1)
                    b2=Button(s8,text=" Submit ",command=verify,bd=4)
                    b2.grid(row=2 , column=2)
                    
                    s8.protocol("WM_DELETE_WINDOW", on_closing)
                    s8.resizable(False, False)
                    s8.mainloop()
            else:
                    pass
                
        else:
                print("Print checkbox Selected")
                cursor.execute("select points from customers where mobno = ?" , (finalnumber,))
                details=cursor.fetchall()
                tc1=float(TC*.80)
                tc2=float(TC*.20)
                points=int(int(details[0][0])/10)
                print(TC,tc1 , tc2 , points)
                if(tc1>points):
                        tc1=tc1-points
                        TC= tc1+tc2
                        points=int(details[0][0])-(points*10)
                        print("if",points,TC)
                else:
                        points=(points-tc1)*10
                        tc1=0
                        TC=tc2
                        print("else",points,TC)

                print(lev1.get())

                if(lev1.get()=="Credit Card"):
                        def on_closing():
                                s7.deiconify()
                                s8.destroy()
                        def verify():
                                if(len(e1.get())>=16 and len(e1.get())<=19 and len(e2.get())==3):
                                        try:
                                                cursor.execute("select points from customers where mobno = ?" , (finalnumber,))
                                                details=cursor.fetchall()
                                                pointsinitial=(details[0][0])+"points"
                                                
                                                cc=int(e1.get())
                                                ps=int(e2.get())
                                                print("finalnumber,cc,ps",finalnumber,cc,ps)
                                                paid="Credit Card"
                                                solddataa=str(solddata)
                                                
                                                sql = "INSERT INTO sold (mobno , total , payment , cardno, cookinginstructions ,points,solddata,dateoforder,currenttime,billno) VALUES (?,?,?,?,?,?,?,?,?,?)"
                                                val = (finalnumber , TC , paid , e1.get(), instructions.get(),pointsinitial,solddataa,DateofOrder,current_time,billno)
                                                conn.execute(sql, val)
                                                conn.commit()
                                                
                                                conn.execute("UPDATE customers set points=? WHERE mobno =?",(points,finalnumber))
                                                conn.commit()

                                                aa=('%.2f' %TC)

                                                s8.destroy()
                                                s7.deiconify()

                                                finel="Order Placed \n"+"Total Amount: Rs."+str(aa)       
                                                messagebox.showinfo("Burger Therapy", finel)
                                                
                                                
                                                s7.destroy()
                                                login(finalnumber)
                                                
                                         
                                        except:
                                                messagebox.showinfo("Burger Therapy", "Invalid Input")
                                                e1.delete(0,END)
                                                e1.insert(0,"")
                                                e2.delete(0,END)
                                                e2.insert(0,"")
                                else:    
                                        messagebox.showinfo("Burger Therapy", "InValid Input")
                                        e1.delete(0,END)
                                        e1.insert(0,"")
                                        e2.delete(0,END)
                                        e2.insert(0,"")
                        s7.withdraw()
                        s8 = Tk()
                        s8.geometry("325x90")
                        s8.title("Burger Therapy - Payment")
                        Label(s8, text="Credit Card",bd=2).grid(row=0, column=1)
                        Label(s8, text="Pin",bd=2).grid(row=1, column=1)


                        e1 = Entry(s8,bd=2)
                        e2 = Entry(s8,bd=2,show='*')
                        
                        e1.grid(row=0, column=2)
                        e2.grid(row=1, column=2)
                        b1=Button(s8,text=" Back ",command=lambda:[s7.deiconify(),s8.destroy()],bd=4)
                        b1.grid(row=2 , column=1)
                        b2=Button(s8,text=" Submit ",command=verify,bd=4)
                        b2.grid(row=2 , column=2)
                        
                        s8.protocol("WM_DELETE_WINDOW", on_closing)
                        s8.resizable(False, False)
                        s8.mainloop()
                        
                elif(lev1.get()=="Cash on Delivery"):
                        c=messagebox.askyesno("Burger Therapy","Are You Sure?")
                        if(c==True):
                                print(finalnumber , TC)
                                paid="Cash on Delivery"
                                solddataa=str(solddata)
                                
                                cursor.execute("select points from customers where mobno = ?" , (finalnumber,))
                                details=cursor.fetchall()
                                pointsinitial=(details[0][0])+"points"

                                sql = "INSERT INTO sold (mobno , total , payment , cardno, cookinginstructions ,points,solddata,dateoforder,currenttime,billno) VALUES (?,?,?,?,?,?,?,?,?,?)"
                                val = (finalnumber , TC , paid , "NA", instructions.get(),pointsinitial,solddataa,DateofOrder,current_time,billno)
                                conn.execute(sql, val)
                                conn.commit()

                                conn.execute("UPDATE customers set points=? WHERE mobno =?",(points,finalnumber))
                                conn.commit()

                                TC=('%.2f' %TC)
                                
                                finel="Order Placed \n"+"Total Amount: Rs."+str(TC)       
                                messagebox.showinfo("Burger Therapy", finel)
                                
                                s7.destroy()
                                login(finalnumber)

                        else:
                                pass

                elif(lev1.get()=="Debit Card"):
                        def on_closing():
                                s7.deiconify()
                                s8.destroy()
                        def verify():
                                if(len(e1.get())>=16 and len(e1.get())<=19 and len(e2.get())==3):
                                        try:
                                                cc=int(e1.get())
                                                ps=int(e2.get())
                                                print("finalnumber,cc,ps",finalnumber,cc,ps)
                                                paid="Debit Card"
                                                solddataa=str(solddata)
                                                
                                                cursor.execute("select points from customers where mobno = ?" , (finalnumber,))
                                                details=cursor.fetchall()
                                                pointsinitial=(details[0][0])+"points"
                                    
                                                
                                                sql = "INSERT INTO sold (mobno , total , payment , cardno, cookinginstructions ,points,solddata,dateoforder,currenttime,billno) VALUES (?,?,?,?,?,?,?,?,?,?)"
                                                val = (finalnumber , TC , paid , e1.get(), instructions.get(),pointsinitial,solddataa,DateofOrder,current_time,billno)
                                                conn.execute(sql, val)
                                                conn.commit()

                                                
                                                conn.execute("UPDATE customers set points=? WHERE mobno =?",(points,finalnumber))
                                                conn.commit()

                                                aa=('%.2f' %TC)

                                                s8.destroy()
                                                s7.deiconify()
                                                
                                                finel="Order Placed \n"+"Total Amount: Rs."+str(aa)     
                                                messagebox.showinfo("Burger Therapy", finel)
                                                
                                                
                                                s7.destroy()
                                                login(finalnumber)
                                                        
                                        except:
                                                messagebox.showinfo("Burger Therapy", "InValid Input")
                                                e1.delete(0,END)
                                                e1.insert(0,"")
                                                e2.delete(0,END)
                                                e2.insert(0,"")
                                else:
                                        messagebox.showinfo("Burger Therapy", "InValid Input")
                                        e1.delete(0,END)
                                        e1.insert(0,"")
                                        e2.delete(0,END)
                                        e2.insert(0,"")
                        s7.withdraw()
                        s8 = Tk()
                        s8.geometry("325x90")
                        s8.title("Burger Therapy - Payment")
                        Label(s8, text="Debit Card",bd=2).grid(row=0, column=1)
                        Label(s8, text="Pin",bd=2).grid(row=1, column=1)


                        e1 = Entry(s8,bd=2)
                        e2 = Entry(s8,bd=2,show='*')
                        
                        e1.grid(row=0, column=2)
                        e2.grid(row=1, column=2)
                        b1=Button(s8,text=" Back ",command=lambda:[s7.deiconify(),s8.destroy()],bd=4)
                        b1.grid(row=2 , column=1)
                        b2=Button(s8,text=" Submit ",command=verify,bd=4)
                        b2.grid(row=2 , column=2)
                        
                        s8.protocol("WM_DELETE_WINDOW", on_closing)
                        s8.resizable(False, False)
                        s8.mainloop()
                        
                else:
                        pass

                    
    s7=Tk()
    s7.geometry("1080x720")
    s7.title("Burger Therapy")

    # Show image using label
    bg = PhotoImage(file = "background.png")
    label1 = Label( s7, image = bg)
    label1.place(x = 0, y = 0)

    b1=Button(s7,text=" Home ",command=lambda:[s7.destroy(),login(finalnumber)],bd=4,bg="#78543c",fg="#ffffff",font=("cooper black",16))
    b1.place(relx=1, x=-2, y=2, anchor=NE)

    frame=LabelFrame(s7,text="Burger Therapy",font=("cooper black",16) , padx=50 , pady=50,bg="#d1b493")
    frame.grid( padx=250 , pady=200)


    lev1=StringVar()

    lab1=Label(frame,text="Cooking Instructions",bd=4,bg="#78543c",fg="#ffffff",font=("cooper black",16))
    lab1.grid(row=1 , column=0)
    lab1=Label(frame,bg="#d1b493")                       
    lab1.grid(row=1 , column=1)
    name =StringVar()
    instructions = Entry(frame, width = 20, textvariable = name , bd=4,font=("cooper black",16))
    instructions.grid(row = 1,column = 2)



    lab1=Label(frame,font=("cooper black",16),bg="#d1b493")                       
    lab1.grid(row=2 , column=2)

    # Create Dropdown menu
    options = ["Cash on Delivery","Credit Card","Debit Card"]
      
    lev1 = StringVar()
    lev1.set( "Credit Card" )

    lab1=Label(frame,text="Payment",bd=4,bg="#78543c",fg="#ffffff",font=("cooper black",16))                       
    lab1.grid(row=3 , column=0)
    lab1=Label(frame,bg="#d1b493")                       
    lab1.grid(row=3 , column=1)
    drop = OptionMenu( frame , lev1 , *options )
    drop.grid(row=3 , column=2)



    lab1=Label(frame,bg="#d1b493")                      
    lab1.grid(row=4 , column=1)

    cursor.execute("select points from customers where mobno = ?" , (finalnumber,))                   
    details=cursor.fetchall()
    f="Use " +details[0][0]+ " Points " 
    lab1=Label(frame,text=f,bd=4,bg="#78543c",fg="#ffffff",font=("cooper black",16))
    lab1.grid(row=5 , column=0)
    lab1=Label(frame,bg="#d1b493")                       
    lab1.grid(row=5 , column=1)

    CheckVar1 = IntVar()
    C1 = Checkbutton(frame, variable = CheckVar1, onvalue = 1, offvalue = 0,bg="#d1b493",activebackground="#d1b493",width=15)
    C1.grid(row = 5,column = 2)
    
    b2=Button(frame,text=" Submit ",command=submit,bd=4,bg="#78543c",fg="#ffffff",font=("cooper black",16))
    b2.grid(row=6 , column=1)

    s7.resizable(False, False)
    s7.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
        pass
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def order(finalnumber):
    
    s6 = Tk()
    s6.geometry("1500x720")# Geometric measurement of the system created
    s6.title("Burger Therapy")
    s6.resizable(False, False)
    s6.configure(background='#d6b594')   # Background Color
    
    b1image = PhotoImage(file = "back.png")
    b1=Button(s6,image = b1image,command=lambda:[s6.destroy(),login(finalnumber)],bg="#d6b594",bd=4,fg="#d6b594",activebackground="#d5b493",font=("perpetua",16))
    b1.place(relx=1, x=-2, y=2, anchor=NE)
        
    Tops = Frame(s6, width=1280, height=100, bd=12, relief="raise")
    Tops.pack(side=TOP)
        
    f1 = Frame(s6, width=640, height=620, bd=8, relief="raise")
    f1.pack(side=LEFT)

    f2 = Frame(s6, width=640, height=620, bd=9, relief="raise")
    f2.pack(side=RIGHT)

    f1a = Frame(f1, width=640, height=620, bd=6, relief="raise")
    f1a.pack(side=TOP)

    ft2 = Frame(f2, width=440, height=450, bd=12, relief="raise")
    ft2.pack()

    fb2 = Frame(f2, width=440, height=750, bd=16, relief="raise")
    fb2.pack()
    
    f1aa = Frame(f1a, width=320, height=620, bd=16, relief="raise")
    f1aa.pack(side=LEFT)

    f1ab = Frame(f1a, width=320, height=620, bd=16, relief="raise")
    f1ab.pack(side=RIGHT)


    # ============================ Configuration set background black ==================================================

    Tops.configure(background='white')
    f1.configure(background='white')
    f2.configure(background='white')

    # =========================================== Label Set on Top to Restaurant MS =================================

    lblInfo = Label(Tops, font=('perpetua', 65, 'bold'), text=" Burger Therapy ", bd=10)
    lblInfo.grid(row=0, column=0)

    # ================================================ Exit the Main frame ===============================================
    def pay():
        try: 
            Item1 =  int(E_paneer_burger.get())
            Item2 =  int(E_swissy_mushi_burger.get())
            Item3 =  int(E_veg_exotic_burger.get())
            Item4 =  int(E_buffmaster_burger.get())
            Item5 =  int(E_italian_burger.get())
            Item6 =  int(E_beat_down_burger.get())
            Item7 =  int(E_kung_fu_paneer_burger.get())
            Item8 =  int(E_maharaja_jalapeno_burger.get())
            Item9 =  int(E_big_crunch_burger.get())
            Item10 = int(E_mumbai_special_burger.get())
            Item11 = int(E_deadpool_burger.get())
            Item12 = int(E_chipotle_chicken_burger.get())
                       
            Item13 = int(E_big_fat_man_burger.get())
            Item14 = int(E_juicy_chicken_cheese_burger.get())
            Item15 = int(E_chicken_masala_burger.get())
            Item16 = int(E_aquaman_burger.get())
            Item17 = int(E_nachos_chicken_burger.get())
            Item18 = int(E_chocolate_drink.get())
            Item19 = int(E_lemonade.get())
            Item20 = int(E_coke.get())
            Item21 = int(E_sprite.get())
            Item22 = int(E_mountain_dew.get())
            Item23 = int(E_thumbs_up.get())
            Item24 = int(E_red_bull.get())

            solddata=[Item1,Item2,Item3,Item4,Item5,Item6,Item7,Item8,Item9,Item10,Item11,Item12,
                      Item13,Item14,Item15,Item16,Item17,Item18,Item19,Item20,Item21,Item22,Item23,Item24]          

            pricefood =(Item1 * 90) + (Item2 * 120) + (Item3 * 130) + (Item4 *150) + (Item5 * 150) + (Item6 * 180) +(Item7 * 180) + (Item8 * 200) + (Item9 * 180) + (Item10 * 190)+\
             (Item11 * 150)+ (Item12 *150)+ (Item13 * 170) + (Item14 * 180) + (Item15 * 200) + (Item16 * 220)+ (Item17 * 230)+ (Item18 * 50) + (Item19 * 30) + (Item20 * 60)+\
             (Item21 * 60)+ (Item22 * 60)+ (Item23 * 60)+ (Item24 * 60)
                
            Price = "Rs "+ str(pricefood)
            pricefood=float(pricefood)
            
            Tax1 = "Rs "+ str(round((pricefood + 0.15)*0.05))
            ServiceCharge.set(Tax1)
            TT = ((pricefood + 0.15)*0.05)
            TC = round((pricefood + 0.15) + TT)
            print(TC)

            if(TC!=0):
                    c=messagebox.askyesno("Burger Therapy","Are You Sure?")
                    if(c==True):
                                s6.destroy()
                                
                                payment(TC,finalnumber,solddata)
                                print("TC notZero")
            else:
                   messagebox.showinfo("Burger Therapy", "Select Atleast One Item") 
                            
        except:
            messagebox.showinfo("Burger Therapy", "Enter a Vaalid Quantity")
    #======================================================== Cost of Items ====================================

    def sum():
        try:
            Item1 =  int(E_paneer_burger.get())
            Item2 =  int(E_swissy_mushi_burger.get())
            Item3 =  int(E_veg_exotic_burger.get())
            Item4 =  int(E_buffmaster_burger.get())
            Item5 =  int(E_italian_burger.get())
            Item6 =  int(E_beat_down_burger.get())
            Item7 =  int(E_kung_fu_paneer_burger.get())
            Item8 =  int(E_maharaja_jalapeno_burger.get())
            Item9 =  int(E_big_crunch_burger.get())
            Item10 = int(E_mumbai_special_burger.get())
            Item11 = int(E_deadpool_burger.get())
            Item12 = int(E_chipotle_chicken_burger.get())
            Item13 = int(E_big_fat_man_burger.get())
            Item14 = int(E_juicy_chicken_cheese_burger.get())
            Item15 = int(E_chicken_masala_burger.get())
            Item16 = int(E_aquaman_burger.get())
            Item17 = int(E_nachos_chicken_burger.get())
            Item18 = int(E_chocolate_drink.get())
            Item19 = int(E_lemonade.get())
            Item20 = int(E_coke.get())
            Item21 = int(E_sprite.get())
            Item22 = int(E_mountain_dew.get())
            Item23 = int(E_thumbs_up.get())
            Item24 = int(E_red_bull.get())
            

            pricefood =(Item1 * 90) + (Item2 * 120) + (Item3 * 130) + (Item4 *150) + (Item5 * 150) + (Item6 * 180) +(Item7 * 180) + (Item8 * 200) + (Item9 * 180) + (Item10 * 190)+\
             (Item11 * 150)+ (Item12 *150)+ (Item13 * 170) + (Item14 * 180) + (Item15 * 200) + (Item16 * 220)+ (Item17 * 230)+ (Item18 * 50) + (Item19 * 30) + (Item20 * 60)+\
             (Item21 * 60)+ (Item22 * 60)+ (Item23 * 60)+ (Item24 * 60)

            Price = "Rs "+ str(pricefood)
            pricefood=float(pricefood)
            
            Tax1 = "Rs "+ str(round((pricefood + 0.15)*0.05))
            ServiceCharge.set(Tax1)
            TT = ((pricefood + 0.15)*0.05)
            TC = "Rs "+ str(round((pricefood + 0.15) + TT))
            TotalCost.set(TC)
            
        except:
            messagebox.showinfo("Burger Therapy", "Enter a Valid Quantity")


    # ================================================== Reset the Entries Module =========================================
    def reset():
        TotalCost.set("")
        ServiceCharge.set("")
        txtReceipt.delete("1.0", END)

        E_paneer_burger.set("0")
        E_swissy_mushi_burger.set("0")
        E_veg_exotic_burger.set("0")
        E_buffmaster_burger.set("0")
        E_italian_burger.set("0")
        E_beat_down_burger.set("0")
        E_kung_fu_paneer_burger.set("0")
        E_maharaja_jalapeno_burger.set("0")
        E_big_crunch_burger.set("0")
        E_mumbai_special_burger.set("0")
        E_deadpool_burger.set("0")
        E_chipotle_chicken_burger.set("0")

        E_big_fat_man_burger.set("0")
        E_juicy_chicken_cheese_burger.set("0")
        E_chicken_masala_burger.set("0")
        E_aquaman_burger.set("0")
        E_nachos_chicken_burger.set("0")
        E_chocolate_drink.set("0")
        E_lemonade.set("0")
        E_coke.set("0")
        E_sprite.set("0")
        E_mountain_dew.set("0")
        E_thumbs_up.set("0")
        E_red_bull.set("0")
   
   
    # ====================================================== Receipt Module ======================
    def viewcart():
        sum()
        global billno,current_time,DateofOrder
        txtReceipt.delete("1.0", END)
        x = random.randint(1000, 500890)
        billno = "Bill No. " + str(x)
        t = time.localtime()
        current_time = time.strftime("%H:%M", t)
        DateofOrder=(time.strftime("%d/%m/%y"))
        print(type(DateofOrder))
        print(DateofOrder)
        #Adding Customer Name to Bill and making name length=10
        cursor.execute("SELECT fname from customers where mobno = ?" , (finalnumber,))
        details=cursor.fetchall()
        billname=str(details[0][0])
        if(len(billname)<=10):
            j=int(10-len(billname))
        if(j!=0):
            for k in range(j):
                billname=billname+" "
        print(len(billname))
        txtReceipt.insert(END, '\t\t     '+'Burger Therapy' +"\n")
        txtReceipt.insert(END, 'Name: '+billname+ '\t\t\t\t Mobile No.: ' + str(finalnumber)+"\n")
        txtReceipt.insert(END, billno + '\t\t         Time: '+current_time+'\t\t\t  Date: ' + DateofOrder+"\n")
        txtReceipt.insert(END, "----------------------------------------------------------------------------------------------\n")
        txtReceipt.insert(END, "Items\t\t\t\t" + "Quantity\t\t"+"Total\n\n")
        
        if(int(E_paneer_burger.get())>=1):
            txtReceipt.insert(END, 'Paneer Burger \t\t\t\t     ' + E_paneer_burger.get() + "\t\t" + "Rs " + str(int(E_paneer_burger.get())*90) + "\n")
        if(int(E_swissy_mushi_burger.get())>=1):
            txtReceipt.insert(END, 'Swissy Mushi Burger \t\t\t\t     ' + E_swissy_mushi_burger.get() + "\t\t" + "Rs " + str(int(E_swissy_mushi_burger.get())*120) + "\n")
        if(int(E_veg_exotic_burger.get())>=1):
            txtReceipt.insert(END, 'Veg Exotic Burger \t\t\t\t     ' + E_veg_exotic_burger.get() + "\t\t" + "Rs " + str(int(E_veg_exotic_burger.get())*130) + "\n")
        if(int(E_buffmaster_burger.get())>=1):
            txtReceipt.insert(END, 'Buffmaater Burger \t\t\t\t     ' + E_buffmaster_burger.get() + "\t\t" + "Rs " + str(int(E_buffmaster_burger.get())*150) + "\n")
        if(int(E_italian_burger.get())>=1):
            txtReceipt.insert(END, 'Italian Burger \t\t\t\t     ' + E_italian_burger.get() + "\t\t" + "Rs " + str(int(E_italian_burger.get())*150) + "\n")
        if(int(E_beat_down_burger.get())>=1):
            txtReceipt.insert(END, 'Beat Down Burger \t\t\t\t     ' + E_beat_down_burger.get() + "\t\t" + "Rs " + str(int(E_beat_down_burger.get())*180) + "\n")
        if(int(E_kung_fu_paneer_burger.get())>=1):
            txtReceipt.insert(END, 'Kung Fu Paneer Burger \t\t\t\t     ' + E_kung_fu_paneer_burger.get() + "\t\t" + "Rs " + str(int(E_kung_fu_paneer_burger.get())*180) + "\n")
        if(int(E_maharaja_jalapeno_burger.get())>=1):
            txtReceipt.insert(END, 'Maharaja Jalapeno Burger\t\t\t\t     ' + E_maharaja_jalapeno_burger.get() + "\t\t" + "Rs " + str(int(E_maharaja_jalapeno_burger.get())*200) + "\n")        
        if(int(E_big_crunch_burger.get())>=1):
            txtReceipt.insert(END, 'Big Crunch Burger \t\t\t\t     ' + E_big_crunch_burger.get() + "\t\t" + "Rs " + str(int(E_big_crunch_burger.get())*180) + "\n") 
        if(int(E_mumbai_special_burger.get())>=1):
            txtReceipt.insert(END, 'Mumbai Special Burger \t\t\t\t     ' + E_mumbai_special_burger.get() + "\t\t" + "Rs " + str(int(E_mumbai_special_burger.get())*190) + "\n") 
        if(int(E_deadpool_burger.get())>=1):
            txtReceipt.insert(END, 'Deadpool Burger \t\t\t\t     ' + E_deadpool_burger.get() + "\t\t" + "Rs " + str(int(E_deadpool_burger.get())*150) + "\n") 
        if(int(E_chipotle_chicken_burger.get())>=1):
            txtReceipt.insert(END, 'Chipotle Chicken Burger \t\t\t\t     ' + E_chipotle_chicken_burger.get() + "\t\t" + "Rs " + str(int(E_chipotle_chicken_burger.get())*150) + "\n") 

        if(int(E_big_fat_man_burger.get())>=1):
            txtReceipt.insert(END, 'Big fatman Burger \t\t\t\t     ' + E_big_fat_man_burger.get() + "\t\t" + "Rs " + str(int(E_big_fat_man_burger.get())*170) + "\n")    
        if(int(E_juicy_chicken_cheese_burger.get())>=1):
            txtReceipt.insert(END, 'Juicy Chicken Cheese Burger \t\t\t\t     ' + E_juicy_chicken_cheese_burger.get() + "\t\t" + "Rs " + str(int(E_juicy_chicken_cheese_burger.get())*180) + "\n")       
        if(int(E_chicken_masala_burger.get())>=1):
            txtReceipt.insert(END, 'Chicken Masala Burger \t\t\t\t     ' + E_chicken_masala_burger.get() + "\t\t" + "Rs " + str(int(E_chicken_masala_burger.get())*200) + "\n")    
        if(int(E_aquaman_burger.get())>=1):
            txtReceipt.insert(END, 'Aquaman Burger \t\t\t\t     ' + E_aquaman_burger.get() + "\t\t" + "Rs " + str(int(E_aquaman_burger.get())*220) + "\n")
        if(int(E_nachos_chicken_burger.get())>=1):
            txtReceipt.insert(END, 'Nachos Chicken Burger \t\t\t\t     ' + E_nachos_chicken_burger.get() + "\t\t" + "Rs " + str(int(E_nachos_chicken_burger.get())*230) + "\n")
        if(int(E_chocolate_drink.get())>=1):
            txtReceipt.insert(END, 'Chocolate Drink \t\t\t\t     ' + E_chocolate_drink.get() + "\t\t" + "Rs " + str(int(E_chocolate_drink.get())*50) + "\n")
        if(int(E_lemonade.get())>=1):
            txtReceipt.insert(END, 'Lemonade \t\t\t\t     ' + E_lemonade.get() + "\t\t" + "Rs " + str(int(E_lemonade.get())*30) + "\n")
        if(int(E_coke.get())>=1):
            txtReceipt.insert(END, 'Coke \t\t\t\t     ' + E_coke.get() + "\t\t" + "Rs " + str(int(E_coke.get())*60) + "\n")
        if(int(E_sprite.get())>=1):
            txtReceipt.insert(END, 'Sprite \t\t\t\t     ' + E_sprite.get() + "\t\t" + "Rs " + str(int(E_sprite.get())*60) + "\n")
        if(int(E_mountain_dew.get())>=1):
            txtReceipt.insert(END, 'Mountain Dew \t\t\t\t     ' + E_mountain_dew.get() + "\t\t" + "Rs " + str(int(E_mountain_dew.get())*60) + "\n")
        if(int(E_thumbs_up.get())>=1):
            txtReceipt.insert(END, 'Thumbs UP \t\t\t\t     ' + E_thumbs_up.get() + "\t\t" + "Rs " + str(int(E_thumbs_up.get())*60) + "\n")
        if(int(E_red_bull.get())>=1):
            txtReceipt.insert(END, 'Red Bull \t\t\t\t     ' + E_red_bull.get() + "\t\t" + "Rs " + str(int(E_red_bull.get())*60) + "\n")
            
        txtReceipt.insert(END, 'GST Charge (5%)\t\t\t\t\t\t' + ServiceCharge.get() + "\t\tTotal Cost:\t\t\t\t\t\t" + TotalCost.get() + "\n")

    # ======================================================= Variables ===============================================
   
    Receipt_Ref = StringVar()
    PaidTax = StringVar()
    SubTotal = StringVar()
    TotalCost = StringVar()
    CostofCakesandDrinks = StringVar()
    CostofFood = StringVar()
    ServiceCharge = StringVar()

    E_paneer_burger = StringVar()
    E_swissy_mushi_burger = StringVar()
    E_veg_exotic_burger = StringVar()
    E_buffmaster_burger = StringVar()
    E_italian_burger = StringVar()
    E_beat_down_burger = StringVar()
    E_kung_fu_paneer_burger = StringVar()
    E_maharaja_jalapeno_burger = StringVar()
    E_big_crunch_burger = StringVar()
    E_mumbai_special_burger = StringVar()
    E_deadpool_burger = StringVar()
    E_chipotle_chicken_burger = StringVar()

    E_big_fat_man_burger = StringVar()
    E_juicy_chicken_cheese_burger = StringVar()
    E_chicken_masala_burger = StringVar()
    E_aquaman_burger = StringVar()
    E_nachos_chicken_burger = StringVar()
    E_chocolate_drink = StringVar()
    E_lemonade = StringVar()
    E_coke = StringVar()
    E_sprite = StringVar()
    E_mountain_dew= StringVar()
    E_thumbs_up = StringVar()
    E_red_bull = StringVar()

    
    E_paneer_burger.set("0")
    E_swissy_mushi_burger.set("0")
    E_veg_exotic_burger.set("0")
    E_buffmaster_burger.set("0")
    E_italian_burger.set("0")
    E_beat_down_burger.set("0")
    E_kung_fu_paneer_burger.set("0")
    E_maharaja_jalapeno_burger.set("0")
    E_big_crunch_burger.set("0")
    E_mumbai_special_burger.set("0")
    E_deadpool_burger.set("0")
    E_chipotle_chicken_burger.set("0")

    E_big_fat_man_burger.set("0")
    E_juicy_chicken_cheese_burger.set("0")
    E_chicken_masala_burger.set("0")
    E_aquaman_burger.set("0")
    E_nachos_chicken_burger.set("0")
    E_chocolate_drink.set("0")
    E_lemonade.set("0")
    E_coke.set("0")
    E_sprite.set("0")
    E_mountain_dew.set("0")
    E_thumbs_up.set("0")
    E_red_bull.set("0")

    # ====================================== 1st Part =======================================================

    paneer_burger = Label(f1aa, text="Paneer Burger \t" , font=('perpetua', 18, 'bold')).grid(row=0, sticky=W)

    swissy_mushi_burger = Label(f1aa, text="Swissy Mushi Burger\t" , font=('perpetua', 18, 'bold')).grid(row=1, sticky=W)

    veg_exotic_burger = Label(f1aa, text="Veg Exotic Burger \t" , font=('perpetua', 18, 'bold')).grid(row=2, sticky=W)
                    
    buffmaster_burger = Label(f1aa, text="Buffmaster Burger \t" , font=('perpetua', 18, 'bold')).grid(row=3, sticky=W)

    italian_burger = Label(f1aa, text="Italian Burger\t" , font=('perpetua', 18, 'bold')).grid(row=4, sticky=W)

    beat_down_burger = Label(f1aa, text="Beat Down Burger\t" , font=('perpetua', 18, 'bold')).grid(row=5, sticky=W)

    kung_fu_paneer_burger = Label(f1aa, text="Kung Fu Paneer Burger\t" , font=('perpetua', 18, 'bold')).grid(row=6, sticky=W)

    maharaja_jalapeno_burger = Label(f1aa, text="Maharaja Jalopeno Burger\t" , font=('perpetua', 18, 'bold')).grid(row=7, sticky=W)
    
    big_crunch_burger = Label(f1aa, text="Big Crunch Burger \t" , font=('perpetua', 18, 'bold')).grid(row=8, sticky=W)
    
    mumbai_special_burger = Label(f1aa, text="Mumbai Special Burger  \t" , font=('perpetua', 18, 'bold')).grid(row=9, sticky=W)
    
    deadpool_burger = Label(f1aa, text="Deadpool Burger \t" , font=('perpetua', 18, 'bold')).grid(row=10, sticky=W)
    
    chipotle_chicken_burger = Label(f1aa, text="Chipotle Chicken Burger \t" , font=('perpetua', 18, 'bold')).grid(row=11, sticky=W)
    
    # ====================================== 2nd Part ================================================

    big_fat_man_burger = Label(f1ab, text="Big Fatman Burger\t" , font=('perpetua', 18, 'bold')).grid(row=0, sticky=W)

    juicy_chicken_cheese_burger = Label(f1ab, text="Juicy Chicken Cheese Burger\t" , font=('perpetua', 18, 'bold')).grid(row=1, sticky=W)

    chicken_masala_burger = Label(f1ab, text="Chicken Masala Burger \t" , font=('perpetua', 18, 'bold')).grid(row=2, sticky=W)

    aquaman_burger = Label(f1ab, text="Aquaman Burger \t" , font=('perpetua', 18, 'bold')).grid(row=3, sticky=W)

    nachos_chicken_burger = Label(f1ab, text="Nachos Chicken Burger\t" , font=('perpetua', 18, 'bold')).grid(row=4, sticky=W)

    chocolate_drink = Label(f1ab, text="Chocolate Drink\t" , font=('perpetua', 18, 'bold')).grid(row=5, sticky=W)

    lemonade = Label(f1ab, text="Lemonade \t" , font=('perpetua', 18, 'bold')).grid(row=6, sticky=W)

    coke = Label(f1ab, text="Can of Coke (90ml)\t" , font=('perpetua', 18, 'bold')).grid(row=7, sticky=W)

    sprite = Label(f1ab, text="Can of Sprite (90ml)\t" , font=('perpetua', 18, 'bold')).grid(row=8, sticky=W)
    
    mountain_dew = Label(f1ab, text="Can of Mountain Dew (90ml)\t" , font=('perpetua', 18, 'bold')).grid(row=9, sticky=W)

    thumbs_up = Label(f1ab, text="Can of Thumbs UP (90ml)\t" , font=('perpetua', 18, 'bold')).grid(row=10, sticky=W)

    red_bull = Label(f1ab, text="Can of Red Bull (90ml)\t" , font=('perpetua', 18, 'bold')).grid(row=11, sticky=W)
    

    # ====================================== Entry Widget 1st Part ===================================================

    txtpaneer_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_paneer_burger)
    txtpaneer_burger.grid(row=0, column=1)    
    txtswissy_mushi_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_swissy_mushi_burger)
    txtswissy_mushi_burger.grid(row=1, column=1)
    txtveg_exotic_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_veg_exotic_burger)
    txtveg_exotic_burger.grid(row=2, column=1)
    txtbuffmaster_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_buffmaster_burger)
    txtbuffmaster_burger.grid(row=3, column=1)
    txtitalian_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_italian_burger)
    txtitalian_burger.grid(row=4, column=1)
    txtbeat_down_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_beat_down_burger)
    txtbeat_down_burger.grid(row=5, column=1)
    txtkung_fu_paneer_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_kung_fu_paneer_burger)
    txtkung_fu_paneer_burger.grid(row=6, column=1)
    txtmaharaja_jalapeno_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_maharaja_jalapeno_burger)
    txtmaharaja_jalapeno_burger.grid(row=7, column=1)
    txtbig_crunch_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_big_crunch_burger)
    txtbig_crunch_burger.grid(row=8, column=1)
    txtmumbai_special_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_mumbai_special_burger)
    txtmumbai_special_burger.grid(row=9, column=1)
    txtdeadpool_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_deadpool_burger)
    txtdeadpool_burger.grid(row=10, column=1)
    txtchipotle_chicken_burger = Entry(f1aa, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_chipotle_chicken_burger)
    txtchipotle_chicken_burger.grid(row=11, column=1)
    

    # ====================================== Entry Widget 2nd Part ===================================================

    txtbig_fat_man_burger = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_big_fat_man_burger)
    txtbig_fat_man_burger.grid(row=0, column=1)
    
    txtjuicy_chicken_cheese_burger = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_juicy_chicken_cheese_burger)
    txtjuicy_chicken_cheese_burger.grid(row=1, column=1)
    
    txtchicken_masala_burger = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_chicken_masala_burger)
    txtchicken_masala_burger.grid(row=2, column=1)
    
    txtaquaman_burger = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_aquaman_burger)
    txtaquaman_burger.grid(row=3, column=1)
    
    txtnachos_chicken_burger = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_nachos_chicken_burger)
    txtnachos_chicken_burger.grid(row=4, column=1)
    
    txtchocolate_drink = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_chocolate_drink)
    txtchocolate_drink.grid(row=5, column=1)
    
    txtlemonade = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_lemonade)
    txtlemonade.grid(row=6, column=1)
    
    txtcoke = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_coke)
    txtcoke.grid(row=7, column=1)

    txtsprite = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_sprite)
    txtsprite.grid(row=8, column=1)

    txtmountain_dew = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_mountain_dew)
    txtmountain_dew.grid(row=9, column=1)
    
    txtthumbs_up = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_thumbs_up)
    txtthumbs_up.grid(row=10, column=1)

    txtred_bull = Entry(f1ab, font=('perpetua', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_red_bull)
    txtred_bull.grid(row=11, column=1)

    # ========================================== Receipt Information ====================================================

    lblReceipt = Label(ft2, font=('perpetua', 12, 'bold'), text="Receipt", bd=2, anchor='w')
    lblReceipt.grid(row=0, column=0, sticky=W)
    txtReceipt = Text(ft2, width=59, height=22, bg="white", bd=8, font=('perpetua', 11, 'bold'))
    txtReceipt.grid(row=1, column=0, sticky=W+E)        

    # ======================================Button===================================================

    menu = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('perpetua', 16, 'bold'), width=5,
                      text="Menu", command=lambda:[s6.destroy(),main_menu(finalnumber)]).grid(row=0, column=0, sticky=W+E+N+S)
    viewcart = Button(fb2,text="View Cart", padx=16, pady=1, bd=4, fg="black", font=('perpetua', 16, 'bold'), width=5,
                         command=viewcart).grid(row=0, column=1, sticky=W+E+N+S)
    reset = Button(fb2 ,text="Reset", padx=16, pady=1, bd=4, fg="black", font=('perpetua', 16, 'bold'), width=5,
                       command=reset).grid(row=0, column=2, sticky=W+E+N+S)
    paid = Button(fb2,text="Payment", padx=16, pady=1, bd=4, fg="black", font=('perpetua', 16, 'bold'), width=5,
                      command=pay).grid(row=0, column=3, sticky=W+E+N+S)
    
    s6.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu(finalnumber):
        s5 = Tk()
        s5.geometry("1080x720")
        s5.title("Burger Therapy - Menu")

        topframe = Frame(s5, bg="#d5b493")
        topframe.pack(side=TOP,fill=BOTH)
        
        lbl = Label(topframe,bg='#d5b493',fg='#d5b493')
        lbl.grid(row=0, column=0)
        lbl = Label(topframe, font=('perpetua', 35, 'bold'), text="aaaaaaaaaaaaaaaasaaaaaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=0)
        lblInfo = Label(topframe, font=('perpetua', 45, 'bold'), text=" MENU ", bd=10, relief="raise")
        lblInfo.grid(row=1, columnspan=2 , sticky='e')
        lbl = Label(topframe, font=('perpetua', 35, 'bold'), text="aaaaaaaaaasaaaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=3)
        
        b1image = PhotoImage(file = "back.png")
        b1=Button(topframe, image=b1image,command=lambda:[s5.destroy(),login(finalnumber)], bd=4,bg="#d6b594",fg="#d6b594",activebackground="#d5b493")
        b1.grid(row=1, column=3, sticky='e')
        
        lblInfo1 = Label(topframe,bg='#d5b493',fg='#d5b493')
        lblInfo1.grid(row=2, column=1)
        
        b2image = PhotoImage(file = "ordernow.png")
        b2=Button(topframe,image=b2image,command=lambda:[s5.destroy(),order(finalnumber)], bd=4,bg="#d6b594",fg="#d6b594",activebackground="#d5b493" )
        b2.grid(row=2, column=3, sticky='e')

        main_frame = Frame(s5, bg="#d5b493" , bd=10)
        main_frame.pack(fill=BOTH , expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side =LEFT , fill=BOTH , expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame , orient = VERTICAL , command = my_canvas.yview)
        my_scrollbar.pack(side =RIGHT , fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = Frame(my_canvas , bg="#d5b493" , bd=10)
        my_canvas.create_window((0,0), window=second_frame , anchor = "nw" )
        j=0

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

        abc = Label(second_frame, text="\t\t\t\t\tVEG ITEMS\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=0, sticky=W)

        abc = Label(second_frame, text="Panner Burger\t\t\t\t\t\t\t\tRs.90\t" , font=('perpetua', 18))
        abc.grid(row=1, sticky=W)
         
        abc = Label(second_frame, text="\t\t\t Crunchy Panner with Mayo & Caramelised Onions\t\t\t" , font=('perpetua', 18))
        abc.grid(row=2, sticky=W)

        abc = Label(second_frame, text="Swissy Mushi Burger\t\t\t\t\t\t\tRs.120\t\t" , font=('perpetua', 18))
        abc.grid(row=3, sticky=W)
        
        abc = Label(second_frame, text="\t\t\tJuicy Mushroom patty topped with Cheese & Jalepanos\t\t" , font=('perpetua', 18))
        abc.grid(row=4, sticky=W)

        abc = Label(second_frame, text="Veg Exotic Burger\t\t\t\t\t\t\t\tRs.130\t" , font=('perpetua', 18))
        abc.grid(row=5, sticky=W)
           
        abc = Label(second_frame, text="\t\t\tVeg patty in spices with Lettuce, Tomato and Zuccini\t\t\t" , font=('perpetua', 18))
        abc.grid(row=6, sticky=W)

        abc = Label(second_frame, text="Buffmaster Burger\t\t\t\t\t\t\t\tRs.150\t" , font=('perpetua', 18))
        abc.grid(row=7, sticky=W)
           
        abc = Label(second_frame, text="\t\t\tBurger in Mustard, Mayo, Cabbage & Spicy Onions\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=8, sticky=W)

        abc = Label(second_frame, text="Italian Burger\t\t\t\t\t\t\t\tRs.150\t" , font=('perpetua', 18))
        abc.grid(row=9, sticky=W)
           
        abc = Label(second_frame, text="\t\t\tVeg patty with Pesto, Mayo, Cheese, Olives & Tomato\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=10, sticky=W)

        abc = Label(second_frame, text="Beat Down Burger\t\t\t\t\t\t\t\tRs.180\t" , font=('perpetua', 18))
        abc.grid(row=11, sticky=W)
           
        abc = Label(second_frame, text="\t\t\tBeetroot and Carrot patty with Basil, Jalapeno & Mayo\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=12, sticky=W)

        abc = Label(second_frame, text="Kung fu Paneer Burger\t\t\t\t\t\t\tRs.180\t" , font=('perpetua', 18))
        abc.grid(row=13, sticky=W)
           
        abc = Label(second_frame, text="\t\t\tAsian marinated Paneer with Schezwan and Mayo\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=14, sticky=W)

        abc = Label(second_frame, text="Maharaja Jalapeno Burger\t\t\t\t\t\t\tRs.200\t" , font=('perpetua', 18))
        abc.grid(row=15, sticky=W)
           
        abc = Label(second_frame, text="\t\t\tVeg patty topped with Jalepanos, Onions and Lettuce\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=16, sticky=W)

        abc = Label(second_frame, text="Big Crunch Burger\t\t\t\t\t\t\t\tRs.180\t" , font=('perpetua', 18))
        abc.grid(row=17, sticky=W)
           
        abc = Label(second_frame, text="\t\t\tFully loaded veg crunchy patty with spicy sauces\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=18, sticky=W)

        abc = Label(second_frame, text="Mumbai Special Burger\t\t\t\t\t\t\tRs.190\t" , font=('perpetua', 18))
        abc.grid(row=19, sticky=W)
           
        abc = Label(second_frame, text="\t\t\tPotato patty placed between baked buns with Onions\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=20, sticky=W)
        
        abc = Label(second_frame, text="Deadpool Burger\t\t\t\t\t\t\t\tRs.150\t\t" , font=('perpetua', 18))
        abc.grid(row=21, sticky=W)
           
        abc = Label(second_frame, text="\t\t\tFresh Beetroot patty with a hint of sweet Potato & Cumin\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=22, sticky=W)
        
        abc = Label(second_frame, text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=23, sticky=W)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
        abc = Label(second_frame, text="\t\t\t\t\tNON VEG ITEMS\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=24, sticky=W)

        abc = Label(second_frame, text="Chipotle Chicken Burger\t\t\t\t\t\t\tRs.150\t\t" , font=('perpetua', 18))
        abc.grid(row=25, sticky=W)
           
        abc = Label(second_frame, text="\t\tSlow cooked Chipotle Chicken with our inhouse Chipotle Sauce\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=26, sticky=W)

        abc = Label(second_frame, text="Big Fat Man Burger\t\t\t\t\t\t\tRs.170\t" , font=('perpetua', 18))
        abc.grid(row=27, sticky=W)
           
        abc = Label(second_frame, text="\t\tCrispy fried Bacon with Chicken Sausages and Cheese \t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=28, sticky=W)

        abc = Label(second_frame, text="Juicy Chicken Cheese Burger\t\t\t\t\t\tRs.180\t" , font=('perpetua', 18))
        abc.grid(row=29, sticky=W)
           
        abc = Label(second_frame, text="\t\tFired Egg patty served with Cheese, Capsicum and Pepper\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=30, sticky=W)

        abc = Label(second_frame, text="Chicken Masala Burger\t\t\t\t\t\t\tRs.200\t" , font=('perpetua', 18))
        abc.grid(row=31, sticky=W)
           
        abc = Label(second_frame, text="\t\tDesi Chicken topped with delicious veggies on toasted bun\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=32, sticky=W)

        abc = Label(second_frame, text="Aquaman Burger\t\t\t\t\t\t\t\tRs.220\t" , font=('perpetua', 18))
        abc.grid(row=33, sticky=W)
           
        abc = Label(second_frame, text="\t\tLoaded with Prawns tossed in Cocktail Sauce.\t\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=34, sticky=W)

        abc = Label(second_frame, text="Nachos Chicken Burger\t\t\t\t\t\t\tRs.230\t" , font=('perpetua', 18))
        abc.grid(row=35, sticky=W)
           
        abc = Label(second_frame, text="\t\tChicken Patty topped with Nachos Chips and Onions\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=36, sticky=W)
        
        abc = Label(second_frame, text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=37, sticky=W)
 #---------------------------------------------------------------------------------------------------------------------------------------------------------------------  
        abc = Label(second_frame, text="\t\t\t\t\tDRINKS\t\t\t\t\t" , font=('perpetua', 18))
        abc.grid(row=38, sticky=W)

        abc = Label(second_frame, text="Chocolate Drink\t\t\t\t\t\t\t\tRs.50\t" , font=('perpetua', 18))
        abc.grid(row=39, sticky=W)

        abc = Label(second_frame, text="Lemonade\t\t\t\t\t\t\t\tRs.30\t" , font=('perpetua', 18))
        abc.grid(row=40, sticky=W)

        abc = Label(second_frame, text="Can of Coke\t\t\t\t\t\t\t\tRs.60\t" , font=('perpetua', 18))
        abc.grid(row=41, sticky=W)
           
        abc = Label(second_frame, text="Can of Sprite\t\t\t\t\t\t\t\tRs.60\t\t" , font=('perpetua', 18))
        abc.grid(row=42, sticky=W)
           
        abc = Label(second_frame, text="Can of Mountain Dew\t\t\t\t\t\t\tRs.60\t" , font=('perpetua', 18))
        abc.grid(row=43, sticky=W)
             
        abc = Label(second_frame, text="Can of Thumbs UP\t\t\t\t\t\t\t\tRs.60\t" , font=('perptua', 18))
        abc.grid(row=44, sticky=W)     
       
        abc = Label(second_frame, text="Can of Red Bull\t\t\t\t\t\t\t\tRs.60\t" , font=('perpetua', 18))
        abc.grid(row=45, sticky=W)

        s5.resizable(False, False)
        s5.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


def feedbackadmin(useridd):
        s5 = Tk()
        s5.geometry("1080x720")
        s5.title("Burger Therapy - Admin - View Feedback")

        topframe = Frame(s5, bg="#d5b493")
        topframe.pack(side=TOP,fill=BOTH)
        lbl = Label(topframe,bg='#d5b493',fg='#d5b493')
        lbl.grid(row=0, column=0)
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="aaaaaaasaaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=0)
        lblInfo = Label(topframe, font=('cooper black', 45, 'bold'), text="Feedback", bd=10, relief="raise")
        lblInfo.grid(row=1, column=1)
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="aaaaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=2)
        b2=Button(topframe, font=('cooper black', 25, 'bold'), text="Back",command=lambda:[s5.destroy(),adminloggedin(useridd)], bd=6 )
        b2.grid(row=1, column=3)
        lblInfo1 = Label(topframe,bg='#d5b493',fg='#d5b493')
        lblInfo1.grid(row=2, column=1)


        main_frame = Frame(s5, bg="#d5b493")
        main_frame.pack(fill=BOTH , expand=1)

        my_canvas = Canvas(main_frame ,bg="#d5b493")
        my_canvas.pack(side =LEFT , fill=BOTH , expand=1)

        my_scrollbar1 = ttk.Scrollbar(s5 , orient = HORIZONTAL , command = my_canvas.xview)
        my_scrollbar1.pack(side =BOTTOM , fill=X )

        my_scrollbar = ttk.Scrollbar(main_frame , orient = VERTICAL , command = my_canvas.yview)
        my_scrollbar.pack(side =RIGHT , fill=Y)

        my_canvas.configure(xscrollcommand=my_scrollbar1.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = Frame(my_canvas , bg="#d5b493")
        my_canvas.create_window((0,0), window=second_frame , anchor = "nw")
        

        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493' ) 
        l1.grid(row=0, column=0)
        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold') ,bg='#d5b493',fg='#d5b493') 
        l1.grid(row=0, column=10)


        #feedback
        cursor.execute("SELECT MAX(LENGTH(feedback)) FROM feedback") 
        details=cursor.fetchall()
        feedback=list(details[0])
        feedback=int(feedback[0])
        if(feedback<10):
            feedback=10


        #Table Heading
        l1= Label(second_frame,text="Sr No.",width=5,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=1)
        l1= Label(second_frame,text="Mobile No.",width=10,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=2)
        l1= Label(second_frame,text="Feedback",width=feedback,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
        l1.grid(row=1, column=3)
        


        cursor.execute("SELECT * FROM feedback") 
        details=list(cursor.fetchall())
        abc=[]
        i=2
        for k in range(len(details)):
            abc=list(details[k])
            l1= Label(second_frame,text=k+1,width=5,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="w") 
            l1.grid(row=k+2, column=1)
            e = Label(second_frame,width=10,font=('cooper black', 15, 'bold'), text=abc[0],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=2)
            e = Label(second_frame,width=feedback,font=('cooper black', 15, 'bold'), text=abc[1],borderwidth=2,relief='ridge', anchor="w") 
            e.grid(row=i, column=3)

        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493') 
        l1.grid(row=i, column=0)
        l1= Label(second_frame,text="ll",font=('cooper black', 15, 'bold'),bg='#d5b493',fg='#d5b493') 
        l1.grid(row=i, column=10)

        s5.resizable(False, False)
        s5.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

def adminloggedin(useridd):
        s3=Tk()
        s3.geometry("1080x720")
        s3.title("Burger Therapy - Admin")

        c = Canvas(s3, width=1080, height=720, bg="red")
        filename = PhotoImage(file = "background.png")

        label1 = Label(s3, image = filename)
        label1.place(x = 0, y = 0 , relwidth=1, relheight=1)

        b1image = PhotoImage(file = "logout.png")
        b1 =Button(s3,image = b1image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s3.destroy(),startscreen()], bd=4 )
        b1.place(x=925, y=10)

        b5image = PhotoImage(file = "addadmin.png")
        b5=Button(s3,image = b5image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s3.destroy(),addadmin(useridd)], bd=4 )
        b5.place(x=10, y=10 )

        b2image = PhotoImage(file = "customerdetail.png")
        b2=Button(s3,image = b2image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s3.destroy(),customerdetails(useridd)], bd=4 )
        b2.place(x=310, y=450)

        b3image = PhotoImage(file = "updatecustomer.png")
        b3=Button(s3,image = b3image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s3.destroy(),editcustomer(useridd)], bd=4 )
        b3.place(x=300, y=525 )
        
        b4image = PhotoImage(file = "sales.png")
        b4=Button(s3,image = b4image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s3.destroy(),viewsales(useridd)], bd=4 )
        b4.place(x=620, y=450 )

        b6image = PhotoImage(file = "viewfeedback.png")
        b6=Button(s3,image = b6image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s3.destroy(),feedbackadmin(useridd)], bd=4 )
        b6.place(x=600, y=525 )
        
        s3.resizable(False, False)
        s3.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

def admin():
        def reset():
                passwd.set("")
                userid.set("")
        def submit():
                if(e1.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Admin ID")
                        
                elif(e2.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Password")
                        
                else:
                        useridd = e1.get()
                        password1 = e2.get()
                        try:
                                cursor.execute("select passwd from admin where userid = ?" , (useridd,))                   
                                details=cursor.fetchone()
                                if(details[0]==password1):
                                        s2.destroy()
                                        adminloggedin(useridd)
                                        
                                else:
                                        passwd.set("")
                                        usermobno.set("")
                                        messagebox.showinfo("Burger Therapy", "Invalid credentials")
                        except:
                                messagebox.showinfo("Burger Therapy", "InValid credentials")
                                
        s2=Tk()
        s2.geometry("1080x720")
        s2.title("Burger Therapy - Admin Login")

        userid=StringVar()
        passwd=StringVar()


        c = Canvas(s2, width=1080, height=720, bg="red")
        filename = PhotoImage(file = "background.png")

        label1 = Label(s2, image = filename)
        label1.place(x = 0, y = 0 , relwidth=1, relheight=1)

        frame=LabelFrame(s2,text="Welcome to Burger Therapy",font=("cooper black",28) , padx=50 , pady=50 ,bg="#d1b493" )
        frame.grid( padx=125 , pady=150)

        lab1=Label(frame,text="Admin Login",fg="#ffffff",bg="#78543c",width=20,font=("cooper black",30))
        lab1.grid(row=0 , column=2)

        lab2=Label(frame,bg="#d1b493",font=("cooper black",18))
        lab2.grid(row=1 , column=0)

        lab3=Label(frame,text="User ID",bg="#78543c",fg="#ffffff",font=("cooper black",18))
        lab3.grid(row=2 , column=1)
        e1=Entry(frame,bg="white",textvariable=userid,width=15,font=("cooper black",18))
        e1.grid(row=2 , column=2)

        lab4=Label(frame,bg="#d1b493",font=("cooper black",18))
        lab4.grid(row=3 , column=0)

        lab5=Label(frame,text="Password",bg="#78543c",fg="#ffffff",font=("cooper black",18))
        lab5.grid(row=4 , column=1)
        e2=Entry(frame,textvariable=passwd, show='*', bg="white",width=15,font=("cooper black",18))
        e2.grid(row=4 , column=2)

        def on_press(event):
                e2.config(show='')

        def on_release( event):
                e2.config(show='*')
                
        b4image = PhotoImage(file = "visible.png")
        b4=Button(frame,image = b4image ,fg="#d5b493" ,anchor="w", bg="#d5b493" ,activebackground="#d5b493" , bd=4 )
        b4.grid(row=4 , column=2 , sticky="e")
        b4.bind("<ButtonPress>", on_press)
        b4.bind("<ButtonRelease>", on_release)

        lab6=Label(frame,bg="#d1b493",font=("cooper black",18))
        lab6.grid(row=5 , column=0)
            
        b1=Button(frame,text=" Back ",command=lambda:[s2.destroy(),startscreen()],bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b1.grid(row=10 , column=1)
        b2=Button(frame,text=" Reset ",command=reset,bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b2.grid(row=10, column=2)
        b3=Button(frame,text=" Submit ",command=submit,bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b3.grid(row=10, column=3)
        s2.resizable(False, False)
        s2.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def displaydetails(finalnumber):
    finalnumber=finalnumber
    def update(finalnumber,points):
        if(fname.get()==""):
            messagebox.showinfo("Burger Therapy", "Enter a Valid Name")
        elif(lname.get()==""):
            messagebox.showinfo("Burger Therapy", "Enter a Valid Name")
        elif(passwd.get()==""):
            messagebox.showinfo("Burger Therapy", "Enter a Valid Password")
        elif(email.get()==""):
            messagebox.showinfo("Burger Therapy", "Enter a Valid Email Address")
        elif(address.get()==""):
            messagebox.showinfo("Burger Therapy", "Enter a Valid Address")
        elif(city.get()==""):
            messagebox.showinfo("Burger Therapy", "Enter a Valid City")
        elif(passwd.get().lower()==fname.get().lower() or passwd.get().lower()==lname.get().lower() or passwd.get()== str(finalnumber)):
            passwd.set("")
            messagebox.showinfo("Burger Therapy", "Enter a Strong Password")
        else:
            try:
                cursor.execute("delete from customers where mobno = ?" , (finalnumber,))
                conn.commit()
                sql = "INSERT INTO customers (fname , lname , passwd , email , address , city , mobno , points) VALUES (?,?,?,?,?,?,?,?)"
                val = (fname.get() , lname.get() , passwd.get() , email.get() ,  address.get() , city.get() , finalnumber , points)
                conn.execute(sql, val)
                conn.commit()
                messagebox.showinfo("Burger Therapy", "Update Successful")   
            except:
                messagebox.showinfo("Burger Therapy", "Server Timed Out")

    cursor.execute("select * from customers where mobno = ?" , (finalnumber,))
    details=cursor.fetchone()
    if details is None:
        messagebox.showinfo("Burger Therapy", "Server Timed Out")
    else:
        fwidth=0
        for i in range(8):
            temp=len(details[i])
            if(temp>fwidth):
                fwidth=temp
        fwidth=fwidth+1
        #print(fwidth)
        s4=Tk()
        s4.geometry("1080x720")
        s4.title("Burger Therapy - Customer Details")

        fname=StringVar()
        lname=StringVar()
        passwd=StringVar()
        email=StringVar()
        address=StringVar()
        city=StringVar()
        
        c = Canvas(s4, width=1080, height=720, bg="red")
        filename = PhotoImage(file = "background.png")
        
        label1 = Label(s4, image = filename)
        label1.place(x = 0, y = 0 , relwidth=1, relheight=1)
        frame=LabelFrame(s4,text=" Welcome to Burger Therapy",font=("cooper black",28) , padx=50 , pady=50 ,bg="#d1b493")
        frame.grid( padx=350 , pady=200)
        
        lab1=Label(frame,text="First Name: ",width=13,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="c")
        lab1.grid(row=0 , column=1)
        e1=Entry(frame,textvariable=fname,bg="white",width=fwidth,font=("cooper black",16),borderwidth=2,relief=GROOVE)
        e1.grid(row=0 , column=3)
        e1.insert(END, details[0])

        lab3=Label(frame,text="Last Name: ",width=13,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="c")
        lab3.grid(row=1 , column=1)
        e2=Entry(frame,textvariable=lname,bg="white",width=fwidth,font=("cooper black",16),borderwidth=2,relief=GROOVE)
        e2.grid(row=1 , column=3)
        e2.insert(END, details[1])
        
        lab5=Label(frame,text="Password: ",width=13,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="c")
        lab5.grid(row=2 , column=1)
        e3=Entry(frame,textvariable=passwd,show='*',bg="white",width=fwidth,font=("cooper black",16),borderwidth=2,relief=GROOVE)
        e3.grid(row=2 , column=3)
        e3.insert(END, details[2])

        lab6=Label(frame,width=1,font=('cooper black', 15, 'bold'),bg="#d1b493")
        lab6.grid(row=2 , column=4)
        def on_press(event):
                e3.config(show='')

        def on_release( event):
                e3.config(show='*')
                
        b1image = PhotoImage(file = "visible.png")
        b1=Button(frame,image = b1image ,fg="#d5b493" ,anchor="w", bg="#d5b493" ,activebackground="#d5b493" , bd=4 )
        b1.grid(row=2 , column=5,sticky="e")
        b1.bind("<ButtonPress>", on_press)
        b1.bind("<ButtonRelease>", on_release)
        
        lab7=Label(frame,text="Email ID: ",width=13,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="c")
        lab7.grid(row=3 , column=1)
        e4=Entry(frame,textvariable=email,bg="white",width=fwidth,font=("cooper black",16),borderwidth=2,relief=GROOVE)
        e4.grid(row=3 , column=3)
        e4.insert(END, details[3])

        lab9=Label(frame,text="Address: " ,width=13,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="c")
        lab9.grid(row=4 , column=1)
        e5=Entry(frame,textvariable=address,bg="white",width=fwidth,font=("cooper black",16),borderwidth=2,relief=GROOVE)
        e5.grid(row=4 , column=3)
        e5.insert(END, details[4])

        lab11=Label(frame,text="City: ",width=13,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="c")
        lab11.grid(row=5 , column=1)
        e6=Entry(frame,textvariable=city,bg="white",width=fwidth,font=("cooper black",16),borderwidth=2,relief=GROOVE)
        e6.grid(row=5 , column=3)
        e6.insert(END, details[5])
        
        lab13=Label(frame,text="Mobile Number: " ,width=13,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="c")
        lab13.grid(row=6 , column=1)
        lab14=Label(frame,text=details[6] , width=fwidth,anchor="w",font=("cooper black",16),borderwidth=2,relief=GROOVE  )
        lab14.grid(row=6 , column=3)

        lab15=Label(frame,text="Points: ",width=13,font=('cooper black', 15, 'bold') ,borderwidth=2,relief='ridge', anchor="c")
        lab15.grid(row=7 , column=1)
        lab16=Label(frame,text=details[7] , width=fwidth,anchor="w",font=("cooper black",16),borderwidth=2,relief=GROOVE  )
        lab16.grid(row=7, column=3)
        
        lab17=Label(frame , bg="#d1b493")
        lab17.grid(row=8 , column=1)

        temppoints=details[7]
        
        b2=Button(frame,text=" Update ",command=lambda:[update(finalnumber,temppoints)],bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b2.grid(row=9 , column=1)
        lab18=Label(frame , bg="#d1b493")
        lab18.grid(row=9 , column=2)
        b3=Button(frame,text=" Back ",command=lambda:[s4.destroy(),login(finalnumber)],bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b3.grid(row=9 , column=3,sticky="e")
        
        s4.resizable(False, False)
        s4.mainloop()        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def faq(finalnumber):
    
    s4 = Tk()
    s4.geometry("1080x720")
    s4.title("Burger Therapy - FAQ")

    topframe = Frame(s4, bg="#d5b493")
    topframe.pack(side=TOP,fill=BOTH)
    lbl = Label(topframe,bg='#d5b493',fg='#d5b493')
    lbl.grid(row=0, column=0)
    lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="\taaaaaaaaaa",bg='#d5b493',fg='#d5b493')
    lbl.grid(row=1, column=0)
    lblInfo = Label(topframe, font=('cooper black', 45, 'bold'), text=" FAQ ", bd=10, relief="raise")
    lblInfo.grid(row=1, column=1 , sticky='e')
    lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="\taaaaaaa",bg='#d5b493',fg='#d5b493')
    lbl.grid(row=1, column=3)
    b1=Button(topframe, font=('cooper black', 20, 'bold'), text="Back",command=lambda:[s4.destroy(),login(finalnumber)], bd=6 )
    b1.grid(row=1, column=3, sticky='e')
    lblInfo1 = Label(topframe,bg='#d5b493',fg='#d5b493')
    lblInfo1.grid(row=2, column=1)

    main_frame = Frame(s4, bg="#d5b493" , bd=10)
    main_frame.pack(fill=BOTH , expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side =LEFT , fill=BOTH , expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame , orient = VERTICAL , command = my_canvas.yview)
    my_scrollbar.pack(side =RIGHT , fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas , bg="#d5b493" , bd=10)
    my_canvas.create_window((0,0), window=second_frame , anchor = "nw" )
    

    abc = Label(second_frame, text="Q1 What are Reward Points ?\t\t\t\t\t\t\t" , font=('cooper black', 18, 'bold'))
    abc.grid(row=0, sticky=W)
    abc = Label(second_frame, text="A1 Reward Points are given to Registered Customers \t\t\t\t" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=1, sticky=W)
    abc = Label(second_frame, text="Q2 How many points can i use at once ?\t\t\t\t\t\t\t" , font=('cooper black', 18, 'bold'))
    abc.grid(row=2, sticky=W)
    abc = Label(second_frame, text="A2 You can use 80% of your Total Bill amount as Reward Points\t\t\t" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=3, sticky=W)
    abc = Label(second_frame, text="Q3 How are my points converted ?\t\t\t\t\t\t\t" , font=('cooper black', 18, 'bold'))
    abc.grid(row=4, sticky=W)
    abc = Label(second_frame, text="A3 10 Reward Points is equal to Rs.1\t\t\t\t\t\t\t\t" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=5, sticky=W)
    abc = Label(second_frame, text="Q4 Where can i use my reward points ?\t\t\t\t\t\t" , font=('cooper black', 18, 'bold'))
    abc.grid(row=6, sticky=W)
    abc = Label(second_frame, text="A4 Reward Points can be Used on instore purchases ONLY\t\t\t\t\t\t" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=7, sticky=W)
    abc = Label(second_frame, text="Q5 How do i earn reward points ?\t\t\t\t\t\t\t\t" , font=('cooper black', 18, 'bold'))
    abc.grid(row=8, sticky=W)
    abc = Label(second_frame, text="A5 Reward Points: 7% points are given on the basis of your Final Bill Amount\t\t\t" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=9, sticky=W)
    abc = Label(second_frame, text="Q6 How can i convey my cooking instructions ?\t\t\t\t\t\t" , font=('cooper black', 18, 'bold'))
    abc.grid(row=10, sticky=W)
    abc = Label(second_frame, text="A6 Before Completing the Payment there would be an option on the screen\t\t" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=11, sticky=W)
    abc = Label(second_frame, text="Q7 Would my payment information be safe ?\t\t\t\t\t\t\t" , font=('cooper black', 18, 'bold'))
    abc.grid(row=12, sticky=W)
    abc = Label(second_frame, text="A7 We ONLY store your Card Number\t\t\t\t\t\t\t\t" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=13, sticky=W)
    abc = Label(second_frame, text="Q8 Can points be exchanged for cash ?\t\t\t\t\t\t" , font=('cooper black', 18, 'bold'))
    abc.grid(row=14, sticky=W)
    abc = Label(second_frame, text="A8 Points cannot be exchanged for cash\t\t\t\t\t" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=15, sticky=W)
    abc = Label(second_frame, text="Q9 Will points be rewarded for purchases made by points ?\t\t\t\t\t\t" , font=('cooper black', 18, 'bold'))
    abc.grid(row=16, sticky=W)
    abc = Label(second_frame, text="A9 Points will not be rewarded for such purchases\t\t\t\t\t" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=17, sticky=W)
    abc = Label(second_frame, text="----------------------------------------------------------------------" , font=('Segoe Print', 18 , 'italic'))
    abc.grid(row=18, sticky=W)
    

    s4.resizable(False, False)
    s4.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def feedback(finalnumber):
        def submitfeedback():
            e1=e2.get(1.0, "end-1c")
            if(e1!=""):
                sql = "INSERT INTO feedback (mobno , feedback) VALUES (?,?)"
                val = (finalnumber , str(e1))
                conn.execute(sql, val)
                conn.commit()
                print("Feedback Submitted")
                finel="Thank you for your valuable feedback"       
                messagebox.showinfo("Burger Therapy", finel)
                s4.destroy()
                login(finalnumber)
            else:
                finel="Kindly enter yor feedback"       
                messagebox.showinfo("Burger Therapy", finel)
                print("NO Feedback Submitted")
                
        s4 = Tk()
        s4.geometry("1080x720")
        s4.title("Burger Therapy - Feedback")
        
        topframe = Frame(s4, bg="#d5b493")
        topframe.pack(side=TOP,fill=BOTH)
        lbl = Label(topframe,bg='#d5b493',fg='#d5b493')
        lbl.grid(row=0, column=0)
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="\taaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=0)
        lblInfo = Label(topframe, font=('cooper black', 45, 'bold'), text=" Feedback ", bd=10, relief="raise")
        lblInfo.grid(row=1, column=1 , sticky='e')
        lbl = Label(topframe, font=('cooper black', 35, 'bold'), text="aaaaaaaa",bg='#d5b493',fg='#d5b493')
        lbl.grid(row=1, column=3)
        b1=Button(topframe, font=('cooper black', 20, 'bold'), text="Back",command=lambda:[s4.destroy(),login(finalnumber)], bd=6 )
        b1.grid(row=1, column=3, sticky='e')
        lblInfo1 = Label(topframe,bg='#d5b493',fg='#d5b493')
        lblInfo1.grid(row=2, column=1)

        main_frame = Frame(s4, bg="#d5b493" , bd=10)
        main_frame.pack(fill=BOTH , expand=1)
        
        abc = Label(main_frame, text="\t\t Kindly enter your feedback for us                                   " ,font=('Segoe Print', 18 , 'italic'))
        abc.grid(row=1, sticky=W)
        abc = Label(main_frame,fg="#d5b493" , bg="#d5b493" )
        abc.grid(row=2, sticky=W)
        e2 = Text(main_frame,height = 10,width = 50)
        e2.grid(row=3)
        abc = Label(main_frame,fg="#d5b493" , bg="#d5b493" )
        abc.grid(row=4, sticky=W)
        b1=Button(main_frame, font=('cooper black', 20, 'bold'), text="Submit",command=lambda:[submitfeedback()], bd=6 )
        b1.grid(row=5)
        
        s4.resizable(False, False)
        s4.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def login(finalnumber):

        finalnumber=finalnumber

        s4 = Tk()

        s4.geometry("1080x720")
        s4.title("Welcome to Burger Therapy") 

        c = Canvas(s4, width=1080, height=720, bg="red")
        bg = PhotoImage(file = "background.png")

        label1 = Label(s4, image = bg)
        label1.place(x = 0, y = 0 , relwidth=1, relheight=1)

        b3image = PhotoImage(file = "logout.png")
        b3 =Button(s4,image = b3image , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s4.destroy(),startscreen()], bd=4 )
        b3.place(x=925, y=10)
        
        b4image = PhotoImage(file = "faq.png")
        b4=Button(s4,image = b4image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s4.destroy(),faq(finalnumber)], bd=4 )
        b4.place(x=375, y=460 )
        
        b1image = PhotoImage(file = "details.png")
        b1=Button(s4,image = b1image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s4.destroy(),displaydetails(finalnumber)], bd=4 )
        b1.place(x=375, y=530 )

        b2image = PhotoImage(file = "menu.png")
        b2=Button(s4,image = b2image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s4.destroy(),main_menu(finalnumber)], bd=4 )
        b2.place(x=575, y=460)
        
        b5image = PhotoImage(file = "feedback.png")
        b5=Button(s4,image = b5image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s4.destroy(),feedback(finalnumber)], bd=4 )
        b5.place(x=555, y=530)

        s4.resizable(False, False)
        s4.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def loginscreen():
        def reset():
                passwd.set("")
                usermobno.set("")
        def submit():
                if(e1.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Mobile Number")
                        
                elif(e2.get()==""):
                        messagebox.showinfo("Burger Therapy", "Enter a Valid Password")
                else:
                        mobno1 = e1.get()
                        password1 = e2.get()
                        try:
                            cursor.execute("select passwd from customers where mobno = ?" , (mobno1,))                   
                            details=cursor.fetchone()
                            if(details[0]==password1):
                                s2.destroy()
                                login(mobno1)
                            else:
                                messagebox.showinfo("Burger Therapy", "Invalid credentials")
                        except:
                                messagebox.showinfo("Burger Therapy", "InValid credentials")
                                
        s2=Tk()
        s2.geometry("1080x720")
        s2.title("Burger Therapy - SignUp")

        usermobno=StringVar()
        passwd=StringVar()
        
        c = Canvas(s2, width=1080, height=720, bg="red")
        filename = PhotoImage(file = "background.png")

        label1 = Label(s2, image = filename)
        label1.place(x = 0, y = 0 , relwidth=1, relheight=1)
        
        frame=LabelFrame(s2,text="Welcome to Burger Therapy",font=("cooper black",28) , padx=50 , pady=50 ,bg="#d1b493" )
        frame.grid( padx=125 , pady=150)
        
        lab1=Label(frame,text="Login",fg="#ffffff",bg="#78543c",width=20,font=("cooper black",30))
        lab1.grid(row=0 , column=2)

        lab2=Label(frame,bg="#d1b493",font=("cooper black",18))
        lab2.grid(row=1 , column=0)
        
        lab3=Label(frame,text="Mobile Number",bg="#78543c",fg="#ffffff",font=("cooper black",18))
        lab3.grid(row=2 , column=1)
        e1=Entry(frame,bg="white",textvariable=usermobno,width=15,font=("cooper black",18))
        e1.grid(row=2 , column=2)

        lab4=Label(frame,bg="#d1b493",font=("cooper black",18))
        lab4.grid(row=3 , column=0)

        lab5=Label(frame,text="Password",bg="#78543c",fg="#ffffff",font=("cooper black",18))
        lab5.grid(row=4 , column=1)
        e2=Entry(frame,textvariable=passwd, show='*', bg="white",width=15,font=("cooper black",18))
        e2.grid(row=4 , column=2)
        
        def on_press(event):
                e2.config(show='')

        def on_release( event):
                e2.config(show='*')
                
        b4image = PhotoImage(file = "visible.png")
        b4=Button(frame,image = b4image ,fg="#d5b493" ,anchor="w", bg="#d5b493" ,activebackground="#d5b493" , bd=4 )
        b4.grid(row=4 , column=2 , sticky="e")
        b4.bind("<ButtonPress>", on_press)
        b4.bind("<ButtonRelease>", on_release)
        
        lab6=Label(frame,bg="#d1b493",font=("cooper black",18))
        lab6.grid(row=5 , column=0)
            
        b1=Button(frame,text=" Back ",command=lambda:[s2.destroy(),startscreen()],bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b1.grid(row=10 , column=1)
        b2=Button(frame,text=" Reset ",command=reset,bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b2.grid(row=10, column=2)
        b3=Button(frame,text=" Submit ",command=submit,bg="#78543c",bd=4,fg="white",font=("cooper black",16))
        b3.grid(row=10, column=3)
        s2.resizable(False, False)
        s2.mainloop()           
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def startscreen():
    s1 = Tk()
      
    s1.geometry("1080x720")
    s1.title("Burger Therapy") 

    c = Canvas(s1, width=1080, height=720, bg="red")
    filename = PhotoImage(file = "background.png")

    label1 = Label(s1, image = filename)
    label1.place(x = 0, y = 0 , relwidth=1, relheight=1)

    b3image = PhotoImage(file = "admin.png")
    b3 =Button(s1,image = b3image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s1.destroy(),admin()], bd=4 )
    b3.place(x=925, y=10)

    b1image = PhotoImage(file = "login.png")
    b1=Button(s1,image = b1image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s1.destroy(),loginscreen()], bd=4 )
    b1.place(x=575, y=490)

    b2image = PhotoImage(file = "signup.png")
    b2=Button(s1,image = b2image ,fg="#d5b493" , bg="#d5b493" ,activebackground="#d5b493" ,command=lambda:[s1.destroy(),signup()], bd=4 )
    b2.place(x=375, y=490 )

    s1.resizable(False, False)
    s1.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

startscreen()