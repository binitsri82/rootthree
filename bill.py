from tkinter import *
from tkinter import messagebox
import math,random,os
import mysql.connector
import datetime
defproduct_mgmt( ):
while True :
print("\t\t\t 1. Add New Product")
print("\t\t\t 2. List Product")
print("\t\t\t 3. Update Product")
print("\t\t\t 4. Delete Product")
print("\t\t\t 5. Back (Main Menu)")
                      p=int (input("\t\tEnter Your Choice :"))
if p==1:
add_product()
if p==2:
search_product()
if p==3:
update_product()
if p==4:
delete_product()
if p== 5 :
break

defpurchase_mgmt( ):
while True :
print("\t\t\t 1. Add Order")
print("\t\t\t 2. List Order")
print("\t\t\t 3. Back (Main Menu)")
                      o=int (input("\t\tEnter Your Choice :"))
if o==1 :
add_order()
if o==2 :
list_order()
if o== 3 :
break

defsales_mgmt( ):
while True :
print("\t\t\t 1. Sale Items")
print("\t\t\t 2. List Sales")
print("\t\t\t 3. Back (Main Menu)")
                      s=int (input("\t\tEnter Your Choice :"))
if s== 1 :
sale_product()
if s== 2 :
list_sale()
if s== 3 :
break

defuser_mgmt( ):
while True :
print("\t\t\t 1. Add user")
print("\t\t\t 2. List user")
print("\t\t\t 3. Back (Main Menu)")
                      u=int (input("\t\tEnter Your Choice :"))
if u==1:
add_user()
if u==2:
list_user()
if u==3:
break

defcreate_database():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")				#change as per system
mycursor=mydb.cursor()
print(" Creating PRODUCT table")
sql = "CREATE TABLE if not exists product (\
pcodeint(4) PRIMARY KEY,\
pname char(30) NOT NULL,\
pprice float(8,2) ,\
pqtyint(4) ,\
pcatchar(30));"
mycursor.execute(sql)
print(" Creating ORDER table")
sql = "CREATE TABLE if not exists orders (\
orderidint(4)PRIMARY KEY ,\
orderdate DATE ,\
pcode char(30) NOT NULL , \
pprice float(8,2) ,\
pqtyint(4) ,\
supplier char(50),\
pcatchar(30));"
mycursor.execute(sql)
print(" ORDER table created")

print(" Creating SALES table")
sql = "CREATE TABLE if not exists sales (\
salesidint(4) PRIMARY KEY ,\
salesdate DATE ,\
pcode char(30) references product(pcode), \
pprice float(8,2) ,\
pqtyint(4) ,\
                  Total double(8,2)\
                  );"
mycursor.execute(sql)
print(" SALES table created")
sql = "CREATE TABLE if not exists user (\
uid char(6) PRIMARY KEY,\
uname char(30) NOT NULL,\
upwdchar(30));"
mycursor.execute(sql)
print(" USER table created")

deflist_database():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")   					#change as per system
mycursor=mydb.cursor()
sql="show tables;"
mycursor.execute(sql)
fori in mycursor:
print(i)

defadd_order():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")				#change as per system
mycursor=mydb.cursor()
now = datetime.datetime.now()
sql="INSERT INTO orders(orderid,orderdate,pcode,pprice,pqty,supplier,pcat) values (%s,%s,%s,%s,%s,%s,%s)"
code=int(input("Enter product code :"))
oid=now.year+now.month+now.day+now.hour+now.minute+now.second
qty=int(input("Enter product quantity : "))
price=float(input("Enter Product unit price: "))
cat=input("Enter product category: ")
supplier=input("Enter Supplier details: ")           
val=(oid,now,code,price,qty,supplier,cat)
mycursor.execute(sql,val)
mydb.commit()



