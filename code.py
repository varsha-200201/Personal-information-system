from tkinter import *
#from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    Aadharid = e_Aadharid.get()
    username = e_username.get();
    passw = e_passw.get();
    
    if(Aadharid=="" or username=="" or passw==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("insert into data values('"+ Aadharid +"','"+ username +"','"+ passw +"')")
        cursor.execute("commit");
        
        e_Aadharid.delete(0,'end')
        e_username.delete(0,'end')
        e_passw.delete(0,'end')
        show()
        MessageBox.showinfo("Insert Status","Inserted Successfully");
        con.close();
    
def delete():
    if(e_Aadharid.get() == ""):
        MessageBox.showinfo("Delete Status","ID is compulsary for delete")
    else:
        con = mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("delete from data where Aadharid='"+ e_Aadharid.get() +"'")
        cursor.execute("commit");
        
        e_Aadharid.delete(0,'end')
        e_username.delete(0,'end')
        e_passw.delete(0,'end')
        MessageBox.showinfo("Delete Status","Deleted Successfully");
        show()
        con.close();
def update():
    Aadharid = e_Aadharid.get()
    username = e_username.get();
    passw = e_passw.get();
    
    if(Aadharid=="" or username=="" or passw==""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("update data set username='"+ username +"', passw='"+ passw +"' where Aadharid='"+ Aadharid +"'")
        cursor.execute("commit");
        
        e_Aadharid.delete(0,'end')
        e_username.delete(0,'end')
        e_passw.delete(0,'end')
        show()
        MessageBox.showinfo("Update Status","Updateted Successfully");
        con.close();
    
def get():
    if(e_Aadharid.get() == ""):
        MessageBox.showinfo("Fetch Status","ID is compulsary for delete")
    else:
        con = mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("select*from data where Aadharid='"+ e_Aadharid.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            e_username.insert(0, row[1])
            e_passw.insert(0, row[2])
        con.close();
        
def nextstep():
    Aadharid = e_Aadharid.get()
    username = e_username.get();
    passw = e_passw.get();
    
    if(Aadharid=="" or username=="" or passw==""):
        MessageBox.showinfo("NEXT STATUS","NEXT ")
    else:
        con=mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("commit");
        e_Aadharid.delete(0,'end')
        e_username.delete(0,'end')
        e_passw.delete(0,'end')
        MessageBox.showinfo("YOUR FILES OR RECORDED")
        con.close();
    root.destroy()
    return

        
def show():
    con = mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
    cursor=con.cursor()
    cursor.execute("select*from data")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    

    for row in rows:
        insertData = str(row[0])+'         '+ row[1]
        list.insert(list.size()+1, insertData)

    con.close();
root = Tk()
root.geometry("600x400");
root.title("MINIPROJECT");

Aadharid = Label(root,text=' ID',font=('bold',10))
Aadharid.place(x=20,y=30);

username = Label(root,text=' NAME',font=('bold',10))
username.place(x=20,y=60);

passw = Label(root,text='PASSWORD',font=('bold',10))
passw.place(x=20,y=90);

e_Aadharid = Entry()
e_Aadharid.place(x=150,y=30)

e_username = Entry()
e_username.place(x=150,y=60)
           
e_passw = Entry()
e_passw.place(x=150,y=90)

insert =Button(root,text="Insert",font=("italic",10), bg="white",command=insert)
insert.place(x=20,y=140)

delete =Button(root,text="Delete",font=("italic",10), bg="white",command=delete)
delete.place(x=70,y=140)

update =Button(root,text="Update",font=("italic",10), bg="white",command=update)
update.place(x=130,y=140)

get =Button(root,text="Get",font=("italic",10), bg="white",command=get)
get.place(x=190,y=140)

next=Button(root,text="NEXT",font=('bold',10),bg="white",command=nextstep)
next.place(x=250,y=140)


list = Listbox(root)
list.place(x=350,y=30)
show()
root.mainloop()


################################################################################################# FORM1

newwindow=Tk()
newwindow.title("personal information")
newwindow.geometry("700x650")
lbl=Label(newwindow,text="BASIC DETAILS")
lbl.pack()
name=Label(newwindow,text="NAME",font=('bold',10))
name.place(x=30,y=40)

age=Label(newwindow,text="AGE",font=('bold',10))
age.place(x=30,y=80)

gender=Label(newwindow,text="GENDER",font=('bold',10))
gender.place(x=30,y=120)

nationality=Label(newwindow,text="NATIONALITY",font=('bold',10))
nationality.place(x=30,y=160)

mobileno=Label(newwindow,text="MOBILE NUMBER",font=('bold',10))
mobileno.place(x=30,y=200)

doorno=Label(newwindow,text="DOOR NUMBER",font=('bold',10))
doorno.place(x=30,y=240)

streetname=Label(newwindow,text="STREET NAME",font=('bold',10))
streetname.place(x=30,y=280)

area=Label(newwindow,text="AREA",font=('bold',10))
area.place(x=30,y=320)

city=Label(newwindow,text="CITY",font=('bold',10))
city.place(x=30,y=360)

state=Label(newwindow,text="STATE",font=('bold',10))
state.place(x=30,y=400)

dob=Label(newwindow,text="DATE OF BIRTH",font=('bold',10))
dob.place(x=30,y=440)

e_name=Entry()
e_name.place(x=200,y=40)

e_age=Entry()
e_age.place(x=200,y=80)

e_gender=Entry()
e_gender.place(x=200,y=120)

e_nationality=Entry()
e_nationality.place(x=200,y=160)

e_mobileno=Entry()
e_mobileno.place(x=200,y=200)

e_doorno=Entry()
e_doorno.place(x=200,y=240)

e_streetname=Entry()
e_streetname.place(x=200,y=280)

e_area=Entry()
e_area.place(x=200,y=320)

e_city=Entry()
e_city.place(x=200,y=360)

e_state=Entry()
e_state.place(x=200,y=400)

e_dob=Entry()
e_dob.place(x=200,y=440)
#form2
from tkinter import *
#from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
def insert():
    name=e_name.get();
    age=e_age.get();
    gender=e_gender.get();
    nationality=e_nationality.get();
    mobileno=e_mobileno.get();
    doorno=e_doorno.get();
    streetname=e_streetname.get();
    area=e_area.get();
    city=e_city.get();
    state=e_state.get();
    dob=e_dob.get();

    if(name=="" or age=="" or gender=="" or nationality==""or mobileno=="" or doorno==""or streetname==""or area==""or city==""or state==""or dob==""):
         MessageBox.showinfo("INSERT STATUS","ALL FIELDS ARE REQUIRED")
    else:
        con=mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("insert into files values('"+name+"','"+age+"','"+gender+"','"+nationality+"','"+mobileno+"','"+doorno+"','"+streetname+"','"+area+"','"+city+"','"+state+"','"+dob+"')")
        cursor.execute("commit");
        e_name.delete(0,'end')
        e_age.delete(0,'end')
        e_gender.delete(0,'end')
        e_nationality.delete(0,'end')
        e_mobileno.delete(0,'end')
        e_doorno.delete(0,'end')
        e_streetname.delete(0,'end')
        e_area.delete(0,'end')
        e_city.delete(0,'end')
        e_state.delete(0,'end')
        e_dob.delete(0,'end')
        MessageBox.showinfo("INSERT STATUS","INSERTED SUCCESSFULLY");
        con.close();

def  nextone():
    name=e_name.get();
    age=e_age.get();
    gender=e_gender.get();
    nationality=e_nationality.get();
    mobileno=e_mobileno.get();
    doorno=e_doorno.get();
    streetname=e_streetname.get();
    area=e_area.get();
    city=e_city.get();
    state=e_state.get();
    dob=e_dob.get();

    if (name==""or age==""or gender==""or nationality==""or mobileno=="" or doorno==""or streetname==""or area==""or city==""or state==""or dob==""):
        MessageBox.showinfo("INSERT STATUS","ALL FIELDS ARE REQUIRED")
    else:
        con=mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("commit")
        e_name.delete(0,'end')
        e_age.delete(0,'end')
        e_gender.delete(0,'end')
        e_nationality.delete(0,'end')
        e_mobileno.delete(0,'end')
        e_doorno.delete(0,'end')
        e_streetname.delete(0,'end')
        e_area.delete(0,'end')
        e_city.delete(0,'end')
        e_state.delete(0,'end')
        e_dob.delete(0,'end')
        MessageBox.showinfo("NEXT");
        con.close;
    newwindow.destroy()
    return
    
insert=Button(newwindow,text="INSERT",font=('bold',10),bg="white",command=insert)
insert.place(x=270,y=540)

nextone=Button(newwindow,text="NEXT",font=('bold',10),bg="white",command=nextone)
nextone.place(x=350,y=540)


newwindow.mainloop()
##################################################################FORM 3

 #form2
newwindow2=Tk()
newwindow2.title("personal information")
newwindow2.geometry("750x600")
lbl=Label(newwindow2,text="OTHERS DETAILS")
lbl.pack()
fathername=Label(newwindow2,text="FATHER NAME",font=('bold',10))
fathername.place(x=30,y=40)

mothername=Label(newwindow2,text="MOTHER NAME",font=('bold',10))
mothername.place(x=30,y=80)

accno=Label(newwindow2,text="ACCOUNT NUMBER",font=('bold',10))
accno.place(x=30,y=120)

bankname=Label(newwindow2,text="BANK NAME",font=('bold',10))
bankname.place(x=30,y=160)

IFSC=Label(newwindow2,text="IFSC CODE",font=('bold',10))
IFSC.place(x=30,y=200)

creditno=Label(newwindow2,text="CREDIT CARD NUMBER",font=('bold',10))
creditno.place(x=30,y=240)

tenthmark=Label(newwindow2,text="TENTH MARKSHEET",font=('bold',10))
tenthmark.place(x=30,y=280)

twenthmark=Label(newwindow2,text="TWENTH MARKSHEET",font=('bold',10))
twenthmark.place(x=30,y=320)

cgpa=Label(newwindow2,text="CGPA",font=('bold',10))
cgpa.place(x=30,y=360)

#hobby=Label(newwindow2,text="HOBBY",font=('bold',10))
#hobby.place(x=30,y=400)


e_fathername=Entry()
e_fathername.place(x=200,y=40)

e_mothername=Entry()
e_mothername.place(x=200,y=80)

e_accno=Entry()
e_accno.place(x=200,y=120)

e_bankname=Entry()
e_bankname.place(x=200,y=160)

e_IFSC=Entry()
e_IFSC.place(x=200,y=200)

e_creditno=Entry()
e_creditno.place(x=200,y=240)

e_tenthmark=Entry()
e_tenthmark.place(x=200,y=280)

e_twenthmark=Entry()
e_twenthmark.place(x=200,y=320)

e_cgpa=Entry()
e_cgpa.place(x=200,y=360)

from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
def insert():
    fathername=e_fathername.get();
    mothername=e_mothername.get();
    accno=e_accno.get();
    bankname=e_bankname.get();
    IFSC=e_IFSC.get();
    creditno=e_creditno.get();
    tenthmark=e_tenthmark.get();
    twenthmark=e_twenthmark.get();
    cgpa=e_cgpa.get();

    if(fathername==" " or mothername==" " or accno==" " or bankname==" " or IFSC==" " or creditno==" " or tenthmark==" " or twenthmark==" "or cgpa==" "):
        MessageBox.showinfo("INSERT STATUS","ALL FIELDS ARE REQUIRED")
    else:
        con=mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("insert into education values('"+fathername+"','"+mothername+"','"+accno+"','"+bankname+"','"+IFSC+"','"+creditno+"','"+tenthmark+"','"+twenthmark+"','"+cgpa+"')")
        cursor.execute("commit");
        e_fathername.delete(0,'end')
        e_mothername.delete(0,'end')
        e_accno.delete(0,'end')
        e_bankname.delete(0,'end')
        e_IFSC.delete(0,'end')
        e_creditno.delete(0,'end')
        e_tenthmark.delete(0,'end')
        e_twenthmark.delete(0,'end')
        e_cgpa.delete(0,'end')
        MessageBox.showinfo("INSERT STATUS","SUBMITTED SUCCESSFULLY");
        con.close();


def next():
    fathername=e_fathername.get();
    mothername=e_mothername.get();
    accno=e_accno.get();
    bankname=e_bankname.get();
    IFSC=e_IFSC.get();
    creditno=e_creditno.get();
    tenthmark=e_tenthmark.get();
    twenthmark=e_twenthmark.get();
    cgpa=e_cgpa.get();

    if(fathername==" " or mothername==" " or accno==" " or bankname==" " or IFSC==" " or creditno==" " or tenthmark==" " or twenthmark==" "or cgpa==" "):
        MessageBox.showinfo("INSERT STATUS","ALL FIELDS ARE REQUIRED");
    else:
        con=mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("commit");
        e_fathername.delete(0,'end')
        e_mothername.delete(0,'end')
        e_accno.delete(0,'end')
        e_bankname.delete(0,'end')
        e_IFSC.delete(0,'end')
        e_creditno.delete(0,'end')
        e_tenthmark.delete(0,'end')
        e_twenthmark.delete(0,'end')
        e_cgpa.delete(0,'end')
        MessageBox.showinfo("NEXT");
        con.close();
    newwindow2.destroy()
    return

insert=Button(newwindow2,text="INSERT",font=('bold',10),bg="yellow",command=insert)
insert.place(x=270,y=540)

next=Button(newwindow2,text="NEXT",font=('bold',10),bg="yellow",command=next)
next.place(x=350,y=540)

newwindow2.mainloop()

################################################
newwindow3=Tk()
newwindow3.title("personal information")
newwindow3.geometry("700x650")
lb1=Label(newwindow3,text="SKILLS")
lb1.pack()
hobby=Label(newwindow3,text="HOBBY",font=('bold',10))
hobby.place(x=30,y=40)

sports=Label(newwindow3,text="SPORTS",font=('bold',10))
sports.place(x=30,y=80)

lang=Label(newwindow3,text="LANGUAGE-KNOWN",font=('bold',10))
lang.place(x=30,y=120)

e_hobby=Entry()
e_hobby.place(x=200,y=40)

e_sports=Entry()
e_sports.place(x=200,y=80)

e_lang=Entry()
e_lang.place(x=200,y=120)

from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def submit():
    hobby=e_hobby.get();
    sports=e_sports.get();
    lang=e_lang.get();
    if(hobby==" " or sports==" " or lang==" "):
        MessageBox.showinfo("INSERT STATUS","ALL FIELDS ARE REQUIRED")
    else:
        con=mysql.connect(host="localhost",user="root",password="sanmathi@2003",database="personalinformation")
        cursor=con.cursor()
        cursor.execute("insert into skills values('"+hobby+"','"+sports+"','"+lang+"')")
        cursor.execute("commit");
        e_hobby.delete(0,'end')
        e_sports.delete(0,'end')
        e_lang.delete(0,'end')
        MessageBox.showinfo("INSERT STATUS","SUBMITTED SUCCESSFULLY");
        con.close();
submit=Button(newwindow3,text="SUBMIT",font=('bold',10),bg="yellow",command=submit)
submit.place(x=250,y=300)

newwindow3.mainloop()