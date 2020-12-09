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
        self.heading=Label(master, text="Update to the Database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=400,y=0)

        #self.i=Label(master,text="ID has reached upto: "+ str(id), font=('arial 18 bold'))
        #self.i.place(x=0,y=40)

        self.id_le=Label(master, text="Enter id", font=('arial 18 bold'), fg='red')
        self.id_le.place(x=0,y=70)

        self.idleb=Entry(master,width=10,font=('arial 18 bold'))
        self.idleb.place(x=380,y=70)

        self.btnsrch=Button(master, text="Search", width=15,height=2,bg='orange',command=self.search)
        self.btnsrch.place(x=450,y=70)
        
        self.name1=Label(master, text="Enter product name", font=('arial 18 bold'), fg='red')
        self.name1.place(x=0,y=110)

        self.stock1=Label(master, text="Enter Stocks", font=('arial 18 bold'), fg='red')
        self.stock1.place(x=0,y=150)
        
        self.cp1=Label(master, text="Enter Cost Price", font=('arial 18 bold'), fg='red')
        self.cp1.place(x=0,y=190)
        
        self.sp1=Label(master, text="Enter Selling Price", font=('arial 18 bold'), fg='red')
        self.sp1.place(x=0,y=230)
        
        self.totalcp1=Label(master, text="Enter Total Cost Price", font=('arial 18 bold'), fg='red')
        self.totalcp1.place(x=0,y=270)
        
        self.totalsp1=Label(master, text="Enter Total Selling Price", font=('arial 18 bold'), fg='red')
        self.totalsp1.place(x=0,y=310)
        
        self.vendor1=Label(master, text="Enter Vendor name", font=('arial 18 bold'), fg='red')
        self.vendor1.place(x=0,y=350)
        

        self.vendorno1=Label(master, text="Enter Vendor Phone No.", font=('arial 18 bold'), fg='red')
        self.vendorno1.place(x=0,y=390)
        

        #self.id1=Label(master, text="Enter ID", font=('arial 18 bold'), fg='red')
        #self.id1.place(x=0,y=350)

        self.name_e=Entry(master,width=25,font=('arial 18 bold'))
        self.name_e.place(x=380,y=110)

        
        self.stock_e=Entry(master,width=25,font=('arial 18 bold'))
        self.stock_e.place(x=380,y=150)
        
        
        self.cp_e=Entry(master,width=25,font=('arial 18 bold'))
        self.cp_e.place(x=380,y=190)
        
        self.sp_e=Entry(master,width=25,font=('arial 18 bold'))
        self.sp_e.place(x=380,y=230)

        self.totalcp_e=Entry(master,width=25,font=('arial 18 bold'))
        self.totalcp_e.place(x=380,y=270)
        
        self.totalsp_e=Entry(master,width=25,font=('arial 18 bold'))
        self.totalsp_e.place(x=380,y=310)
        
        
        self.vendor_e=Entry(master,width=25,font=('arial 18 bold'))
        self.vendor_e.place(x=380,y=350)
        
        
        self.vendorno_e=Entry(master,width=25,font=('arial 18 bold'))
        self.vendorno_e.place(x=380,y=390)



        #self.id_e=Entry(master,width=25,font=('arial 18 bold'))
        #self.id_e.place(x=380,y=350)


        self.btnadd=Button(master, text="Update the Database", width=25,height=2,bg='steelblue', fg='white',command=self.update)
        self.btnadd.place(x=520,y=430)


        #self.btnclear=Button(master, text="clear all fields", width=18,height=2,bg='lightgreen', fg='white')  #command=self.clear_all
        #self.btnclear.place(x=350,y=430)


        self.tBox=Text(master,width=60,height=14.4)
        self.tBox.place(x=750,y=70)
        self.tBox.insert(END,"ID has reached upto: "+ str(id))


    def search(self,*args,**kwargs):
        sql='SELECT * FROM inventory WHERE id=?'
        result=c.execute(sql,(self.idleb.get(),))
        for r in result:
            self.n1=r[1] #name
            self.n2=r[2] #stock
            self.n3=r[3] #cp
            self.n4=r[4] #sp
            self.n5=r[5] #totalcp
            self.n6=r[6] #totalsp
            self.n7=r[7] #assumedprofit
            self.n8=r[8] #vendor
            self.n9=r[9] #vendorphno
        conn.commit()


        self.name_e.delete(0,END)
        self.name_e.insert(0,str(self.n1))
        self.stock_e.delete(0,END)
        self.stock_e.insert(0,str(self.n2))
        self.cp_e.delete(0,END)
        self.cp_e.insert(0,str(self.n3))
        self.sp_e.delete(0,END)
        self.sp_e.insert(0,str(self.n4))
        self.vendor_e.delete(0,END)
        self.vendor_e.insert(0,str(self.n8))
        self.vendorno_e.delete(0,END)
        self.vendorno_e.insert(0,str(self.n9))
        self.totalcp_e.delete(0,END)
        self.totalcp_e.insert(0,str(self.n5))
        self.totalsp_e.delete(0,END)
        self.totalsp_e.insert(0,str(self.n6))

    def update(self,*args,**kwargs):
        self.u1=self.name_e.get()
        self.u2=self.stock_e.get()
        self.u3=self.cp_e.get()
        self.u4=self.sp_e.get()
        self.u5=self.totalcp_e.get()
        self.u6=self.totalsp_e.get()
        self.u7=self.vendor_e.get()
        self.u8=self.vendorno_e.get()

        query="UPDATE inventory SET name=?, stock=?, cost_price=?, selling_price=?, total_costprice=?, total_sellingprice=?, vendor=?, vendor_phno=? WHERE id=?"
        c.execute(query,(self.u1,self.u2,self.u3,self.u4,self.u5,self.u6,self.u7,self.u8,self.idleb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success","Update  the Database")

      
root=Tk()
b=Database(root)
root.geometry("1366x768+0+0")
root.title('Update to the database')
root.mainloop()