deflist_order():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")					#change as per system
mycursor=mydb.cursor()
sql="SELECT * from orders"
mycursor.execute(sql)
print("\t\t\t\t\t\t\t ORDER DETAILS")
print("-"*85)
print("orderid    Date    Product code    price     quantity      Supplier      Category")
print("-"*85)
fori in mycursor:
                      print(i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t",i[4],"\t     ",i[5],"\t",i[6])
print("-"*85)


defdb_mgmt( ):
while True :
print("\t\t\t 1. Database creation")
print("\t\t\t 2. List Database")
print("\t\t\t 3. Back (Main Menu)")
                      p=int (input("\t\tEnter Your Choice :"))
if p==1 :
create_database()
if p==2 :
list_database()
if p== 3 :
break
defadd_product():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")				#change as per system
mycursor=mydb.cursor()
sql="INSERT INTO product(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
code=int(input("\t\tEnter product code :"))
search="SELECT count(*) FROM product WHERE pcode=%s;"
val=(code,)
mycursor.execute(search,val)
for x in mycursor:
cnt=x[0]
ifcnt==0:
name=input("\t\tEnter product name :")
qty=int(input("\t\tEnter product quantity :"))
price=float(input("\t\tEnter product unit price :"))
cat=input("\t\tEnter Product category :")
val=(code,name,price,qty,cat)
mycursor.execute(sql,val)
mydb.commit()
else:
print("\t\t Product already exist")
defupdate_product():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
mycursor=mydb.cursor()
code=int(input("Enter the product code :"))
qty=int(input("Enter the quantity :"))
sql="UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
val=(qty,code)
mycursor.execute(sql,val)
mydb.commit()
print("\t\t Product details updated")

defdelete_product():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
mycursor=mydb.cursor()
code=int(input("Enter the product code :"))
sql="DELETE FROM product WHERE pcode = %s;"
val=(code,)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount," record(s) deleted");
defsearch_product():

while True :
print("\t\t\t 1. List all product")
print("\t\t\t 2. List product code wise")
print("\t\t\t 3. List product categoty wise")
print("\t\t\t 4. Back (Main Menu)")
                      s=int (input("\t\tEnter Your Choice :"))
if s==1 :
list_product()
if s==2 :
code=int(input(" Enter product code :"))
list_prcode(code)

if s==3 :
cat=input("Enter category :")
list_prcat(cat)

if s== 4 :
break

deflist_product():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
mycursor=mydb.cursor()
sql="SELECT * from product"
mycursor.execute(sql)
print("\t\t\t\t PRODUCT DETAILS")
print("\t\t","-"*47)
print("\t\t code    name    price   quantity      category")
print("\t\t","-"*47)
fori in mycursor:
                      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
print("\t\t","-"*47)


deflist_prcode(code):
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
mycursor=mydb.cursor()
sql="SELECT * from product WHERE pcode=%s"
val=(code,)
mycursor.execute(sql,val)
print("\t\t\t\t PRODUCT DETAILS")
print("\t\t","-"*47)
print("\t\t code    name    price   quantity      category")
print("\t\t","-"*47)
fori in mycursor:
                      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
print("\t\t","-"*47)


defsale_product():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
mycursor=mydb.cursor()
pcode=input("Enter product code: ")
sql="SELECT count(*) from product WHERE pcode=%s;"
val=(pcode,)
mycursor.execute(sql,val)
for x in mycursor:
cnt=x[0]
ifcnt !=0 :
sql="SELECT * from product WHERE pcode=%s;"
val=(pcode,)
mycursor.execute(sql,val)
for x in mycursor:
print(x)
price=int(x[2])
pqty=int(x[3])
qty=int(input("Enter no of quantity :"))
ifqty<= pqty:
total=qty*price;
print ("Collect  Rs. ", total)
sql="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
val=(int(cnt)+1,datetime.datetime.now(),pcode,price,qty,total)
mycursor.execute(sql,val)
sql="UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
val=(qty,pcode)
mycursor.execute(sql,val)
mydb.commit()
else:
print(" Quantity not Available")
else:
print(" Product is not avalaible")

