import tkinter
from tkinter import messagebox
from tkinter import*
import sqlite3
from tkinter import ttk
root=tkinter.Tk()
import datetime
import random
import re



table=tkinter.Frame(root,bg="white",padx=20,pady=20)
table.grid(row=0,column=1)
root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(1,weight=1)

tablen=tkinter.Frame(root,bg="white",padx=20,pady=20)
tablen.grid(row=0,column=0)
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)




def submition():
#new user data getting    
    conn=sqlite3.connect('user.db')
    cursor=conn.cursor()
    #cursor.execute("create table userinformation IF not exists(name int,phonenumber int,mailid text, housenumber int, address text,password text)")
    cursor.execute("insert into userinformation values(:name,:phonenumber,:mailid,:housenumber,:address,:password)",
    {
        'name':name_entry.get(),
        'phonenumber':phonenumber_entry.get(),
        'mailid':mailid_entry.get(),
        'housenumber':housenumber_entry.get(),
        'address':address_entry.get(),
        'password':password_entry.get()
        }
        )
    
    
    name_entry.delete(0,END)
    phonenumber_entry.delete(0,END)
    mailid_entry.delete(0,END)
    housenumber_entry.delete(0,END)
    address_entry.delete(0,END)
    password_entry.delete(0,END)
    conn.commit()
    conn.close()
    messagebox.showinfo("message","Your account has created sucessfully! \n login and order \n thank you!")
    
#existing user login   
    
