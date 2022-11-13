
##REGISTRATION FORM
from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image,ImageTk
import mysql.connector as sq
import os
import random
import wikipedia


mysql_password=input("ENTER YOUR MYSQL ROOT USER PASSWORD:")

#utilities for project
def create_registration_table():
    con=sq.connect(host="localhost",user="root",passwd=mysql_password)
    cur=con.cursor()
    cur.execute("create database if not exists gp")
    cur.execute("use gp")
    cur.execute("create table if not exists register_table(cus_id int(5) primary key auto_increment,firstname varchar(20),lastname varchar(20),email varchar(50) unique,password varchar(20),security_question varchar(50),security_answer varchar(50))")
    con.close()
create_registration_table()    
def create_book_table():
    try:
        con=sq.connect(host="localhost",user="root",passwd=mysql_password)
        cur=con.cursor()
        cur.execute("create database if not exists gp")
        cur.execute("use gp")
        cur.execute("create table if not exists book_table(bookno int(3),bookname varchar(50) primary key)")
        cur.execute("insert into book_table values(1,'Smarter,Faster,Better')")
        cur.execute("insert into book_table values(2,'You Are a Badass')")
        cur.execute("insert into book_table values(3,'Choose Yourself')")
        cur.execute("insert into book_table values(4,'Hustle')")
        cur.execute("insert into book_table values(5,'High-Hanging Fruit')")
        cur.execute("insert into book_table values(6,'Now, Discover Your')")
        cur.execute("insert into book_table values(7,'Girl Stop Apologizing')")
        cur.execute("insert into book_table values(8,'Unfu_k Yourself')")
        cur.execute("insert into book_table values(9,'The 5 Second Rule')")
        cur.execute("insert into book_table values(10,'Tuesdays')")
        cur.execute("insert into book_table values(11,'Grit')")
        cur.execute("insert into book_table values(12,'Make Your Bed')")
        
        cur.execute("insert into book_table values(13,'Attention Revolution')")
        cur.execute("insert into book_table values(14,'Carl Sagan')")
        cur.execute("insert into book_table values(15,'Daring Greatly')")
        cur.execute("insert into book_table values(16,'Effective People')")
        cur.execute("insert into book_table values(17,'Failing Forward')")
        cur.execute("insert into book_table values(18,'Feeling Good')")
        cur.execute("insert into book_table values(19,'How to win friends')")
        cur.execute("insert into book_table values(20,'Life On Earth')")
        cur.execute("insert into book_table values(21,'Love Yourself')")
        cur.execute("insert into book_table values(22,'Mind Sight')")
        cur.execute("insert into book_table values(23,'Now')")
        cur.execute("insert into book_table values(24,'Paleo Manifesto')")
        
        cur.execute("insert into book_table values(25,'Ancient Nine')")
        cur.execute("insert into book_table values(26,'Black Flag')")
        cur.execute("insert into book_table values(27,'Gale Force')")
        cur.execute("insert into book_table values(28,'Empire Of Lies')")
        cur.execute("insert into book_table values(29,'Coastal Pursuit')")
        cur.execute("insert into book_table values(30,'Desperate Creed')")
        cur.execute("insert into book_table values(31,'Savage Son')")
        cur.execute("insert into book_table values(32,'Lee Child')")
        cur.execute("insert into book_table values(33,'Stone Cross')")
        cur.execute("insert into book_table values(34,'The White Road')")
        cur.execute("insert into book_table values(35,'Wrath')")
        
        cur.execute("insert into book_table values(36,'Adolf Hitler')")
        cur.execute("insert into book_table values(37,'Anne Frank')")
        cur.execute("insert into book_table values(38,'Mahatma Gandhi')")
        cur.execute("insert into book_table values(39,'Bob Dylan')")
        cur.execute("insert into book_table values(40,'Barack Obama')")
        cur.execute("insert into book_table values(41,'Mark Twain')")
        cur.execute("insert into book_table values(42,'Stephen King')")
        cur.execute("insert into book_table values(43,'Mandela')")
        
        cur.execute("insert into book_table values(44,'7-Minute')")
        cur.execute("insert into book_table values(45,'Fat Loss Blitz')")
        cur.execute("insert into book_table values(46,'Fittest Book')")
        cur.execute("insert into book_table values(47,'Get It Done')")
        cur.execute("insert into book_table values(48,'Get Strong')")
        cur.execute("insert into book_table values(49,'Lose Weight')")
        cur.execute("insert into book_table values(50,'Meal Plan')")
        cur.execute("insert into book_table values(51,'No Sweat')")
        cur.execute("insert into book_table values(52,'Not Diet Book')")
        cur.execute("insert into book_table values(53,'Run Fast')")
        cur.execute("insert into book_table values(54,'The Fitness Chef')")
        cur.execute("insert into book_table values(55,'The Fitness Mindset')")
        
        cur.execute("insert into book_table values(56,'Be Healthy')")
        cur.execute("insert into book_table values(57,'Food Freedom Forever')")
        cur.execute("insert into book_table values(58,'Solution')")
        cur.execute("insert into book_table values(59,'Organic')")
        cur.execute("insert into book_table values(60,'Obsessed')")
        cur.execute("insert into book_table values(61,'Nourished Kitchen')")
        cur.execute("insert into book_table values(62,'Food To Live')")
        cur.execute("insert into book_table values(63,'Paled Cooking')")
        cur.execute("insert into book_table values(64,'Primal Blueprint')")
        #
        cur.execute("insert into book_table values(65,'1984')")
        cur.execute("insert into book_table values(66,'All the Missing Girls')")
        cur.execute("insert into book_table values(67,'Bird Box')")
        cur.execute("insert into book_table values(68,'Ghost Story')")
        cur.execute("insert into book_table values(69,'Hell House')")
        cur.execute("insert into book_table values(70,'It')")
        cur.execute("insert into book_table values(71,'Penpal')")
        cur.execute("insert into book_table values(72,'Pet Sematary')")
        cur.execute("insert into book_table values(73,'Pretty Girls')")
        cur.execute("insert into book_table values(74,'The Fall of the House of Usher')")
        cur.execute("insert into book_table values(75,'The Other')")
        cur.execute("insert into book_table values(76,'The Woman in the Window')")
        
        cur.execute("insert into book_table values(77,'Gone Girl')")
        cur.execute("insert into book_table values(78,'Code')")
        cur.execute("insert into book_table values(79,'Dragon Tattoo')")
        cur.execute("insert into book_table values(80,'Big Little Lies')")
        cur.execute("insert into book_table values(81,'Rebecca')")
        cur.execute("insert into book_table values(82,'Tana French')")
        cur.execute("insert into book_table values(83,'The Day Of Jackal')")
        cur.execute("insert into book_table values(84,'The Hound')")
        cur.execute("insert into book_table values(85,'The Girl On Train')")
        cur.execute("insert into book_table values(86,'Woman In White')")
        cur.execute("insert into book_table values(87,'The Silence Of The Lambs')")
        
        cur.execute("insert into book_table values(88,'Leaves of Grass')")
        cur.execute("insert into book_table values(89,'The Anthology of Really Important Modern Poetry')")
        cur.execute("insert into book_table values(90,'Collected Poems')")
        cur.execute("insert into book_table values(91,'Where the Sidewalk Ends')")
        cur.execute("insert into book_table values(92,'View with a Grain of Sand')")
        cur.execute("insert into book_table values(93,'Paradise Lost')")
        cur.execute("insert into book_table values(94,'House of Light')")
        cur.execute("insert into book_table values(95,'American Sonnets for My Past and Future Assassin')")
        cur.execute("insert into book_table values(96,'The Poetry of Yehuda Amichai translated')")
        cur.execute("insert into book_table values(97,'the princess saves herself in this one')")
        
        cur.execute("insert into book_table values(98,'2001')")
        cur.execute("insert into book_table values(99,'A Game Of Thrones')")

        cur.execute("insert into book_table values(100,'Animal Farm')")
        cur.execute("insert into book_table values(101,'Dune')")
        cur.execute("insert into book_table values(102,'Guide To The Galaxy')")
        cur.execute("insert into book_table values(103,'Hyperion')")
        cur.execute("insert into book_table values(104,'Kindred')")
        cur.execute("insert into book_table values(105,'Lord Rings')")
        cur.execute("insert into book_table values(106,'Reday Player One')")
        cur.execute("insert into book_table values(107,'Strange Land')")
        cur.execute("insert into book_table values(108,'The Hungers Game')")
        con.commit()
        con.close()
        print("Book Table succesfully created")
    except:
        pass
        con.close()