deflist_sale():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
mycursor=mydb.cursor()
sql="SELECT * FROM sales"
mycursor.execute(sql)
print(" \t\t\t\tSALES DETAILS")
print("-"*80)
print("Sales id  Date    Product Code     Price             Quantity           Total")
print("-"*80)
for x in mycursor:
                      print(x[0],"\t",x[1],"\t",x[2],"\t   ",x[3],"\t\t",x[4],"\t\t",x[5])
print("-"*80)


deflist_prcat(cat):
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
mycursor=mydb.cursor()
print (cat)
sql="SELECT * from product WHERE pcat =%s"
val=(cat,)
mycursor.execute(sql,val)
clrscr()
print("\t\t\t\t PRODUCT DETAILS")
print("\t\t","-"*47)
print("\t\t code    name    price   quantity      category")
print("\t\t","-"*47)
fori in mycursor:
                      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
print("\t\t","-"*47)

defadd_user():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
mycursor=mydb.cursor()
uid=input("Enter emaid id :")
name=input(" Enter Name :")
paswd=input("Enter Password :")
sql="INSERT INTO user values (%s,%s,%s);"
val=(uid,name,paswd)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, " user created")


deflist_user():
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="stock")
mycursor=mydb.cursor()
sql="SELECT uid,uname from user"
mycursor.execute(sql)
clrscr()
print("\t\t\t\t USER DETAILS")
print("\t\t","-"*27)
print("\t\t UID        name    ")
print("\t\t","-"*27)
fori in mycursor:
print("\t\t",i[0],"\t",i[1])
print("\t\t","-"*27)

defclrscr():
print("\n"*5)

while True:
clrscr()
print("\t\t\t STOCK MANAGEMENT")
print("\t\t\t ****************\n")
print("\t\t 1. PRODUCT MANAGEMENT")
print("\t\t 2. PURCHASE MANAGEMENT")
print("\t\t 3. SALES MANAGEMENT")
print("\t\t 4. USER MANAGEMENT")
print("\t\t 5. DATABASE SETUP")
print("\t\t 6. EXIT\n")
           n=int(input("Enter your choice :"))