def check():
    conn=sqlite3.connect('user.db')
    cursor=conn.cursor()
    
    cursor.execute('select phonenumber,password from userinformation where phonenumber=? AND password=?',(phonenumberlogin_entry.get(),passwordlogin_entry.get()))
    data=cursor.fetchone()
    phonenumberget=phonenumberlogin_entry.get()
    passwordget=passwordlogin_entry.get()
    if data:
         root1=tkinter.Tk()
         incremented_date=datetime.datetime.now() + (datetime.timedelta(days=1))
         bookingdate=incremented_date.strftime("%d-%m-%y")

         def view():
             rootad=tkinter.Tk()
             rootad.title("admin page")
             rootad.geometry("800x1000")
             def upcomming():
                 conn=sqlite3.connect("user.db")
                 cursor=conn.cursor()
                 #query=("select * from PAYMENT where phonenumber=={}".format(date))
                 cursor.execute("select * from PAYMENT ")
                 rows=cursor.fetchall()
                 tableview=tkinter.ttk.Treeview(rootad)
                 tableview["columns"]=["phonenumber","date","T_method","T_number","amount","housenumber","address","milk","water"]
                 for row in rows:
                      tableview.insert("","end",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
                 tableview.grid(row=3,column=0,sticky="nsew")

             tablead=tkinter.Frame(rootad,bg="white",padx=20,pady=20)
             tablead.grid(row=0,column=0)
             rootad.grid_rowconfigure(0,weight=1)
             rootad.grid_columnconfigure(0,weight=1)
             
             filter1=tkinter.Label(tablead,text="UPCOMMING DELIVERY :")
             filter1.grid(row=0,column=0)

             #date_entry=Entry(root)
             #date_entry.grid(row=1,column=0)
             #date=str(date_entry.get())

             filter1=tkinter.Button(tablead,text="click",command=upcomming)
             filter1.grid(row=0,column=2)
             incremented_date=datetime.datetime.now() + (datetime.timedelta(days=1))
             bookingdate=incremented_date.strftime("%d-%m-%y")


         def submitorder():
               incremented_date=datetime.datetime.now() + (datetime.timedelta(days=1))
               bookingdate=incremented_date.strftime("%d-%m-%y")
               #session["mobilnumber"]= phonenumberid
               global totalcost

               milknos=int(milk_entry.get())
               milkcost=milknos*23
               watercannos=int(watercan_entry.get())
               watercancost=watercannos*30
               totalcost=milkcost+watercancost
               
               conn=sqlite3.connect("user.db")
               cursor=conn.cursor()
               #cursor.execute("create table orderdetails IF not exists(orderdate str,phonenumber int,milk int,watercan int, cost int)")
               cursor.execute("insert into orderdetails values (:orderdate,:phonenumber,:milk,:watercan,:cost)",
               {
                         "orderdate":bookingdate,
                         "phonenumber":phonenumberid,
                         "milk":milk_entry.get(),
                         "watercan":watercan_entry.get(),
                         "cost":totalcost
               })
               conn.commit()
               conn.close()
               
               #def payment():
                #   methods=["UPI","DEBIT CARD","CREDIT CARD"]
                 #  m=tkinter.StringVar()

               def upipay():
                          root2=tkinter.Tk()
                          root2.title("payment page")
                          root2.geometry("700x900")
                          #selected_method=selection
                          
                          


                          def paidupi():
                              #ids=str(idi)
                              #if len(ids)==10 :
                                  conn=sqlite3.connect('user.db')
                                  cursor=conn.cursor()
                                  #cursor.execute("create table PAYMENT (phonenumber int,date str,T_method str,T_number int,amount int)")
                                  #cursor.execute("alter table PAYMENT add column milk int")
                                  #cursor.execute("alter table PAYMENT add column water int")
                                  cursor.execute("insert into  PAYMENT values(:phonenumber,:date,:T_method,:T_number,:amount,:housenumber,:address,:milk,:water)",
                                                 {
                                                     "phonenumber":pn,
                                                     "date":bookingdate,
                                                     "T_method":"UPI",
                                                     "T_number":transaction_id,
                                                     "amount":cost,
                                                     "housenumber":housenumber,
                                                     "address":address,
                                                     "milk":milk,
                                                     "water":water
                                                     })
                                  messagebox.showinfo('message','ORDER SUCcESSFULL \n you will receive the items by {} at 5AM - 6AM \n THANK YOU'.format(bookingdate))
                                  conn.commit()
                                  conn.close()
                             # else:
                                 # messagebox.showinfo('message','INVALID UPI ID')
                                                 
                          cost=totalcost
                          pn=p_number
                          milk=milk_no
                          water=watercan_no
                          
                          transaction_id=random.randint(1000000000000,999999999999999)
                                                 
                          incremented_date=datetime.datetime.now() + (datetime.timedelta(days=1))
                          bookingdate=incremented_date.strftime("%d-%m-%y")
                          
                          conn=sqlite3.connect("user.db")
                          cursor=conn.cursor()
                          cursor.execute("select housenumber from userinformation where phonenumber=={}".format(pn))
                          housenumber=cursor.fetchall()[0][0]

                          cursor.execute("select address from userinformation where phonenumber=={}".format(pn))
                          address=cursor.fetchall()[0][0]

                          #cursor.execute("select milk from orderdetails where phonenumber=={} AND orderdate=={} AND cost=={}".format(pn,bookingdate,cost))
                          #milk=cursor.fetchall()[0]

                          #cursor.execute("select water from orderdetails where phonenumber=={} AND orderdate=={} AND cost=={}".format(pn,bookingdate,cost))
                          #water=cursor.fetchall()[0]
                          
                          
                          conn.commit()
                          conn.close()
                          def paid():
                              if re.match(condition_upiid,upiid_entry.get()):
                                  paidupi()
                              else:
                                  messagebox.showinfo('message','INVALID UPI ID')
                          tableb=tkinter.Frame(root2,bg="white",padx=20,pady=20)
                          tableb.grid(row=0,column=0)
                          root2.grid_rowconfigure(0,weight=1)
                          root2.grid_columnconfigure(0,weight=1)
                          
                          upiid=tkinter.Label(tableb,text="UPI ID")
                          upiid.grid(row=1,column=0)
                          upiid_entry=tkinter.Entry(tableb)
                          upiid_entry.grid(row=1,column=1)
                          condition_upiid="^([a-zA-Z0-9.\-_]{2,256})@([a-zA-Z]{2,64})"

                          #idi=upiid_entry.get()
                          #ids=str(idi)

                          pay=tkinter.Button(tableb,text="pay",bg="blue", activebackground="green",command=paid)
                          pay.grid(row=2,column=1)
                          
                           
               def debitpay():
                           root2=tkinter.Tk()
                           root2.title("payment page")
                           root2.geometry("700x900")


                           def paiddebitcard():
                              
                              #if ids:
                                  conn=sqlite3.connect('user.db')
                                  cursor=conn.cursor()
                                  #cursor.execute("create table PAYMENT (phonenumber int,date str,T_method str,T_number int,amount int)")
                                  #cursor.execute("alter table PAYMENT add column housenumber int")
                                  #cursor.execute("alter table PAYMENT add column address text")
                                  cursor.execute("insert into PAYMENT values(:phonenumber,:date,:T_method,:T_number,:amount,:housenumber,:address,:milk,:water)",
                                                 {
                                                     "phonenumber":pn,
                                                     "date":bookingdate,
                                                     "T_method":"DEBIT CARD",
                                                     "T_number":transaction_id,
                                                     "amount":cost,
                                                     "housenumber":housenumber,
                                                     "address":address,
                                                     "milk":milk,
                                                     "water":water
                                                     })
                                  messagebox.showinfo('message','ORDER SUCcESSFULL \n you will receive the items by {} at 5AM - 6AM \n THANK YOU'.format(bookingdate))
                                  conn.commit()
                                  conn.close()
                              #else:
                                   #messagebox.showinfo('message','INVALID CARD NUMBER')
                                                 
                           cost=totalcost
                           pn=p_number
                           milk=milk_no
                           water=watercan_no
                           
                           conn=sqlite3.connect("user.db")
                           cursor=conn.cursor()
                           cursor.execute("select housenumber from userinformation where phonenumber=={}".format(pn))
                           housenumber=cursor.fetchall()[0][0]

                           cursor.execute("select address from userinformation where phonenumber=={}".format(pn))
                           address=cursor.fetchall()[0][0]

                           #cursor.execute("select milk from orderdetails where phonenumber=={} AND orderdate=={} AND cost=={}".format(pn,bookingdate,cost))
                           #milk=cursor.fetchall()[0]

                           #cursor.execute("select water from orderdetails where phonenumber=={} AND orderdate=={} AND cost=={}".format(pn,bookingdate,cost))
                           #water=cursor.fetchall()[0]
                           
                           conn.commit()
                           conn.close()
                           
                           transaction_id=random.randint(1000000000000,999999999999999)
                                                 
                           incremented_date=datetime.datetime.now() + (datetime.timedelta(days=1))
                           bookingdate=incremented_date.strftime("%d-%m-%y")
                           def paid():
                               if re.match(condition_dc,dc_entry.get()):
                                   if re.match(condition_date,exdate_entry.get()):
                                       if re.match(condition_cvv,cvv_entry.get()):
                                           paiddebitcard()
                                       else:
                                         messagebox.showinfo('message','INVALID CVV NUMBER')
                                   else:
                                       messagebox.showinfo('message','INVALID DATE')
                               else:
                                   messagebox.showinfo('message','INVALID CARD NUMBER')
                                   
                           tableb=tkinter.Frame(root2,bg="white",padx=20,pady=20)
                           tableb.grid(row=0,column=0)
                           root2.grid_rowconfigure(0,weight=1)
                           root2.grid_columnconfigure(0,weight=1)
                           
                           dc=tkinter.Label(tableb,text="ENTER YOUR CARD NUMBER")
                           dc.grid(row=1,column=0)
                           dc_entry=tkinter.Entry(tableb)
                           dc_entry.grid(row=1,column=1)
                           condition_dc="^[0-9]{13,16}"

                           #idi=dc_entry.get()
                           #ids=str(idi)

                           exdate=tkinter.Label(tableb,text="MONTH/YEAR")
                           exdate.grid(row=2,column=0)
                           exdate_entry=tkinter.Entry(tableb)
                           exdate_entry.grid(row=2,column=1)
                           condition_date="^(0[1-9]|1[0-2])[/\-]([0-9]{2}|[0-9]{4})"


                           cvv=tkinter.Label(tableb,text="CVV")
                           cvv.grid(row=2,column=2)
                           cvv_entry=tkinter.Entry(tableb)
                           cvv_entry.grid(row=2,column=3)
                           condition_cvv="^[0-9]{3,4}"


                           pay=tkinter.Button(tableb,text="pay",bg="blue", activebackground="green",command=paid)
                           pay.grid(row=3,column=2)
                           
               def creditpay():
                           root2=tkinter.Tk()
                           root2.title("payment page")
                           root2.geometry("700x900")

                           def paidcreditcard():
                              
                              #if ids:
                                  conn=sqlite3.connect('user.db')
                                  cursor=conn.cursor()
                                  #cursor.execute("create table PAYMENT (phonenumber int,date str,T_method str,T_number int,amount int)")
                                  
                                  cursor.execute("insert into PAYMENT values(:phonenumber,:date,:T_method,:T_number,:amount,:housenumber,:address,:milk,:water)",
                                                 {
                                                     "phonenumber":pn,
                                                     "date":bookingdate,
                                                     "T_method":"CREDIT CARD",
                                                     "T_number":transaction_id,
                                                     "amount":cost,
                                                     "housenumber":housenumber,
                                                     "address":address,
                                                     "milk":milk,
                                                     "water":water
                                                     })
                                  messagebox.showinfo('message','ORDER SUCcESSFULL \n you will receive the items by {} at 5AM - 6AM \n THANK YOU '.format(bookingdate))
                                  conn.commit()
                                  conn.close()
                              #else:
                                   #messagebox.showinfo('message','INVALID CARD NUMBER')
                                                 
                           cost=totalcost
                           pn=p_number
                           milk=milk_no
                           water=watercan_no
                                                 
                           transaction_id=random.randint(1000000000000,999999999999999)
                                                 
                           incremented_date=datetime.datetime.now() + (datetime.timedelta(days=1))
                           bookingdate=incremented_date.strftime("%d-%m-%y")
                           
                           conn=sqlite3.connect("user.db")
                           cursor=conn.cursor()
                           cursor.execute("select housenumber from userinformation where phonenumber=={}".format(pn))
                           housenumber=cursor.fetchall()[0][0]

                           cursor.execute("select address from userinformation where phonenumber=={}".format(pn))
                           address=cursor.fetchall()[0][0]

                           #cursor.execute("select milk from orderdetails where phonenumber=={} AND orderdate=={} AND cost=={}".format(pn,bookingdate,cost))
                           #milk=cursor.fetchall()[0]

                           #cursor.execute("select water from orderdetails where phonenumber=={} AND orderdate=={} AND cost=={}".format(pn,bookingdate,cost))
                           #water=cursor.fetchall()[0]
                           
                           conn.commit()
                           conn.close()
                           def paid():
                               if re.match(condition_cc,cc_entry.get()):
                                   if re.match(condition_date,exdate_entry.get()):
                                       if re.match(condition_cvv,cvv_entry.get()):
                                           paidcreditcard()
                                       else:
                                         messagebox.showinfo('message','INVALID CVV NUMBER')
                                   else:
                                       messagebox.showinfo('message','INVALID DATE')
                               else:
                                   messagebox.showinfo('message','INVALID CARD NUMBER')
                        
                           tableb=tkinter.Frame(root2,bg="white",padx=20,pady=20)
                           tableb.grid(row=0,column=0)
                           root2.grid_rowconfigure(0,weight=1)
                           root2.grid_columnconfigure(0,weight=1)
                           
                           cc=tkinter.Label(tableb,text="ENTER YOUR CARD NUMBER")
                           cc.grid(row=1,column=0)
                           cc_entry=tkinter.Entry(tableb)
                           cc_entry.grid(row=1,column=1)
                           condition_cc="^[0-9]{13,16}"
                           #idi=dc_entry.get()
                           #ids=str(idi)

                           exdate=tkinter.Label(tableb,text="MONTH/YEAR")
                           exdate.grid(row=2,column=0)
                           exdate_entry=tkinter.Entry(tableb)
                           exdate_entry.grid(row=2,column=1)
                           condition_date="^(0[1-9]|1[0-2])[/\-]([0-9]{2}|[0-9]{4})"

                           cvv=tkinter.Label(tableb,text="CVV")
                           cvv.grid(row=2,column=2)
                           cvv_entry=tkinter.Entry(tableb)
                           cvv_entry.grid(row=2,column=3)
                           condition_cvv="^[0-9]{3,4}"

                           pay=tkinter.Button(tableb,text="pay",bg="blue", activebackground="green",command=paid)
                           pay.grid(row=3,column=2)
                   
                  # payment_method=Radiobutton(root1,text=methods[0],variable=m,value=methods[0])
                   #payment_method.grid(row=8,column=1)
                   #payment_method=Radiobutton(root1,text=methods[1],variable=m,value=methods[1])
                   #payment_method.grid(row=9,column=1)
                   #payment_method=Radiobutton(root1,text=methods[2],variable=m,value=methods[2])
                   #payment_method.grid(row=10,column=1)
                   #selection=m.get()
                   #use=Button(root1,text="CHOOSE",command=paypage)
                   #use.grid(row=11,column=1)

                   
                                    
                       
                   
               
               milk_no=milknos
               watercan_no=watercannos
               cost=Label(root1,text="PAYABLE AMOUNT RS:{}".format(totalcost))
               cost.grid(row=5,column=1)
               p_number=phonenumberid
    

               payable_amount=tkinter.Label(tablea,text="RS : {}".format(totalcost))
               payable_amount.grid(row=6,column=1)

               payment=tkinter.Button(tablea,text='UPI',bg="blue", activebackground="green",command=upipay)
               payment.grid(row=7,column=1)

               payment=tkinter.Button(tablea,text='DEBIT CARD',bg="blue", activebackground="green",command=debitpay)
               payment.grid(row=8,column=1)

               payment=tkinter.Button(tablea,text='CREDIT',bg="blue", activebackground="green",command=creditpay)
               payment.grid(row=9,column=1)

               
         def submit():
             if re.match(condition_milk,milk_entry.get()):
                 if re.match(condition_watercan,watercan_entry.get()):
                     submitorder()
                 else:
                     messagebox.showinfo("message","enter valid number in watercan")
             else:
                 messagebox.showinfo("message","enter valid number in milk")
        #front end for date
         root1.title("choose product")
         root1.geometry("800x1000")

         tablea=tkinter.Frame(root1,bg="white",padx=20,pady=20)
         tablea.grid(row=0,column=0)
         root1.grid_rowconfigure(0,weight=1)
         root1.grid_columnconfigure(0,weight=1)
         
         
         if phonenumberget=="7402615190":
             if passwordget=="Abcd@123":
                 view=tkinter.Button(tablea,text="VIEW DATABASE",bg="blue", activebackground="green",command=view)
                 view.grid(row=2,column=3)
         #phonenumberid=Label(root1,text='PHONE NUMBER')
         #phonenumberid.grid(row=1,column=0)
         #phonenumberid_entry=Entry(root1)
         #phonenumberid_entry.grid(row=1,column=1)
         phonenumberid=phonenumberget

         

         date=tkinter.Label(tablea,text="Your are booking for the {} day".format(bookingdate))
         date.grid(row=1,column=1)

         user=tkinter.Label(tablea,text="CHOOSE PRODUCT")
         user.config(font=("Arial",20))
         user.grid(row=0,column=1)
         
         milk=tkinter.Label(tablea,text='MILK(NOS)450ml')
         milk.grid(row=2,column=0)  
         milk_entry=tkinter.Entry(tablea)
         milk_entry.grid(row=2,column=1)
         condition_milk="[0-9]+"
         milk_amount=tkinter.Label(tablea,text="X $23")
         milk_amount.grid(row=2,column=2)

         watercan=tkinter.Label(tablea,text='WATER CAN(NOS)30L')
         watercan.grid(row=3,column=0)  
         watercan_entry=tkinter.Entry(tablea)
         watercan_entry.grid(row=3,column=1)
         condition_watercan="[0-9]+"
         watercan_amount=tkinter.Label(tablea,text="X $30")
         watercan_amount.grid(row=3,column=2)


         signup=tkinter.Button(tablea,text='SUBMIT',bg="blue", activebackground="green",command=submit)
         signup.grid(row=4,column=1)


        #conn=sqlite3.connect("user.db")
        #cursor=conn.cursor()
        #cursor.execute("create table orderdetails(orderdate str,phonenumber int,milk int,watercan int, cost int)")
        #conn.commit()

        #conn.close()
    else:
         messagebox.showinfo('message','no user pannel')
    conn.commit()
    conn.close()

def submit():
    if re.match(condition_name,name_entry.get()):
        if re.match(condition_phonenumber,phonenumber_entry.get()):
            if re.match(condition_mail,mailid_entry.get()):
                if re.match(condition_housenumber,housenumber_entry.get()):
                    if re.match(condition_address,address_entry.get()):
                        if re.match(condition_password,password_entry.get()):
                            submition()
                        else:
                            messagebox.showinfo("message","enter  the password  with  atleast one capsletter,small letter,any symbol and must contain 8characters")
                            
                    else:
                        messagebox.showinfo("message","enter the address only by alphabets ")
                    
                else:
                    messagebox.showinfo("message","enter only  numbers in housenumber ")
                
            else:
                messagebox.showinfo("message","enter the valid email id")
            
        else:
            messagebox.showinfo("message","phone number must contain 10digit number only")
        
    else:
        messagebox.showinfo("message","enter the name only in alphabets")
    
                                                                                                                                                                                                                                  
#tikinter for front end login page
#bg1_image = Image.open("background1.jpg")
#bg1_photo = ImageTk.PhotoImage(bg1_image)

root.title('signup')
#root.geometry('1000x800')


#root.configure(bg=bg1_photo)

new_user=tkinter.Label(tablen,text="NEW USER")
new_user.config(font=("Arial",20))
new_user.grid(row=0,column=1)

condition_name="\D"
name=tkinter.Label(tablen,text='NAME')
name.grid(row=1,column=0)  
name_entry=tkinter.Entry(tablen)
name_entry.grid(row=1,column=1)


condition_phonenumber="\d{10}"
phonenumber=tkinter.Label(tablen,text='PHONE NUMBER')
phonenumber.grid(row=2,column=0)
phonenumber_entry=tkinter.Entry(tablen)
phonenumber_entry.grid(row=2,column=1)

old_user=tkinter.Label(table,text="EXISTING USER")
old_user.config(font=("Arial",20))
old_user.grid(row=0,column=6)
phonenumberlogin=tkinter.Label(table,text='PHONE NUMBER')
phonenumberlogin.grid(row=1,column=5)
phonenumberlogin_entry=tkinter.Entry(table)
phonenumberlogin_entry.grid(row=1,column=6)

phonenumberid=[phonenumber_entry.get()]
#session["mobilnumber"]= phonenumber_entry.get()
print(phonenumberid[0])

condition_mail="^([a-zA-Z0-9_.+-]+\.)*[a-zA-Z0-9_.+-]+@gmail.com"
mailid=tkinter.Label(tablen,text='MAIL ID')
mailid.grid(row=3,column=0)
mailid_entry=tkinter.Entry(tablen)
mailid_entry.grid(row=3,column=1)

condition_housenumber="[0-9]+"
housenumber=tkinter.Label(tablen,text='HOUSE NUMBER')
housenumber.grid(row=4,column=0)
housenumber_entry=tkinter.Entry(tablen)
housenumber_entry.grid(row=4,column=1)

condition_address="\D"
address=tkinter.Label(tablen,text='ADDRESS')
address.grid(row=5,column=0)
address_entry=tkinter.Entry(tablen)
address_entry.grid(row=5,column=1)

condition_password="^(?=.{8,}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-=]).*$"
password=tkinter.Label(tablen,text='ENTER PASSWORD')
password.grid(row=6,column=0)
password_entry=tkinter.Entry(tablen)
password_entry.grid(row=6,column=1)

passwordlogin=tkinter.Label(table,text='ENTER PASSWORD')
passwordlogin.grid(row=2,column=5)
passwordlogin_entry=tkinter.Entry(table)
passwordlogin_entry.grid(row=2,column=6)



signup=tkinter.Button(tablen,text='SIGN UP',bg="blue", activebackground="green",command=submit)
signup.grid(row=7,column=1)

login=tkinter.Button(table,text='LOGIN',bg="blue", activebackground="green",command=check)
login.grid(row=3,column=6)

cancel=tkinter.Button(tablen,text='CANCEL',bg="yellow", activebackground="red",command=root.destroy)
cancel.grid(row=7,column=5)

#hint=Label(root,text="If your are a EXISTING USER please enter [PHONE NUMBER] and [PASSWORD] ONLY")
#hint.grid(row=9,column=0)

#conn=sqlite3.connect('user.db')
#cursor=conn.cursor()
#cursor.execute("create table userinformation(name int,phonenumber int,mailid text, housenumber int, address text,password text)")
#conn.commit()
#conn.close()