create_book_table()
def registration_page():
    def login_page():
        def login_to_registeration():
            root2.withdraw()
            root.iconify()
            root.deiconify()
        def forget_password():
            def next_to_question():
                def next_to_nwpasswd():
                    def reset_password():
                        if passwd_fgt.get()!=conpasswd_fgt.get():
                            messagebox.showerror("ERROR!","Entered Password and Confirm Password does not match")
                        elif len(passwd_fgt.get())==0:
                            messagebox.showerror("ERROR!","Password Field is Empty")
                        else:
                            con=sq.connect(host="localhost",user="root",passwd=mysql_password)
                            cur=con.cursor()
                            cur.execute("use gp")
                            cur.execute("update register_table set password='"+passwd_fgt.get()+"' where cus_id='"+cusno_fgt.get()+"'")
                            con.commit()
                            messagebox.showinfo("SUCCESS!","Your Password is updated successfully.")
                            con.close()
                    if ans_fgt.get().upper()!=security_fgt[1].upper():
                        messagebox.showerror("ERROR!","ENTERED SECURITY ANSWER DOES NOT MATCH")
                    else:
                        question_fgt_entry.config(state="disabled")
                        reset_fgt=Frame(question_fgt,bg="white")
                        reset_fgt.place(x=0,y=80,width=400,height=300)
                        Label(reset_fgt,text="New Password:",font=("aleo",15,"bold"),bg="white").place(x=30,y=30)
                        passwd_fgt=StringVar()
                        conpasswd_fgt=StringVar()
                        Entry(reset_fgt,textvariable=passwd_fgt,font=("aleo",15,"bold"),bg='lightgray',justify="center").place(x=190,y=30,height=30,width=180)
                        Label(reset_fgt,text="Confirm Password:",font=("aleo",15,"bold"),bg="white").place(x=10,y=70)
                        Entry(reset_fgt,textvariable=conpasswd_fgt,font=("aleo",15,"bold"),bg='lightgray',justify="center").place(x=190,y=70,height=30,width=180)
                        print(passwd_fgt.get(),)
                        Button(reset_fgt,text="Reset Password",command=reset_password,cursor="hand2",font=("aleo",25,"bold"),fg="white",bg="#57106B").place(x=75,y=165,height=50,width=250)
                        
              
                con=sq.connect(host="localhost",user="root",passwd=mysql_password)
                cur=con.cursor()
                cur.execute("use gp")
                cur.execute("select security_question,security_answer from register_table where cus_id="+cusno_fgt.get())
                security_fgt=cur.fetchone()
                con.close()
                if security_fgt==None:
                    messagebox.showerror("ERROR!","Entered Customer No.does not exists\n GO BACK AND REGISTER")
                else:
                    cusno_fgt_entry.config(state="disabled")
                    question_fgt=Frame(f1_fgt,bg="white")
                    question_fgt.place(x=0,y=55,width=400,height=430)
                    Label(question_fgt,text="Question:     "+security_fgt[0],font=("aleo",15,"bold"),bg="white").place(x=10,y=0,width=400,height=40)
                    Label(question_fgt,text="Your Answer:",font=("aleo",15,"bold"),bg="white").place(x=20,y=40)
                    ans_fgt=StringVar()
                    question_fgt_entry=Entry(question_fgt,textvariable=ans_fgt,font=("aleo",15,"bold"),bg='lightgray',justify="center")
                    question_fgt_entry.place(x=175,y=40,height=30,width=210)
                    
                    Button(question_fgt,text="NEXT",command=next_to_nwpasswd,font=("aleo",15,"bold"),fg="white",bg="#57106B").place(x=140,y=95,height=30,width=100)
                    
    
                

                
            fgtpasswd=Toplevel()
            fgtpasswd.geometry("400x500")
            fgtpasswd.maxsize(400,500)
            fgtpasswd.configure(bg="white")
            fgtpasswd.iconphoto(False,icon)
            fgtpasswd.title("FORGOT PASSWORD")
            Label(fgtpasswd,text="Forgot Password",font=('Impact',25),bg="white",fg="#57106B").pack(side="top")
            f1_fgt=Frame(fgtpasswd,bg="white")
            f1_fgt.place(x=0,y=70,width=400,height=430)
            Label(f1_fgt,text="Customer No.",font=("aleo",15,"bold"),bg="white").place(x=30,y=0)
            cusno_fgt=StringVar()
            cusno_fgt_entry=Entry(f1_fgt,textvariable=cusno_fgt,font=("aleo",15,"bold"),bg='lightgray',justify="center")
            cusno_fgt_entry.place(x=190,y=0,height=30,width=180)
            Button(f1_fgt,text="NEXT",command=next_to_question,font=("aleo",15,"bold"),fg="white",bg="#57106B").place(x=140,y=60,height=30,width=100)
            
            fgtpasswd.mainloop()
        def login_data():
           def clear_login_data():
               cusno.set("")
               password.set("")
        
           #book store page
           def store_page():
               root2.withdraw()
               root3=Toplevel()
               root3.geometry("1366x768")
               root3.maxsize(1366,768)
               root3.iconphoto(False,icon)
               root3.title(200*" "+"Book Store")
               f1main=Frame(root3,bg="white")
               f1main.place(x=0,y=0,width=1366,height=750)
               def order_book():
                   a=messagebox.askyesnocancel("CONFIRM","DO YOU WANT TO BUY THIS BOOK")
                   if a==YES:
                       messagebox.showinfo("ORDERED","Dear customer your ebook is succesfully sent to your \n E-mail address :-"+cus_email)
               def store_to_login():
                root3.withdraw()
                root2.iconify()
                root2.deiconify()
               
               def search_page():
                  def search_entry():
                       global searchvar
                       searchvar=StringVar()
                       shentry=Entry(root4,textvariable=searchvar,font=("aleo",20)).place(x=10,y=10,width=200,height=50)
                  def search_button():
                       try:
                           global search_img,search_p
                           Button(root4,text="TAP TO ENTER",borderwidth=3,command=search_entry,font=("aleo",15)).place(x=10,y=10,width=200,height=50)
                           f2search=Frame(root4,bg="lavender",borderwidth=0)
                           f2search.place(x=0,y=70,width=270,height=330)
                           bname=searchvar.get()
                           if len(bname)==0:
                               Label(f2search,text="Please enter some Book name\n in the search bar",bg="lavender",fg="black",font=("aleo",14,"bold")).place(x=5,y=100)
                           else:
                               con=sq.connect(host="localhost",user="root",passwd=mysql_password)
                               cur=con.cursor()
                               cur.execute("use gp")
                               bname=searchvar.get()
                               cur.execute("select bookname from book_table where bookname like '%"+bname+"%'")

                               search_data=cur.fetchone()
                               if search_data==None:
                                   search_img=Image.open("no-result2.jpg")
                                   search_p=ImageTk.PhotoImage(search_img)
                                   Label(f2search,image=search_p).pack(side="bottom")
                               else:
                                   try:
                                       Label(f2search,text="RESULTS:-",bg="lavender",fg="black",font=("aleo",14,"bold")).place(x=20,y=0)
                                       search_f=Frame(f2search,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                                       search_f.place(x=55,y=35)
                                       search_img=Image.open(search_data[0]+".jpg")
                                       search_p=ImageTk.PhotoImage(search_img)
                                       Label(search_f,image=search_p).place(x=0,y=0,width=145,height=215)
                                       Label(search_f,text=search_data[0],font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                                       Button(search_f,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                                       con.close()
                                   except:
                                       search_img=Image.open(search_data[0]+".png")
                                       search_p=ImageTk.PhotoImage(search_img)
                                       Label(search_f,image=search_p).place(x=0,y=0,width=145,height=215)
                                       Label(search_f,text=search_data[0],font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                                       Button(search_f,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                                       con.close()
                       except:
                           messagebox.showerror("ERROR","NO SEARCH ENTRY ")
                                    
                    #search
                  
                  root4=Toplevel()
                  root4.geometry("270x400")
                  root4.maxsize(270,400)
                  root4.iconphoto(False,icon)
                  root4.title(10*" "+"SEARCH")
                  root4.configure(bg="lavender")
                  Label(root4,text="Please enter some Book name\n in the search bar",bg="lavender",fg="black",font=("aleo",14,"bold")).place(x=5,y=170) 
                  #global searchbimg,searchbuttonimg
                  searchbimg=Image.open("second search.png")
                  searchbuttonimg=ImageTk.PhotoImage(searchbimg)
                  Button(root4,text="TAP TO ENTER",command=search_entry,borderwidth=3,bg="white",font=("aleo",15)).place(x=10,y=10,width=200,height=50)
                  Button(root4,image=searchbuttonimg,command=search_button).place(x=200,y=10,width=60,height=50)
                  root4.mainloop()
              
               #global store_back
               def motivational_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)
               
                   global store_p1,store_img1,store_p2,store_img2,store_p3,store_img3,store_p4,store_img4,store_p5,store_img5,store_p6,store_img6,store_p7,store_img7,store_p8,store_img8,store_p9,store_img9,store_p10,store_img10,store_p11,store_img11,store_p12,store_img12
                   #1
                   store_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=10,y=10)  
                   store_img1=Image.open("Smarter,Faster,Better.png")
                   store_p1=ImageTk.PhotoImage(store_img1)
                   Label(store_f1,image=store_p1).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="Smarter,Faster,Better",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   #2
                   store_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=175,y=10) 
                   store_img2=Image.open("You Are a Badass.jpg")
                   store_p2=ImageTk.PhotoImage(store_img2)
                   Label(store_f1,image=store_p2).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="You Are a Badass",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                #3
                   store_f1=Frame(f3main,width=157,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=340,y=10) 
                   store_img3=Image.open("Choose Yourself.jpg")
                   store_p3=ImageTk.PhotoImage(store_img3)
                   Label(store_f1,image=store_p3).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="Choose Yourself",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                #4
                   store_f1=Frame(f3main,width=157,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=505,y=10) 
                   store_img4=Image.open("Hustle.jpg")
                   store_p4=ImageTk.PhotoImage(store_img4)
                   Label(store_f1,image=store_p4).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="Hustle",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                #5
                   store_f1=Frame(f3main,width=157,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=670,y=10) 
                   store_img5=Image.open("High-Hanging Fruit.jpg")
                   store_p5=ImageTk.PhotoImage(store_img5)
                   Label(store_f1,image=store_p5).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="High-Hanging Fruit",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                  #6
                   store_f1=Frame(f3main,width=157,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=835,y=10) 
                   store_img6=Image.open("Now, Discover Your.jpg")
                   store_p6=ImageTk.PhotoImage(store_img6)
                   Label(store_f1,image=store_p6).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="Now, Discover Your",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   #7
                   store_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=10,y=280)  
                   store_img7=Image.open("Girl Stop Apologizing.jpg")
                   store_p7=ImageTk.PhotoImage(store_img7)
                   Label(store_f1,image=store_p7).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="Girl Stop Apologizing",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                #8
                   store_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=175,y=280) 
                   store_img8=Image.open("Unfu_k Yourself.jpg")
                   store_p8=ImageTk.PhotoImage(store_img8)
                   Label(store_f1,image=store_p8).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="Unfu_k Yourself",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   #9
                   store_f1=Frame(f3main,width=157,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=340,y=280) 
                   store_img9=Image.open("The 5 Second Rule.jpg")
                   store_p9=ImageTk.PhotoImage(store_img9)
                   Label(store_f1,image=store_p9).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="The 5 Second Rule",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                #10
                   store_f1=Frame(f3main,width=157,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=505,y=280) 
                   store_img10=Image.open("Tuesdays.jpg")
                   store_p10=ImageTk.PhotoImage(store_img10)
                   Label(store_f1,image=store_p10).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="Tuesdays",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   #11
                   store_f1=Frame(f3main,width=157,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=670,y=280) 
                   store_img11=Image.open("Grit.jpg")
                   store_p11=ImageTk.PhotoImage(store_img11)
                   Label(store_f1,image=store_p11).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="Grit",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   #12
                   store_f1=Frame(f3main,width=157,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   store_f1.place(x=835,y=280) 
                   store_img12=Image.open("Make Your Bed.jpg")
                   store_p12=ImageTk.PhotoImage(store_img12)
                   Label(store_f1,image=store_p12).place(x=0,y=0,width=145,height=215)
                   Label(store_f1,text="Make Your Bed",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(store_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                  
               def self_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)


                   global self_p1,self_img1,self_p2,self_img2,self_p3,self_img3,self_p4,self_img4,self_p5,self_img5,self_p6,self_img6,self_p7,self_img7,self_p8,self_img8,self_p9,self_img9,self_p10,self_img10,self_p11,self_img11,self_p12,self_img12
                   #1
                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=10,y=10)  
                   self_img1=Image.open("Attention Revolution.jpg")
                   self_p1=ImageTk.PhotoImage(self_img1)
                   Label(self_f1,image=self_p1).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Attention Revolution",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   #2
                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=175,y=10)  
                   self_img2=Image.open("Carl Sagan.jpg")
                   self_p2=ImageTk.PhotoImage(self_img2)
                   Label(self_f1,image=self_p2).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Carl Sagan",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   #3
                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=340,y=10)  
                   self_img3=Image.open("Daring Greatly.jpg")
                   self_p3=ImageTk.PhotoImage(self_img3)
                   Label(self_f1,image=self_p3).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Daring Greatly",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   #4
                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=505,y=10)  
                   self_img4=Image.open("Effective people.jpg")
                   self_p4=ImageTk.PhotoImage(self_img4)
                   Label(self_f1,image=self_p4).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Effective people",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   #5
                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=670,y=10)  
                   self_img5=Image.open("Failing Forward.jpg")
                   self_p5=ImageTk.PhotoImage(self_img5)
                   Label(self_f1,image=self_p5).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Failing Forward",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=835,y=10)  
                   self_img6=Image.open("Feeling Good.jpg")
                   self_p6=ImageTk.PhotoImage(self_img6)
                   Label(self_f1,image=self_p6).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Feeling Good",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=10,y=280)  
                   self_img7=Image.open("How to win friends.jpg")
                   self_p7=ImageTk.PhotoImage(self_img7)
                   Label(self_f1,image=self_p7).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="How to win friends",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=175,y=280)  
                   self_img8=Image.open("Life On Earth.jpg")
                   self_p8=ImageTk.PhotoImage(self_img8)
                   Label(self_f1,image=self_p8).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Life On Earth",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=340,y=280)  
                   self_img9=Image.open("Love Yourself.jpg")
                   self_p9=ImageTk.PhotoImage(self_img9)
                   Label(self_f1,image=self_p9).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Love Yourself",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=505,y=280)  
                   self_img10=Image.open("Mind Sight.jpg")
                   self_p10=ImageTk.PhotoImage(self_img10)
                   Label(self_f1,image=self_p10).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Mind Sight",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=670,y=280)  
                   self_img11=Image.open("Now.jpg")
                   self_p11=ImageTk.PhotoImage(self_img11)
                   Label(self_f1,image=self_p11).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Now",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   self_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   self_f1.place(x=835,y=280)  
                   self_img12=Image.open("Paleo Manifesto.jpg")
                   self_p12=ImageTk.PhotoImage(self_img12)
                   Label(self_f1,image=self_p12).place(x=0,y=0,width=145,height=215)
                   Label(self_f1,text="Paleo Manifesto",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(self_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

               def fitness_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)
                   global fitness_p1,fitness_img1,fitness_p2,fitness_img2,fitness_p3,fitness_img3,fitness_p4,fitness_img4,fitness_p5,fitness_img5,fitness_p6,fitness_img6,fitness_p7,fitness_img7,fitness_p8,fitness_img8,fitness_p9,fitness_img9,fitness_p10,fitness_img10,fitness_p11,fitness_img11,fitness_p12,fitness_img12
                   #1
                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=10,y=10)  
                   fitness_img1=Image.open("No Sweat.png")
                   fitness_p1=ImageTk.PhotoImage(fitness_img1)
                   Label(fitness_f1,image=fitness_p1).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="No Sweat",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=175,y=10)  
                   fitness_img2=Image.open("The Fitness Mindset.png")
                   fitness_p2=ImageTk.PhotoImage(fitness_img2)
                   Label(fitness_f1,image=fitness_p2).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="The Fitness Mindset",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=340,y=10)  
                   fitness_img3=Image.open("7-Minute.jpg")
                   fitness_p3=ImageTk.PhotoImage(fitness_img3)
                   Label(fitness_f1,image=fitness_p3).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="7-Minute",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=505,y=10)  
                   fitness_img4=Image.open("Fat Loss Blitz.jpg")
                   fitness_p4=ImageTk.PhotoImage(fitness_img4)
                   Label(fitness_f1,image=fitness_p4).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="Fat Loss Blitz",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=670,y=10)  
                   fitness_img5=Image.open("Fittest Book.jpg")
                   fitness_p5=ImageTk.PhotoImage(fitness_img5)
                   Label(fitness_f1,image=fitness_p5).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="Fittest Book",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=835,y=10)  
                   fitness_img6=Image.open("Get It Done.jpg")
                   fitness_p6=ImageTk.PhotoImage(fitness_img6)
                   Label(fitness_f1,image=fitness_p6).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="Get It Done",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=10,y=280)  
                   fitness_img7=Image.open("Get Strong.jpg")
                   fitness_p7=ImageTk.PhotoImage(fitness_img7)
                   Label(fitness_f1,image=fitness_p7).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="Get Strong",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=175,y=280)  
                   fitness_img8=Image.open("Lose Weight.jpg")
                   fitness_p8=ImageTk.PhotoImage(fitness_img8)
                   Label(fitness_f1,image=fitness_p8).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="Lose Weight",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=340,y=280)  
                   fitness_img9=Image.open("Meal Plan.jpg")
                   fitness_p9=ImageTk.PhotoImage(fitness_img9)
                   Label(fitness_f1,image=fitness_p9).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="Meal Plan",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=505,y=280)  
                   fitness_img10=Image.open("Not Diet Book.jpg")
                   fitness_p10=ImageTk.PhotoImage(fitness_img10)
                   Label(fitness_f1,image=fitness_p10).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="Not Diet Book",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=670,y=280)  
                   fitness_img11=Image.open("Run Fast.jpg")
                   fitness_p11=ImageTk.PhotoImage(fitness_img11)
                   Label(fitness_f1,image=fitness_p11).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="Run Fast",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   fitness_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   fitness_f1.place(x=835,y=280)  
                   fitness_img12=Image.open("The Fitness chef.jpg")
                   fitness_p12=ImageTk.PhotoImage(fitness_img12)
                   Label(fitness_f1,image=fitness_p12).place(x=0,y=0,width=145,height=215)
                   Label(fitness_f1,text="The Fitness chef",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(fitness_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


               def healthy_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)
                   global healthy_p1,healthy_img1,healthy_p2,healthy_img2,healthy_p3,healthy_img3,healthy_p4,healthy_img4,healthy_p5,healthy_img5,healthy_p6,healthy_img6,healthy_p7,healthy_img7,healthy_p8,healthy_img8,healthy_p9,healthy_img9
                   healthy_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   healthy_f1.place(x=10,y=10)  
                   healthy_img1=Image.open("Food Freedom Forever.png")
                   healthy_p1=ImageTk.PhotoImage(healthy_img1)
                   Label(healthy_f1,image=healthy_p1).place(x=0,y=0,width=145,height=215)
                   Label(healthy_f1,text="Food Freedom Forever",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(healthy_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   healthy_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   healthy_f1.place(x=175,y=10)  
                   healthy_img2=Image.open("Be Healthy.jpg")
                   healthy_p2=ImageTk.PhotoImage(healthy_img2)
                   Label(healthy_f1,image=healthy_p2).place(x=0,y=0,width=145,height=215)
                   Label(healthy_f1,text="Be Healthy",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(healthy_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   healthy_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   healthy_f1.place(x=340,y=10)  
                   healthy_img3=Image.open("Food To Live.jpg")
                   healthy_p3=ImageTk.PhotoImage(healthy_img3)
                   Label(healthy_f1,image=healthy_p3).place(x=0,y=0,width=145,height=215)
                   Label(healthy_f1,text="Food To Live",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(healthy_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   healthy_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   healthy_f1.place(x=505,y=10)  
                   healthy_img4=Image.open("Nourished Kitchen.jpg")
                   healthy_p4=ImageTk.PhotoImage(healthy_img4)
                   Label(healthy_f1,image=healthy_p4).place(x=0,y=0,width=145,height=215)
                   Label(healthy_f1,text="Nourished Kitchen",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(healthy_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   healthy_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   healthy_f1.place(x=670,y=10)  
                   healthy_img5=Image.open("Obsessed.jpg")
                   healthy_p5=ImageTk.PhotoImage(healthy_img5)
                   Label(healthy_f1,image=healthy_p5).place(x=0,y=0,width=145,height=215)
                   Label(healthy_f1,text="Obsessed",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(healthy_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   healthy_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   healthy_f1.place(x=835,y=10)  
                   healthy_img6=Image.open("Organic.jpg")
                   healthy_p6=ImageTk.PhotoImage(healthy_img6)
                   Label(healthy_f1,image=healthy_p6).place(x=0,y=0,width=145,height=215)
                   Label(healthy_f1,text="Organic",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(healthy_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   healthy_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   healthy_f1.place(x=10,y=280)  
                   healthy_img7=Image.open("Paled Cooking.jpg")
                   healthy_p7=ImageTk.PhotoImage(healthy_img7)
                   Label(healthy_f1,image=healthy_p7).place(x=0,y=0,width=145,height=215)
                   Label(healthy_f1,text="Paled Cooking",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(healthy_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   healthy_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   healthy_f1.place(x=175,y=280)  
                   healthy_img8=Image.open("Primal Blueprint.jpg")
                   healthy_p8=ImageTk.PhotoImage(healthy_img8)
                   Label(healthy_f1,image=healthy_p8).place(x=0,y=0,width=145,height=215)
                   Label(healthy_f1,text="Primal Blueprint",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(healthy_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   healthy_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   healthy_f1.place(x=340,y=280)  
                   healthy_img9=Image.open("Solution.jpg")
                   healthy_p9=ImageTk.PhotoImage(healthy_img9)
                   Label(healthy_f1,image=healthy_p9).place(x=0,y=0,width=145,height=215)
                   Label(healthy_f1,text="Solution",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(healthy_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


               def auto_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)
                   global auto_p1,auto_img1,auto_p2,auto_img2,auto_p3,auto_img3,auto_p4,auto_img4,auto_p5,auto_img5,auto_p6,auto_img6,auto_p7,auto_img7,auto_p8,auto_img8
                   auto_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   auto_f1.place(x=10,y=10)  
                   auto_img1=Image.open("Adolf Hitler.jpg")
                   auto_p1=ImageTk.PhotoImage(auto_img1)
                   Label(auto_f1,image=auto_p1).place(x=0,y=0,width=145,height=215)
                   Label(auto_f1,text="Adolf Hitler",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(auto_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   auto_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   auto_f1.place(x=175,y=10)  
                   auto_img2=Image.open("Anne Frank.jpg")
                   auto_p2=ImageTk.PhotoImage(auto_img2)
                   Label(auto_f1,image=auto_p2).place(x=0,y=0,width=145,height=215)
                   Label(auto_f1,text="Anne Frank",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(auto_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   auto_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   auto_f1.place(x=340,y=10)  
                   auto_img3=Image.open("Barack Obama.jpg")
                   auto_p3=ImageTk.PhotoImage(auto_img3)
                   Label(auto_f1,image=auto_p3).place(x=0,y=0,width=145,height=215)
                   Label(auto_f1,text="Barack Obama",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(auto_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   auto_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   auto_f1.place(x=505,y=10)  
                   auto_img4=Image.open("Bob Dylan.jpg")
                   auto_p4=ImageTk.PhotoImage(auto_img4)
                   Label(auto_f1,image=auto_p4).place(x=0,y=0,width=145,height=215)
                   Label(auto_f1,text="Bob Dylan",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(auto_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   auto_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   auto_f1.place(x=670,y=10)  
                   auto_img5=Image.open("Mahatma Gandhi.jpg")
                   auto_p5=ImageTk.PhotoImage(auto_img5)
                   Label(auto_f1,image=auto_p5).place(x=0,y=0,width=145,height=215)
                   Label(auto_f1,text="Mahatma Gandhi",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(auto_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   auto_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   auto_f1.place(x=835,y=10)  
                   auto_img6=Image.open("Mandela.jpeg")
                   auto_p6=ImageTk.PhotoImage(auto_img6)
                   Label(auto_f1,image=auto_p6).place(x=0,y=0,width=145,height=215)
                   Label(auto_f1,text="Mandela",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(auto_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   auto_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   auto_f1.place(x=10,y=280)  
                   auto_img7=Image.open("Mark Twain.jpg")
                   auto_p7=ImageTk.PhotoImage(auto_img7)
                   Label(auto_f1,image=auto_p7).place(x=0,y=0,width=145,height=215)
                   Label(auto_f1,text="Mark Twain",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(auto_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)



                   auto_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   auto_f1.place(x=175,y=280)  
                   auto_img8=Image.open("Stephen King.jpg")
                   auto_p8=ImageTk.PhotoImage(auto_img8)
                   Label(auto_f1,image=auto_p8).place(x=0,y=0,width=145,height=215)
                   Label(auto_f1,text="Stephen King",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(auto_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


               def science_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)
                   global science_p1,science_img1,science_p2,science_img2,science_p3,science_img3,science_p4,science_img4,science_p5,science_img5,science_p6,science_img6,science_p7,science_img7,science_p8,science_img8,science_p9,science_img9,science_p10,science_img10,science_p11,science_img11
                   #1
                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=10,y=10)  
                   science_img1=Image.open("2001.jpg")
                   science_p1=ImageTk.PhotoImage(science_img1)
                   Label(science_f1,image=science_p1).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="2001",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=175,y=10)  
                   science_img2=Image.open("A Game Of Thrones.jpg")
                   science_p2=ImageTk.PhotoImage(science_img2)
                   Label(science_f1,image=science_p2).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="A Game Of Thrones",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=340,y=10)  
                   science_img3=Image.open("Dune.jpg")
                   science_p3=ImageTk.PhotoImage(science_img3)
                   Label(science_f1,image=science_p3).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="Dune",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=505,y=10)  
                   science_img4=Image.open("Animal Farm.jpg")
                   science_p4=ImageTk.PhotoImage(science_img4)
                   Label(science_f1,image=science_p4).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="Animal Farm",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=670,y=10)  
                   science_img5=Image.open("Hyperion.jpg")
                   science_p5=ImageTk.PhotoImage(science_img5)
                   Label(science_f1,image=science_p5).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="Hyperion",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=835,y=10)  
                   science_img6=Image.open("Guide To The Galaxy.jpg")
                   science_p6=ImageTk.PhotoImage(science_img6)
                   Label(science_f1,image=science_p6).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="Guide To The Galaxy",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=10,y=280)  
                   science_img7=Image.open("Kindred.jpg")
                   science_p7=ImageTk.PhotoImage(science_img7)
                   Label(science_f1,image=science_p7).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="Kindred",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=175,y=280)  
                   science_img8=Image.open("Lord Rings.jpg")
                   science_p8=ImageTk.PhotoImage(science_img8)
                   Label(science_f1,image=science_p8).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="Lord Rings",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=340,y=280)  
                   science_img9=Image.open("Reday Player One.jpg")
                   science_p9=ImageTk.PhotoImage(science_img9)
                   Label(science_f1,image=science_p9).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="Reday Player One",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=505,y=280)  
                   science_img10=Image.open("Strange Land.jpg")
                   science_p10=ImageTk.PhotoImage(science_img10)
                   Label(science_f1,image=science_p10).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="Strange Land",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   science_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   science_f1.place(x=670,y=280)  
                   science_img11=Image.open("The Hungers Game.jpg")
                   science_p11=ImageTk.PhotoImage(science_img11)
                   Label(science_f1,image=science_p11).place(x=0,y=0,width=145,height=215)
                   Label(science_f1,text="The Hungers Game",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(science_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

               def action_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)
                   global action_p1,action_img1,action_p2,action_img2,action_p3,action_img3,action_p4,action_img4,action_p5,action_img5,action_p6,action_img6,action_p7,action_img7,action_p8,action_img8,action_p9,action_img9,action_p10,action_img10,action_p11,action_img11
                   #1
                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=10,y=10)  
                   action_img1=Image.open("Ancient Nine.jpg")
                   action_p1=ImageTk.PhotoImage(action_img1)
                   Label(action_f1,image=action_p1).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Ancient Nine",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=175,y=10)  
                   action_img2=Image.open("Black Flag.jpg")
                   action_p2=ImageTk.PhotoImage(action_img2)
                   Label(action_f1,image=action_p2).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Black Flag",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=340,y=10)  
                   action_img3=Image.open("Desperate Creed.jpg")
                   action_p3=ImageTk.PhotoImage(action_img3)
                   Label(action_f1,image=action_p3).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Desperate Creed",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=505,y=10)  
                   action_img4=Image.open("Coastal Pursuit.jpg")
                   action_p4=ImageTk.PhotoImage(action_img4)
                   Label(action_f1,image=action_p4).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Coastal Pursuit",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=670,y=10)  
                   action_img5=Image.open("Gale Force.jpg")
                   action_p5=ImageTk.PhotoImage(action_img5)
                   Label(action_f1,image=action_p5).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Gale Force",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=835,y=10)  
                   action_img6=Image.open("Empire Of Lies.jpg")
                   action_p6=ImageTk.PhotoImage(action_img6)
                   Label(action_f1,image=action_p6).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Empire Of Lies",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=10,y=280)  
                   action_img7=Image.open("Lee Child.jpg")
                   action_p7=ImageTk.PhotoImage(action_img7)
                   Label(action_f1,image=action_p7).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Lee Child",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=175,y=280)  
                   action_img8=Image.open("Stone Cross.jpg")
                   action_p8=ImageTk.PhotoImage(action_img8)
                   Label(action_f1,image=action_p8).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Stone Cross.jpg",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=340,y=280)  
                   action_img9=Image.open("Wrath.jpg")
                   action_p9=ImageTk.PhotoImage(action_img9)
                   Label(action_f1,image=action_p9).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Wrath",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=505,y=280)  
                   action_img10=Image.open("The White Road.jpg")
                   action_p10=ImageTk.PhotoImage(action_img10)
                   Label(action_f1,image=action_p10).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="The White Road.jpg",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   action_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   action_f1.place(x=670,y=280)  
                   action_img11=Image.open("Savage Son.jpg")
                   action_p11=ImageTk.PhotoImage(action_img11)
                   Label(action_f1,image=action_p11).place(x=0,y=0,width=145,height=215)
                   Label(action_f1,text="Savage Son",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(action_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

               def mystery_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)
                   global mystery_p1,mystery_img1,mystery_p2,mystery_img2,mystery_p3,mystery_img3,mystery_p4,mystery_img4,mystery_p5,mystery_img5,mystery_p6,mystery_img6,mystery_p7,mystery_img7,mystery_p8,mystery_img8,mystery_p9,mystery_img9,mystery_p10,mystery_img10,mystery_p11,mystery_img11
                   #1
                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=10,y=10)  
                   mystery_img1=Image.open("Rebecca.jpg")
                   mystery_p1=ImageTk.PhotoImage(mystery_img1)
                   Label(mystery_f1,image=mystery_p1).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="Rebecca",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=175,y=10)  
                   mystery_img2=Image.open("Dragon Tattoo.jpg")
                   mystery_p2=ImageTk.PhotoImage(mystery_img2)
                   Label(mystery_f1,image=mystery_p2).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="Dragon Tattoo",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=340,y=10)  
                   mystery_img3=Image.open("Code.jpg")
                   mystery_p3=ImageTk.PhotoImage(mystery_img3)
                   Label(mystery_f1,image=mystery_p3).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="Code",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=505,y=10)  
                   mystery_img4=Image.open("Big Little Lies.jpg")
                   mystery_p4=ImageTk.PhotoImage(mystery_img4)
                   Label(mystery_f1,image=mystery_p4).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="Big Little Lies",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)



                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=670,y=10)  
                   mystery_img5=Image.open("Gone Girl.jpg")
                   mystery_p5=ImageTk.PhotoImage(mystery_img5)
                   Label(mystery_f1,image=mystery_p5).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="Gone Girls",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=835,y=10)  
                   mystery_img6=Image.open("Tana French.jpg")
                   mystery_p6=ImageTk.PhotoImage(mystery_img6)
                   Label(mystery_f1,image=mystery_p6).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="Tana French",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=10,y=280)  
                   mystery_img7=Image.open("The Day Of Jackal.jpg")
                   mystery_p7=ImageTk.PhotoImage(mystery_img7)
                   Label(mystery_f1,image=mystery_p7).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="The Day Of Jackal",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=175,y=280)  
                   mystery_img8=Image.open("The Girl On Train.jpg")
                   mystery_p8=ImageTk.PhotoImage(mystery_img8)
                   Label(mystery_f1,image=mystery_p8).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="The Girl On Train",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=340,y=280)  
                   mystery_img9=Image.open("Woman In White.jpg")
                   mystery_p9=ImageTk.PhotoImage(mystery_img9)
                   Label(mystery_f1,image=mystery_p9).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="Woman In White",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=505,y=280)  
                   mystery_img10=Image.open("The Hound.jpg")
                   mystery_p10=ImageTk.PhotoImage(mystery_img10)
                   Label(mystery_f1,image=mystery_p10).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="The Hound",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)


                   mystery_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   mystery_f1.place(x=670,y=280)  
                   mystery_img11=Image.open("The Silence Of The Lambs.jpg")
                   mystery_p11=ImageTk.PhotoImage(mystery_img11)
                   Label(mystery_f1,image=mystery_p11).place(x=0,y=0,width=145,height=215)
                   Label(mystery_f1,text="The Silence Of The Lambs",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(mystery_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

               def horror_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)
                   global horror_p1,horror_img1,horror_p2,horror_img2,horror_p3,horror_img3,horror_p4,horror_img4,horror_p5,horror_img5,horror_p6,horror_img6,horror_p7,horror_img7,horror_p8,horror_img8,horror_p9,horror_img9,horror_p10,horror_img10,horror_p11,horror_img11,horror_p12,horror_img12
                   #1
                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=10,y=10)  
                   horror_img1=Image.open("1984.jpg")
                   horror_p1=ImageTk.PhotoImage(horror_img1)
                   Label(horror_f1,image=horror_p1).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="1984",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=175,y=10)  
                   horror_img2=Image.open("All the Missing Girls.jpg")
                   horror_p2=ImageTk.PhotoImage(horror_img2)
                   Label(horror_f1,image=horror_p2).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="All the Missing Girls",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=340,y=10)  
                   horror_img3=Image.open("Bird Box.jpg")
                   horror_p3=ImageTk.PhotoImage(horror_img3)
                   Label(horror_f1,image=horror_p3).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="Bird Box",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=505,y=10)  
                   horror_img4=Image.open("Ghost Story.jpg")
                   horror_p4=ImageTk.PhotoImage(horror_img4)
                   Label(horror_f1,image=horror_p4).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="Ghost Story",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=670,y=10)  
                   horror_img5=Image.open("Hell House.jpg")
                   horror_p5=ImageTk.PhotoImage(horror_img5)
                   Label(horror_f1,image=horror_p5).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="Hell House",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=835,y=10)  
                   horror_img6=Image.open("It.jpg")
                   horror_p6=ImageTk.PhotoImage(horror_img6)
                   Label(horror_f1,image=horror_p6).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="It",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=10,y=280)  
                   horror_img7=Image.open("Penpal.jpg")
                   horror_p7=ImageTk.PhotoImage(horror_img7)
                   Label(horror_f1,image=horror_p7).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="Penpal",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=175,y=280)  
                   horror_img8=Image.open("Pet Sematary.jpg")
                   horror_p8=ImageTk.PhotoImage(horror_img8)
                   Label(horror_f1,image=horror_p8).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="Pet Sematary",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=340,y=280)  
                   horror_img9=Image.open("The Fall of the House of Usher.jpg")
                   horror_p9=ImageTk.PhotoImage(horror_img9)
                   Label(horror_f1,image=horror_p9).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="The Fall of the House of Usher",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=505,y=280)  
                   horror_img10=Image.open("Pretty Girls.jpg")
                   horror_p10=ImageTk.PhotoImage(horror_img10)
                   Label(horror_f1,image=horror_p10).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="Pretty Girls",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=670,y=280)  
                   horror_img11=Image.open("Woman In White.jpg")
                   horror_p11=ImageTk.PhotoImage(horror_img11)
                   Label(horror_f1,image=horror_p11).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="Woman In White",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   horror_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   horror_f1.place(x=835,y=280)  
                   horror_img12=Image.open("The Silence Of The Lambs.jpg")
                   horror_p12=ImageTk.PhotoImage(horror_img12)
                   Label(horror_f1,image=horror_p12).place(x=0,y=0,width=145,height=215)
                   Label(horror_f1,text="The Silence Of The Lambs",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(horror_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   
               def poetry_books():
                   global store_back
                   f3main=Frame(root3,bg="white",borderwidth=0)
                   f3main.place(x=280,y=140,width=1050,height=560)
                   store_back=PhotoImage(file="arrow for 3rd page.png")
                   Button(f3main,image=store_back,command=quote_page,cursor="hand2",bd=0,bg="white").pack(anchor="ne",pady=10)
                   global poetry_p1,poetry_img1,poetry_p2,poetry_img2,poetry_p3,poetry_img3,poetry_p4,poetry_img4,poetry_p5,poetry_img5,poetry_p6,poetry_img6,poetry_p7,poetry_img7,poetry_p8,poetry_img8,poetry_p9,poetry_img9,poetry_p10,poetry_img10
                   #1
                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=10,y=10)  
                   poetry_img1=Image.open("Leaves of Grass.jpg")
                   poetry_p1=ImageTk.PhotoImage(poetry_img1)
                   Label(poetry_f1,image=poetry_p1).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="Leaves of Grass",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=175,y=10)  
                   poetry_img2=Image.open("The Anthology of Really Important Modern Poetry.jpg")
                   poetry_p2=ImageTk.PhotoImage(poetry_img2)
                   Label(poetry_f1,image=poetry_p2).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="The Anthology of Really Important Modern Poetry",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=340,y=10)  
                   poetry_img3=Image.open("Collected Poems.jpg")
                   poetry_p3=ImageTk.PhotoImage(poetry_img3)
                   Label(poetry_f1,image=poetry_p3).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="Collected Poems",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=505,y=10)  
                   poetry_img4=Image.open("Where the Sidewalk Ends.png")
                   poetry_p4=ImageTk.PhotoImage(poetry_img4)
                   Label(poetry_f1,image=poetry_p4).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="Where the Sidewalk Ends",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=670,y=10)  
                   poetry_img5=Image.open("View with a Grain of Sand.jpg")
                   poetry_p5=ImageTk.PhotoImage(poetry_img5)
                   Label(poetry_f1,image=poetry_p5).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="View with a Grain of Sand",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=835,y=10)  
                   poetry_img6=Image.open("Paradise Lost.jpg")
                   poetry_p6=ImageTk.PhotoImage(poetry_img6)
                   Label(poetry_f1,image=poetry_p6).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="Paradise Lost",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=10,y=280)  
                   poetry_img7=Image.open("House of Light.jpg")
                   poetry_p7=ImageTk.PhotoImage(poetry_img7)
                   Label(poetry_f1,image=poetry_p7).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="House of Light",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=175,y=280)  
                   poetry_img8=Image.open("American Sonnets for My Past and Future Assassin.jpg")
                   poetry_p8=ImageTk.PhotoImage(poetry_img8)
                   Label(poetry_f1,image=poetry_p8).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="American Sonnets for My Past and Future Assassin",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=340,y=280)  
                   poetry_img9=Image.open("The Poetry of Yehuda Amichai translated.jpg")
                   poetry_p9=ImageTk.PhotoImage(poetry_img9)
                   Label(poetry_f1,image=poetry_p9).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="The Poetry of Yehuda Amichai translated",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)

                   poetry_f1=Frame(f3main,width=155,height=265,borderwidth=5,relief="groove",bg="#57106B")
                   poetry_f1.place(x=505,y=280)  
                   poetry_img10=Image.open("the princess saves herself in this one.jpg")
                   poetry_p10=ImageTk.PhotoImage(poetry_img10)
                   Label(poetry_f1,image=poetry_p10).place(x=0,y=0,width=145,height=215)
                   Label(poetry_f1,text="the princess saves herself in this one",font=("alegreya medium",11),bg="#57106B",fg="white").place(x=0,y=215,width=145,height=20)
                   Button(poetry_f1,text="Price=₹"+str(random.randint(200,300))+"   ☑",command=order_book,font=("alegreya medium",12),cursor="hand2",bg="#57106B",fg="white").place(x=0,y=235,width=145,height=22)
                   
                   
               
               #apna logo
               main_p1=PhotoImage(file="bookshelves logo in pp colour.png")
               Label(f1main,image=main_p1).place(x=0,y=20,width=300,height=99)
               #frame for catagories
               f2main=Frame(root3)
               f2main.place(x=20,y=150,width=250,height=550)
               catagory_photo=PhotoImage(file="CATEGORIESBUTTON.png")
               Label(f2main,image=catagory_photo,font=("times new roman",20,"bold"),borderwidth=5,relief="sunken",bg="black",fg="white").place(x=0,y=0,width=250,height=50)

               Button(f2main,text="Poetry",command=poetry_books,font=("times new roman",20,"bold"),borderwidth=5,cursor="hand2",relief="raised",bg="white",fg="black").place(x=0,y=50,width=250,height=50)
               Button(f2main,text="Horror",command=horror_books,font=("times new roman",20,"bold"),borderwidth=5,cursor="hand2",relief="raised",bg="white",fg="black").place(x=0,y=100,width=250,height=50)
               Button(f2main,text="Fitness",command=fitness_books,font=("times new roman",20,"bold"),borderwidth=5,cursor="hand2",relief="raised",bg="white",fg="black").place(x=0,y=150,width=250,height=50)
               Button(f2main,text="Mystery",command=mystery_books,font=("times new roman",20,"bold"),borderwidth=5,cursor="hand2",relief="raised",bg="white",fg="black").place(x=0,y=200,width=250,height=50)
               Button(f2main,text="Motivational",command=lambda :[motivational_books()],font=("times new roman",20,"bold"),cursor="hand2",borderwidth=5,relief="raised",bg="white",fg="black").place(x=0,y=250,width=250,height=50)
               Button(f2main,text="Healthy Eating",command=healthy_books,font=("times new roman",20,"bold"),borderwidth=5,cursor="hand2",relief="raised",bg="white",fg="black").place(x=0,y=300,width=250,height=50)
               Button(f2main,text="Science Fiction",command=science_books,font=("times new roman",20,"bold"),borderwidth=5,cursor="hand2",relief="raised",bg="white",fg="black").place(x=0,y=350,width=250,height=50)
               Button(f2main,text="AutoBiographies",command=auto_books,font=("times new roman",20,"bold"),borderwidth=5,cursor="hand2",relief="raised",bg="white",fg="black").place(x=0,y=400,width=250,height=50)
               Button(f2main,text="Self Improvement",command=self_books,font=("times new roman",20,"bold"),cursor="hand2",borderwidth=5,relief="raised",bg="white",fg="black").place(x=0,y=450,width=250,height=50)
               Button(f2main,text="Action & Adventure",command=action_books,font=("times new roman",20,"bold"),borderwidth=5,cursor="hand2",relief="raised",bg="white",fg="black").place(x=0,y=500,width=250,height=50)
               #Quotes frame
               f4main=Frame(root3,bg="white",borderwidth=0)
               f4main.place(x=280,y=150,width=1050,height=550)
               def quote_page():
                   f4main=Frame(root3,bg="white",bd=5,relief="groove")
                   f4main.place(x=280,y=150,width=1050,height=550)
                   def myfunction(event):
                       canvas.configure(scrollregion=canvas.bbox("all"),width=1050,height=550)
                   canvas=Canvas(f4main,bg="white")
                   frame=Frame(canvas,bg="white")
                   myscrollbar=Scrollbar(f4main,orient="vertical",command=canvas.yview)
                   canvas.configure(yscrollcommand=myscrollbar.set)

                   myscrollbar.pack(side="right",fill="y")
                   canvas.pack(side="left")
                   canvas.create_window((0,0),window=frame,anchor='nw')
                   frame.bind("<Configure>",myfunction)
                   quote_frame1=Frame(frame,width=1050,height=150,bg="white")
                   quote_frame1.pack(side="top")
                   global quote_img
                   quote_img=PhotoImage(file="quote frame .png")
                   Label(quote_frame1,image=quote_img,width=1030,height=150).place(x=0,y=0)
                   quote_frame2=Frame(frame,width=1030,bd=2,bg="white")
                   quote_frame2.pack(side="top",padx=10)
                   Label(quote_frame2,text="“A great book should leave you with many experiences, and slightly exhausted at the end. You live several lives while reading.”\n"+80*"  " +"– William Styron\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“I love books. I adore everything about them. I love the feel of the pages on my fingertips. They are light enough to carry,\n yet so heavy with worlds and ideas. I love the sound of the pages flicking against my fingers.\n Print against fingerprints. Books make people quiet, yet they are so loud.”\n"+80*"  " +" – Nnedi Okorafor\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top")
                   Label(quote_frame2,text="“If you would tell me the heart of a man, tell me not what he reads, but what he rereads.”\n"+80*"  " +"– Francois Mauriac\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“For some of us, books are as important as almost anything else on earth. What a miracle it is that out of these small, flat,\n rigid squares of paper unfolds world after world after world, worlds that sing to you, comfort and quiet or excite you.\n Books help us understand who we are and how we are to behave. They show us what community and friendship mean;\n they show us how to live and die.”\n"+80*"  " +"– Anne Lamott\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“In the case of good books, the point is not to see how many of them you can get through,\n but rather how many can get through to you.”\n"+80*"  " +"– Mortimer J. Adler\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“I guess there are never enough books.”\n"+80*"  " +"– John Steinbeck\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“A good bookshop is just a genteel Black Hole that knows how to read.”\n"+80*"  " +"– Terry Pratchett\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Of course anyone who truly loves books buys more of them than he or she can hope to read in one fleeting lifetime.\n A good book, resting unopened in its slot on a shelf, full of majestic potentiality, is most comforting sort of intellectual wallpaper.”\n"+80*"  " +"– David Quammen\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“You know you’ve read a good book when you turn the last page and feel a little as if you have lost a friend.”\n"+80*"  " +"– Paul Sweeney\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Libraries will get you through times of no money better than money will get you through times of no libraries.”\n"+80*"  " +"– Toni Morrison\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Libraries will get you through times of no money better than money will get you through times of no libraries.”\n"+80*"  " +"– Anne Herbert\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Happiness. That’s what books smells like. Happiness. That’s why I always wanted to have a book shop.\n What better life than to trade in happiness?”\n"+80*"  " +"– Saran MacLean\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="Books should go where they will be most appreciated, and not sit unread, gathering dust on a forgotten shelf, don’t you agree?”\n"+80*"  " +"– Christopher Paolini\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Reading is an exercise in empathy; an exercise in walking in someone else’s shoes for a while.”\n"+80*"  " +"– Malorie Blackman\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“We read in bed because reading is halfway between life and dreaming, our own consciousness in someone else’s mind.”\n"+80*"  " +"– Anna Quindlen\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Show me a family of readers, and I will show you the people who move the world.”\n"+80*"  " +"– Napoleon Bonaparte\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Read the best books first, or you may not have a chance to read them at all.”\n"+80*"  " +"– Henry David Thoreau\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Reading is to the mind what exercise is to the body.”\n"+80*"  " +"– Joseph Addison\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Until I feared I would lose it, I never loved to read. One does not love breathing.”\n"+80*"  " +"– Harper Lee\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Reading is an act of civilization; it’s one of the greatest acts of civilization because it takes the free raw material\n of the mind and builds castles of possibilities.”\n"+80*"  " +"– Ben Okri\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“If you only read the books that everyone else is reading, you can only think what everyone else is thinking.”\n"+80*"  " +"– Haruki Murakami\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“The unread story is not a story; it is little black marks on wood pulp. The reader, reading it, makes it live: a live thing, a story.”\n"+80*"  " +"– Ursula K. LeGuin\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“I have a passion for teaching kids to become readers, to become comfortable with a book, not daunted.\n Books shouldn’t be daunting, they should be funny, exciting and wonderful;\n and learning to be a reader gives a terrific advantage.”\n"+80*"  " +"– Roald Dahl\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Reading should not be presented to children as a chore, a duty. It should be offered as a gift.”\n"+80*"  " +"– Kate DiCamillo\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Reading is a form of prayer, a guided meditation that briefly makes us believe we’re someone else, \ndisrupting the delusion that we’re permanent and at the center of the universe.\n Suddenly (we’re saved!) other people are real again, and we’re fond of them.”\n"+80*"  " +"– George Saunders\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Reading—even browsing—an old book can yield sustenance denied by a database search.”\n"+80*"  " +"– James Gleick\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“I am reading six books at once, the only way of reading; since, as you will agree, one book is only a single unaccompanied note,\n and to get the full sound, one needs ten others at the same time.”\n"+80*"  " +"– Virginia Woolf\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“Read. Read. Read. Just don’t read one type of book. Read different books by various authors so that you develop different style.”\n"+80*"  " +"– R.L. Stine\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
                   Label(quote_frame2,text="“It wasn’t until I started reading and found books they wouldn’t let us read in school\n that I discovered you could be insane and happy and have a good life without being like everybody else.”\n"+80*"  " +"– John Waters\n"+"_____________________________________",font=("aleo",13,"bold"),bg="white").pack(side="top",pady=20)
               quote_page()
               def wiki_page():
                   
                   wikiwin = Toplevel(f1main)
                   wikiwin.geometry("600x600+400+60")
                   wikiwin.title("PERSONAL WIKIPEDIA")
                   wikiwin.configure(bg="white")
                   wikiwin.iconphoto(False,icon)
                   try:
                        # wiki entry
                       wikimess = Label(wikiwin, text="PERSONAL  WIKIPEDIA",fg="#57106B",bg="white",font=("aleo", 25, "bold")).place(x=100, y=10)
                       fwikisearvalue = StringVar()
                       fwikisear = Entry(wikiwin, font=("aleo", 17), bg="white",fg="black",justify=CENTER, textvariable=fwikisearvalue)
                       fwikisear.place(x=214, y=90, height=25, width=175)

                       # scrollbar
                       scrollbar2 = Scrollbar(wikiwin)
                       scrollbar2.pack(side=RIGHT, fill=Y)
                       # textbox
                       getdoc = Text(wikiwin, bg="#D253F6", yscrollcommand=scrollbar2.set, font=("alegreya medium",13),relief="groove", wrap=WORD)
                       getdoc.place(x=5, y=200, height=395, width=575)
                       scrollbar2.config(command=lambda: [getdoc.yview()])
                       def clear4():
                            getdoc.delete(1.0, END)
                       def wikifetch():
                            try:
                                doc_value = fwikisearvalue.get()
                                getdoc_value = wikipedia.summary(doc_value)
                                getdoc.insert(INSERT, getdoc_value)
                            except:
                                messagebox.showerror("Error", "No Result found / Kindly check your Internet connection", parent=f1main)
                        # wikisear btn
                       
                       searchbtn1 = Button(wikiwin, text="SEARCH",font=("aleo",15,"bold"),fg="white",bg="#57106B", cursor="hand2",command=lambda: [clear4(),wikifetch()])
                       searchbtn1.place(x=250, y=120,width=100,height=40)

                       wikiwin.mainloop()
                   except:
                       messagebox.showerror("Error", "Kindly check your Internet connection", parent=f1main)





                   
               #buttons of store
               search_store=Image.open("go to search page icon1.png")
               search_store_img=ImageTk.PhotoImage(search_store)
               Button(f1main,image=search_store_img,command=search_page,cursor="hand2",bd=0).place(x=600,y=10,width=200,height=116)
               
               wiki_store=PhotoImage(file="Wikipedia-logo-v2.png")
               Label(f1main,text="Want to Use Your \nPersonal Wikipedia?",bg="white",fg="black",font=("aleo",14,"bold")).place(x=880,y=5)
               Button(f1main,image=wiki_store,command=wiki_page,cursor="hand2",bd=0,bg="white").place(x=940,y=60,width=70,height=63)

               Label(f1main,text="Welcome, "+cus_name,bg="white",fg="black",font=("aleo",14,"bold")).place(x=1150,y=0)
               Label(f1main,text=cus_email,bg="white",fg="black",font=("aleo",10,"bold")).place(x=1150,y=25)
               #logout image
               logout_img=PhotoImage(file="LOG OUT.png")
               Button(f1main,image=logout_img,command=store_to_login,cursor="hand2",borderwidth=0,bg="white").place(x=1140,y=60,width=210,height=42)
               root3.mainloop()
        
 
           if password.get()=='' or cusno.get()=='':
                messagebox.showerror('ERROR!','Please fill required details!')
           else:
               con=sq.connect(host="localhost",user="root",passwd=mysql_password)
               if not con.is_connected:
                   messagebox.showerror('ERROR!',"connection failed")
               else:
                   try:                       
                       cur=con.cursor()
                       cur.execute("use gp")
                       cur.execute("select cus_id,password from register_table")
                       count1=0
                       for i in cur.fetchall():
                           if cusnoentry.get()==str(i[0]) and password.get()==i[1]:
                               count1+=1
                    
                       if count1>0:       
                           cur.execute('select firstname,email from register_table where cus_id='+cusnoentry.get())
                           (cus_name,cus_email)=cur.fetchone()
                           messagebox.showinfo("SUCCESS","'"+cus_name+"',you have Logon succesfully\n Press 'OK' Button")
                           clear_login_data()
                           store_page()
                           con.close()
                       else:
                           messagebox.showerror('ERROR!',"Invalid Customer No. or Password")
                           clear_login_data()
                           con.close()
                    
                   except Exception as es:
                       messagebox.showerror('ERROR!',"Error due to"+str(es))
                       con.close()
        #login page
        root.withdraw()
        root2=Toplevel()
        root2.geometry("1366x768")          #1cm=38uts of pc
        outerloginframe=Frame(root2,bg="black",borderwidth=0)        
        outerloginframe.place(x=0,y=0,width=1366,height=768)
        p1=PhotoImage(file="2nd page collage.png")
        Label(outerloginframe,image=p1).place(x=0,y=0,width=1366,height=768)
        p2=PhotoImage(file="SHORT LOGO.png")
        root2.iconphoto(False,icon)
        root2.title(200*" "+"LOGIN")
                    
        framelogin=Frame(root2,bg='white')
        framelogin.place(x=160,y=200,height=360,width=550)
        Label(framelogin,image=p2,borderwidth=0).pack(anchor="ne")
        title1=Label(framelogin,text='Login Here',font=('Impact',35,'bold'),fg='#57106B',bg='white').place(x=90,y=30)
        title2=Label(framelogin,text='Enter your details please.',font=('times new roman',15,'bold'),fg='#57106B',bg='white').place(x=90,y=100)
        title3=Label(framelogin,text='Customer No.',font=('times new roman',15,'bold'),fg='black',bg='white').place(x=90,y=150)
        title3=Label(framelogin,text='Password',font=('times new roman',15,'bold'),fg='black',bg='white').place(x=90,y=230)
        cusno=StringVar()
        password=StringVar()
        cusnoentry=Entry(framelogin,textvariable=cusno,font=('times new roman',16),bg='lightgray')
        cusnoentry.place(x=90,y=180,width=300,height=35)
        passwordentry=Entry(framelogin,textvariable=password,font=('times new roman',16),bg='lightgray')
        passwordentry.place(x=90,y=260,width=300,height=35)
        Button(framelogin,text='Forget Password? Click here',command=forget_password,bd=0,bg='white',fg='#57106B',font=('time new roman',12)).place(x=90,y=300)
        Button(root2,text='Login',font=("times new roman",19,"bold"),command=login_data,cursor='hand2',fg='white',bg='#57106B').place(x=350,y=535,width=150,height=45)
        #back button
        back_img=Image.open("back button2.png")
        back_photo=ImageTk.PhotoImage(back_img)
        
        Button(root2,image=back_photo,command=login_to_registeration,cursor='hand2').place(x=1160,y=0,width=200,height=40)
        
        root2.mainloop()
        
    def clear_reg_data():
        fname.set('')
        lname.set('')
        email.set('')
        password1.set('')
        conpassword1.set('')
        sec2.set('')
        ckvar.set('')
        sec1.current(0)
        

    def register_data():
        messagebox.askquestion("CONFIRM","DO YOU WISH TO PROCEED")
        if fname.get()=='' or lname.get()=='' or email.get()=='' or password1.get()=='' or sec1.get()=='SELECT' or sec2.get()=='':
            messagebox.showerror('ERROR!','PLEASE FILL ALL THE FIELDS')
        elif password1.get()!=conpassword1.get():
            messagebox.showerror('ERROR!','ENTERED PASSWORD DOES NOT MATCH!')           #doubt why parent=obj
        elif ckvar.get()==0:
            messagebox.showerror('ERROR!','Please verify the details and click the check box.')
        elif '@gmail.com' not in email.get():
            messagebox.showerror('ERROR!','Please enter a valid email id')
        else:            
            con=sq.connect(host="localhost",user="root",passwd=mysql_password)
            if not con.is_connected:
                messagebox.showerror('ERROR!',"connection failed")
            else:
                try:
                    cur=con.cursor()
                    cur.execute("use gp")
                    cur.execute("INSERT INTO register_table(FIRSTNAME,LASTNAME,EMAIL,PASSWORD,SECURITY_QUESTION,SECURITY_ANSWER) VALUES('"+fname.get()+"','"+lname.get()+"','"+email.get()+"','"+password1.get()+"','"+sec1.get()+"','"+sec2.get()+"')")
                    con.commit()
                    cur.execute("select *from register_table where email='"+email.get()+"'")
                    genid=str(cur.fetchone()[0])
                    messagebox.showinfo("REGISTERED!","DEAR CUSTOMER YOU HAD REGISTERED SUCCESSFULLY! \nYOUR GENERATED CUSTOMER NUMBER IS:-"+genid)
                    con.close()
                    clear_reg_data()   
                except:
                    
                    messagebox.showerror('ERROR!','ENTERED EMAIL ALLREAGY EXISTS OR CHECK YOUR CONNECTION')
                    con.close()
     #register            
    root=Tk()
    root.geometry("1366x750")
    root.maxsize(1366,750)
    icon=PhotoImage(file="SHORT LOGO.png")
    root.iconphoto(False,icon)
    root.title(200*" "+"REGISTERATION")

        #frame
    f2=Frame(root,bg="white")
    f2.place(x=0,y=0,width=1366,height=720)
    img1=Image.open("1 attempt.png")
    p1=ImageTk.PhotoImage(img1)
    l1=Label(f2,image=p1)
    l1.place(x=0,y=0,width=1366,height=720)
    
        #frame
    f1=Frame(root,bg="white",bd=3)
    f1.place(x=440,y=0,width=466,height=710)
        #logo image
    p2=PhotoImage(file="bookshelves logo in pp colour.png")
    Label(f1,image=p2,borderwidth=0).place(x=80,y=20)
        #registration image
    l2=Label(f1,text="create account",font=("permanent marker",35, "bold"),fg="#57106B",bg="white")
    l2.place(x=50,y=150)

        #Label and entry
    l3=Label(f1,text="First Name",font=("aleo",11,"bold"),bg="white",fg="black")
    l3.place(x=40,y=250)
    fname=StringVar()                    #gap between label and label entry is 25
    fnameentry=Entry(f1,textvariable=fname,bg="lightgray",fg="black",font="alegreya 14",borderwidth=3,relief="sunken")
    fnameentry.place(x=40,y=275,width=170)                                         #gapbetween label1 entry and label2 is 50

    l3=Label(f1,text="Last Name",font=("aleo",11,"bold"),bg="white",fg="black")
    l3.place(x=250,y=250)
    lname=StringVar()    
    lnameentry=Entry(f1,textvariable=lname,bg="lightgray",fg="black",font="alegreya 14",borderwidth=3,relief="sunken")
    lnameentry.place(x=250,y=275,width=170)

    l4=Label(f1,text="Email ID",font=("aleo",11,"bold"),bg="white",fg="black")
    l4.place(x=40,y=325)
    email=StringVar()
    emailentry=Entry(f1,textvariable=email,bg="lightgray",fg="black",font="alegreya 14",borderwidth=3,relief="sunken")
    emailentry.place(x=40,y=350,width=300)

    l5=Label(f1,text="Password",font=("aleo",11,"bold"),bg="white",fg="black")
    l5.place(x=40,y=400)
    password1=StringVar()
    passentry=Entry(f1,textvariable=password1,bg="lightgray",fg="black",font="alegreya 14",borderwidth=3,relief="sunken")
    passentry.place(x=40,y=425,width=170)

    l6=Label(f1,text="Confirm Password",font=("aleo",11,"bold"),bg="white",fg="black")
    l6.place(x=250,y=400)
    conpassword1=StringVar()
    conpassentry=Entry(f1,textvariable=conpassword1,bg="lightgray",fg="black",font="alegreya 14",borderwidth=3,relief="sunken")
    conpassentry.place(x=250,y=425,width=170)

    ls1=Label(f1,text="Security Question",font=("aleo",11,"bold"),bg="white",fg="black")
    ls1.place(x=40,y=475)
    ls1=Label(f1,text="Empty",borderwidth=3,relief="groove")
    ls1.place(x=40,y=500,width=180,height=30)
    sec1=ttk.Combobox(f1,font=("aleo",11,"bold"),state='readonly')
    sec1['values']=('SELECT','Your favourite author','Your nick name','Your favourite footballer','Your Birthplace','Your favourite subject')
    sec1.place(x=43,y=503,width=174,height=24)
    sec1.current(0)

    ls2=Label(f1,text="Security Answer",font=("aleo",11,"bold"),bg="white",fg="black")
    ls2.place(x=250,y=475)
    sec2=StringVar()
    sec2entry=Entry(f1,textvariable=sec2,bg="lightgray",fg="black",font="alegreya 14",borderwidth=3,relief="sunken")
    sec2entry.place(x=250,y=500,width=170)

    ckvar=IntVar()
    ckbutton=Checkbutton(f1,text="I agree to the Terms and Conditions",variable=ckvar)
    ckbutton.place(x=45,y=560)
    l7=Label(f1,text="I agree to the Terms and Conditions",font=("aleo",12,"bold"),bg="white",fg="black")
    l7.place(x=66,y=560,width=260,height=30)
        
    img2=Image.open("REGISTER NOW BUTTON.png")
    p3=ImageTk.PhotoImage(img2)
    registorbutton=Button(f1,image=p3,command=register_data,cursor="hand2",borderwidth=0,bg="white")
    registorbutton.place(x=50,y=610)

    l8=Label(f1,text="OR",font=("aleo",15,"bold"),bg="white",fg="black")
    l8.place(x=210,y=620)
    img3=Image.open("login button.png")
    p4=ImageTk.PhotoImage(img3)
    registorbutton=Button(f1,image=p4,command=login_page,cursor="hand2",borderwidth=0,bg="white")
    registorbutton.place(x=270,y=610)

    root.mainloop()



registration_page()