if n== 1:
product_mgmt()
if n== 2:
os.system('cls')
purchase_mgmt()
if n== 3:
sales_mgmt()
if n== 4:
user_mgmt()
if n==5:
db_mgmt()
if n== 6:
break

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=============Variables======================
        #=============Cosmatics======================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #=============Grocery========================
        self.rice=IntVar()
        self.food_oil=IntVar() 
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #=============Cold Drinka====================
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        #=============Total Product Price and Tax variables====================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        #=============Customer Detail================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #=============Customer Detail================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=90,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",fg="white",bg=bg_color,font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=11,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="Phone No.",fg="white",bg=bg_color,font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=11,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        cbill_lbl=Label(F1,text="Bill Number",fg="white",bg=bg_color,font=("times new roman",14,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=11,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=50,pady=10)
        
        #=============Cosmetics Frame================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=3,y=205,width=325,height=380)
        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        face_crm_lbl=Label(F2,text="Face Cream",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_crm_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        hair_gel_lbl=Label(F2,text="Hair Gell",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gel_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        body_lbl=Label(F2,text="Body Loshan",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============Grocery Frame================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=320,y=205,width=285,height=380)
        g1_lbl=Label(F3,text="Rice",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        g3_lbl=Label(F3,text="Daal",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        g4_lbl=Label(F3,text="Wheat",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        g5_lbl=Label(F3,text="Suger",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============Cold Drink Frame================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=600,y=205,width=300,height=380)
        c1_lbl=Label(F4,text="Maza",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        c2_lbl=Label(F4,text="Cock",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        c3_lbl=Label(F4,text="Frooti",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        c4_lbl=Label(F4,text="ThumbsUp",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        c5_lbl=Label(F4,text="Limca",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        c6_lbl=Label(F4,text="Sprite",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #=============Bill Area Frame================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=905,y=205,width=440,height=350)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=============Button Frame================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=3,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=15,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=15,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=15,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=3,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=15,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=1)

        c2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=3,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=15,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=1)

        c3_lbl=Label(F6,text="Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=3,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=15,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=1)
        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=820,width=510,height=180)
        total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_spr_p=self.spray.get()*180
        self.c_g_p=self.gell.get()*140
        self.c_l_p=self.loshan.get()*180
        self.total_cosmatic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_spr_p+
                                    self.c_g_p+
                                    self.c_l_p
                                  )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmatic_price))
        self.c_tax=round(self.total_cosmatic_price*0.05,2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        self.g_r_p=self.rice.get()*80
        self.g_fo_p=self.food_oil.get()*180
        self.g_w_p=self.wheat.get()*60
        self.g_d_p=self.daal.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*150
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_fo_p+
                                    self.g_w_p+
                                    self.g_d_p+
                                    self.g_s_p+
                                    self.g_t_p
                                  )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round(self.total_grocery_price*0.1,2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        self.cd_m_p=self.maza.get()*60
        self.cd_c_p=self.cock.get()*60
        self.cd_f_p=self.frooti.get()*50
        self.cd_th_p=self.thumbsup.get()*45
        self.cd_l_p=self.limca.get()*40
        self.cd_s_p=self.sprite.get()*60
        self.total_cold_drink_price=float(
                                    self.cd_m_p+
                                    self.cd_c_p+
                                    self.cd_f_p+
                                    self.cd_th_p+
                                    self.cd_l_p+
                                    self.cd_s_p
                                   )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round(self.total_cold_drink_price*0.05,2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))
        self.total_bill=float(
            self.total_cosmatic_price+
            self.total_grocery_price+
            self.total_cold_drink_price+
            self.c_tax+
            self.g_tax+
            self.cd_tax
        )
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome KV Retail")
        self.textarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number :{self.c_phon.get()}")
        
        self.textarea.insert(END,f"\n======================================")
        self.textarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n======================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are Required")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Selected")
        else:
            self.welcome_bill()
            #===cosmatics=====
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash \t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_s_p}")
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\n Hair Gell \t\t{self.gell.get()}\t\t{self.c_g_p}")
            if self.loshan.get()!=0:
                self.textarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_l_p}")
            #===Grocery=====
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice   \t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal   \t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat  \t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Suger  \t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea   \t\t{self.tea.get()}\t\t{self.g_t_p}")
            
            #===Cold Drink=====
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza   \t\t{self.maza.get()}\t\t{self.cd_m_p}")
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n Cock   \t\t{self.cock.get()}\t\t{self.cd_c_p}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti  \t\t{self.frooti.get()}\t\t{self.cd_f_p}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.cd_th_p}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.cd_l_p}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite  \t\t{self.sprite.get()}\t\t{self.cd_s_p}")
            self.textarea.insert(END,f"\n--------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmatic Tax \t\t\t{self.cosmetic_tax.get()}")
            
            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax \t\t\t{self.grocery_tax.get()}")
                
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n ColdDrink Tax\t\t\t{self.cold_drink_tax.get()}")
            self.textarea.insert(END,f"\n Total Bill  \t\t\t Rs. {self.total_bill}")
            self.textarea.insert(END,f"\n---------------------------------------")
        self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("D:\\project\\bill_app\\invoice\\"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved successfullt")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("D:\\project\\bill_app\\invoice\\"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"D:\\project\\bill_app\\invoice\\{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")
    def clear_data(self):
        op=messagebox.askyesno("clear","Do you want to Reset Entries?")
        if op>0:
            #=============Cosmatics======================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            #=============Grocery========================
            self.rice.set(0)
            self.food_oil.set(0) 
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #=============Cold Drinka====================
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            #=============Total Product Price and Tax variables====================
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #=============Customer Detail================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()





root=Tk()
obj=Bill_App(root)

root.mainloop()
