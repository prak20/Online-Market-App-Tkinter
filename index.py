from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import random
import os
conn=sqlite3.connect('E:\Projects\Store management system\databases\store.db')
c=conn.cursor()

date=datetime.datetime.now().date()

prod_list=[]
prod_price=[]
prod_quantity=[]
prod_id=[]

label_list=[]

class application:
    def __init__(self,master,*args,**kwargs):
        self.master=master
        #frame
        self.left=Frame(master,width=700,height=768,bg='white')
        self.left.pack(side=LEFT)

        self.right=Frame(master,width=666,height=768,bg='lightgreen')
        self.right.pack(side=RIGHT)

        #components
        self.heading=Label(self.left, text="अपना शहर अपनी दुकान ", font=('arial 38 bold'),bg='white',fg='salmon')
        self.heading.place(x=0,y=0)

        self.date_1=Label(self.right, text='Today Date is :'+str(date), font=('arial 20 bold'),bg='yellow',fg='red')
        self.date_1.place(x=0,y=0)

        #table invoice
        self.tproduct=Label(self.right, text="Products", font=('arial 25 bold'),bg='lightgreen',fg='blue4')
        self.tproduct.place(x=0,y=60)

        self.tquantity=Label(self.right, text="Quantity", font=('arial 25 bold'),bg='lightgreen',fg='blue4')
        self.tquantity.place(x=260,y=60)

        self.tamount=Label(self.right, text="Amount", font=('arial 25 bold'),bg='lightgreen',fg='blue4')
        self.tamount.place(x=520,y=60)

        self.enterid=Label(self.left, text="Enter Product ID", font=('arial 20 bold'),bg='white')
        self.enterid.place(x=0,y=80)

        self.enteride=Entry(self.left, width=20 ,font=('arial 20 bold'),bg='lightblue')
        self.enteride.place(x=320,y=80)
        self.enteride.focus()

        self.searchbtn=Button(self.left, text='Search',width=20 ,height=2,bg='orange',command=self.ajax)
        self.searchbtn.place(x=370,y=120)

        self.productname=Label(self.left, text="", font=('arial 20 bold'),bg='white',fg='steelblue')
        self.productname.place(x=0,y=220)

        self.pprice=Label(self.left, text="", font=('arial 20 bold'),bg='white',fg='steelblue')
        self.pprice.place(x=0,y=260)

        #total label
        self.total1=Label(self.right, text="", font=('arial 30 bold'),bg='lightgreen',fg='magenta')  #bg='lightblue'
        self.total1.place(x=0,y=600)

        self.master.bind('<Return>',self.ajax)
        self.master.bind('<Up>',self.add_to_cart)
        self.master.bind('<space>',self.gen_bill)

    def ajax(self,*args,**kwargs):
        self.get_id=self.enteride.get()
        query='SELECT * from inventory WHERE id=?'
        result=c.execute(query,(self.get_id,))
        for self.r in result:
            self.get_id=self.r[0]
            self.get_name=self.r[1]
            self.get_price=self.r[4]
            self.get_stock=self.r[2]

        self.productname.configure(text="Product Name: "+str(self.get_name))
        self.pprice.configure(text="Price Rs: "+str(self.get_price))

        self.quantity1=Label(self.left, text="Enter Number of Products: ", font=('arial 18 bold'),bg='white')
        self.quantity1.place(x=0,y=330)

        self.quantitye=Entry(self.left, width=23, font=('arial 18 bold'),bg='lightblue')
        self.quantitye.place(x=320,y=330)
        self.quantitye.focus()

        self.disc1=Label(self.left, text="Enter Discount: ", font=('arial 18 bold'),bg='white')
        self.disc1.place(x=0,y=380)

        self.disce=Entry(self.left, width=23, font=('arial 18 bold'),bg='lightblue')
        self.disce.place(x=320,y=380)
        self.disce.insert(END,0)

        self.addtocartbtn=Button(self.left, text='Add to Cart',width=20 ,height=2,bg='orange',command=self.add_to_cart)
        self.addtocartbtn.place(x=370,y=420)

        self.change1=Label(self.left, text="Given Amount: ", font=('arial 18 bold'),bg='white')
        self.change1.place(x=0,y=470)

        self.changee=Entry(self.left, width=23,font=('arial 18 bold'),bg='lightblue')
        self.changee.place(x=320,y=470)

        self.changebtn=Button(self.left, text='Calculate Bill',width=20 ,height=2,bg='orange',command=self.change_func)
        self.changebtn.place(x=370,y=510)

        self.billbtn=Button(self.left, text='Generate Bill',width=80 ,height=2,bg='red',fg='white',command=self.gen_bill)
        self.billbtn.place(x=50,y=610)

    def add_to_cart(self,*args,**kwargs):

        #get quantity value
        self.quant_value=int(self.quantitye.get())
        if self.quant_value>int(self.get_stock):
            tkinter.messagebox.showinfo("Error",'Not that many products in our inventory')
        else:
            self.final_price=(float(self.quant_value)*float(self.get_price))-(float(self.disce.get()))

            prod_list.append(self.get_name)
            prod_price.append(self.final_price)
            prod_quantity.append(self.quant_value)
            prod_id.append(self.get_id)
            #print(prod_list)
            #print(prod_price)
            #print(prod_quantity)

            self.x_index=0
            self.y_index=140
            self.count=0
            for self.p in prod_list:
                self.tempname=Label(self.right, text=str(prod_list[self.count]), font=('arial 20 bold'),bg='lightgreen',fg='red')
                self.tempname.place(x=25, y=self.y_index)
                label_list.append(self.tempname)

                self.tempqt=Label(self.right, text=str(prod_quantity[self.count]), font=('arial 20 bold'),bg='lightgreen',fg='red')
                self.tempqt.place(x=300, y=self.y_index)
                label_list.append(self.tempqt)

                self.tempprice=Label(self.right, text=str(prod_price[self.count]), font=('arial 20 bold'),bg='lightgreen',fg='red')
                self.tempprice.place(x=520, y=self.y_index)
                label_list.append(self.tempprice)

                self.y_index+=40
                self.count+=1

                #total configure
                self.total1.configure(text="Total Rs: " +str(sum(prod_price)))

                #delete
                self.quantity1.place_forget()
                self.quantitye.place_forget()
                self.disc1.place_forget()
                self.disce.place_forget()
                #self.change1.place_forget()
                #self.changee.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.addtocartbtn.destroy()
                #self.changebtn.destroy()

                #autofocus
                self.enteride.focus()
                self.enteride.delete(0,END)
    def  change_func(self,*args,**kwargs):
        #get amount given by customer
        self.amt_given=float(self.changee.get())
        self.our_total=float(sum(prod_price))
        self.to_give=self.amt_given-self.our_total

        self.c_amt=Label(self.left, text='Change Rs:' +str(self.to_give), font=('arial 18 bold'),bg='white',fg='red')
        self.c_amt.place(x=350, y=570)

    def gen_bill(self,*args,**kwargs):
        #create bill before updating db
        directory='E:/Projects/Store management system/invoice/' + str(date) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        #create templates
        company = "\t\t\t\tअपना शहर अपनी दुकान Pvt. Ltd.\n"
        address="\t\t\t\tUttar Pradesh , India\n"
        phone="\t\t\t\t9999999999\n"
        sample="\t\t\t\tInvoice\n"
        dt="\t\t\t\t" + str(date)

        table_header="\n\n\t\t\t...............................................................\n\t\tSN.\t\tProducts\t\tQty\t\tAmount\n\t\t\t..............................................................."
        final=company+address+phone+sample+dt+"\n"+table_header

        #open file
        file_name=str(directory)+str(random.randrange(5000,10000)) + ".rtf"
        with open(file_name, "w",encoding="utf-8") as f:
            f.write(final)
           #fill dynamic
            r=1
            i=0
            for t in prod_list:
                f.write("\n\t\t" + str(r) + "\t\t"  + str(prod_list[i] +".......")[:7] +"\t\t" + str(prod_quantity[i]) + "\t\t" + str(prod_price[i]))
                i+=1
                r+=1

            f.write('\n\n\n\tTotal Amount is Rs.' + str(sum(prod_price)))
            f.write('\n\tThanks for Visiting! \n \tDo Shop here Again!')
            os.startfile(file_name,"print")
            
        #decerase stock  
        self.x=0
        initial="SELECT * FROM inventory WHERE id=?"
        result=c.execute(initial,(prod_id[self.x],))


        for i in prod_list:
            for r in result:
               self.old_stock=r[2]
            self.new_stock=int(self.old_stock)-int(prod_quantity[self.x])

            #updating stock of the store
            sql="UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql,(self.new_stock,prod_id[self.x]))
            conn.commit()

            #insert into transaction
            sql2="INSERT INTO transactions (prod_name,quantity, amount, date) VALUES (?,?,?,?)"
            c.execute(sql2,(prod_list[self.x],prod_quantity[self.x],prod_price[self.x],date))
            conn.commit()
            self.x+=1
        for a in label_list:
            a.destroy()
        del(prod_list[:])
        del(prod_id[:])
        del(prod_quantity[:])
        del(prod_price[:])

        self.total1.configure(text="")
        self.c_amt.configure(text="")
        self.changee.delete(0,END)
        self.enteride.focus()

        tkinter.messagebox.showinfo("Success",'Everything Working fine')


root=Tk()
b=application(root)
root.geometry("1366x768+0+0")
root.mainloop()
