from tkinter import *
import sqlite3
import tkinter.messagebox
conn=sqlite3.connect('E:\Projects\Store management system\databases\store.db')
c=conn.cursor()

result=c.execute("SELECT Max(id) from inventory")
for r in result:
    id=r[0]

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master=master
        self.heading=Label(master, text="Add to the Database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=400,y=0)

        #self.i=Label(master,text="ID has reached upto: "+ str(id), font=('arial 18 bold'))
        #self.i.place(x=0,y=40)
        
        self.name1=Label(master, text="Enter product name", font=('arial 18 bold'), fg='red')
        self.name1.place(x=0,y=70)

        self.stock1=Label(master, text="Enter Stocks", font=('arial 18 bold'), fg='red')
        self.stock1.place(x=0,y=110)
        
        self.cp1=Label(master, text="Enter Cost Price", font=('arial 18 bold'), fg='red')
        self.cp1.place(x=0,y=150)
        
        self.sp1=Label(master, text="Enter Selling Price", font=('arial 18 bold'), fg='red')
        self.sp1.place(x=0,y=190)
        
        self.vendor1=Label(master, text="Enter Vendor name", font=('arial 18 bold'), fg='red')
        self.vendor1.place(x=0,y=230)

        self.vendorno1=Label(master, text="Enter Vendor Phone No.", font=('arial 18 bold'), fg='red')
        self.vendorno1.place(x=0,y=270)

        self.id1=Label(master, text="Enter ID", font=('arial 18 bold'), fg='red')
        self.id1.place(x=0,y=310)

        self.name_e=Entry(master,width=25,font=('arial 18 bold'))
        self.name_e.place(x=380,y=70)
        
        self.stock_e=Entry(master,width=25,font=('arial 18 bold'))
        self.stock_e.place(x=380,y=110)
        
        self.cp_e=Entry(master,width=25,font=('arial 18 bold'))
        self.cp_e.place(x=380,y=150)
        
        self.sp_e=Entry(master,width=25,font=('arial 18 bold'))
        self.sp_e.place(x=380,y=190)
        
        self.vendor_e=Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_e.place(x=380,y=230)
        
        self.vendorno_e=Entry(master,width=25,font=('arial 18 bold'))
        self.vendorno_e.place(x=380,y=270)

        self.id_e=Entry(master,width=25,font=('arial 18 bold'))
        self.id_e.place(x=380,y=310)

        self.btnadd=Button(master, text="add to db", width=25,height=2,bg='steelblue', fg='white',command=self.get_item)
        self.btnadd.place(x=520,y=360)

        self.btnadd=Button(master, text="clear all fields", width=18,height=2,bg='lightgreen', fg='white',command=self.clear_all)
        self.btnadd.place(x=350,y=360)

        self.tBox=Text(master,width=60,height=14.4)
        self.tBox.place(x=750,y=70)
        self.tBox.insert(END,"ID has reached upto: "+ str(id))
        
        self.master.bind('<Return>',self.get_item)
        self.master.bind('<Up>',self.clear_all)

    def get_item(self,*args,**kwargs):
        self.name=self.name_e.get()
        self.stock=self.stock_e.get()
        self.cp=self.cp_e.get()
        self.sp=self.sp_e.get()
        self.vendor=self.vendor_e.get()
        self.vendorno=self.vendorno_e.get()

        self.totalcp=float(self.cp)*float(self.stock)
        self.totalsp=float(self.sp)*float(self.stock)
        self.assumed_profit=float(self.totalsp-self.totalcp)
        
        if self.name== '' or self.stock== '' or self.cp== '' or self.sp== ''  :
            #print("Empty")
            tkinter.messagebox.showinfo('Error','Please fill all details')
        else:
            #print("Continue Further")
            sql="INSERT INTO inventory (name,stock,cost_price,selling_price,total_costprice,total_sellingprice,assumed_profit,vendor,vendor_phno) VALUES(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name,self.stock,self.cp,self.sp,self.totalcp,self.totalsp,self.assumed_profit,self.vendor,self.vendorno))
            conn.commit()

            self.tBox.insert(END,"\n\nInserted " + str(self.name) + " into the database with code " + str(self.id_e.get()))
            tkinter.messagebox.showinfo('Success','Successfully added to db')

    def clear_all(self,*args,**kwargs):
          self.name_e.delete(0,END)
          self.stock_e.delete(0,END)
          self.cp_e.delete(0,END)
          self.sp_e.delete(0,END)
          self.vendor_e.delete(0,END)
          self.vendorno_e.delete(0,END)
          self.id_e.delete(0,END)

root=Tk()
b=Database(root)
root.geometry("1366x768+0+0")
root.title('Add to the database')
root.mainloop()


