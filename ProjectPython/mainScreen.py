#import modules
 
from tkinter import *
import os
from datetime import date
from datetime import datetime
import requests 
import re
main_screen = Tk()

# CREATING THE REGISTRATION SCREEN
 
def register():
    global register_screen
    #LAYOUT INFORMATION:
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    #VARIABLES:
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    #ASKING THE USER TO INSERT THEY DETAILS 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    #THE BUTTON REGISTER WILL SEND THE INFORMATION TO register_user where the information will be manage
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# CREATING LOGIN SCREEN
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    #DESIGNER SET UP
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 #ASKING THE USER TO INSERT THEY DETAILS 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
     #THE BUTTON LOGIN WILL SEND THE INFORMATION TO login_verify WHERE THE INFORMATION WILL BE VERIFIED
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# THE REGISTER BUTTON WILL SEND THE INFORMATION FOR THE FOLLOWING :
 
def register_user():
    #GETTING THE INFORMATION FROM THE USER
    username_info = username.get()
    password_info = password.get()
    #WRITING THE INFORMATION ON A FILE
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info+ "\n")
    file.close() #CLOSING THE FIKE
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 #DISPLAYING THE  MESSAGE
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    news_now()

def news_now():
    global news_screen
    news_screen = Toplevel(main_screen)
    news_screen.title("News")
    #news_screen.geometry("300x250")
    URL = "https://newsapi.org/v2/top-headlines?country=ie&category=business&apiKey=c7e21cd081124ea28a1b9e011327d0a8"
    count=int("0")
    r = requests.get(url=URL)
    data= r.json()
    news_b=[]
    global desc_business
    desc_business=[]
    for x in range(3):
        head= data['articles'][x]['title']
        date= data['articles'][x]['publishedAt']
        content= data['articles'][x]['content']
        count=count+1
        desc_business.append(str(count)+" - "+head +" - "+ date + '\n')
        news_b.append(str(count)+" - "+head +" - "+ date + '\n')
        print(str(count)+" - "+head, date, '\n')
    
   
    frame = LabelFrame(news_screen, text='Business News')
    frame.pack(expand=YES, fill=BOTH)
    
    for y in range(3):
        business_news= Label(frame, text=news_b[y])
        business_news.grid(row=y, column =0)
    b1= Button(frame, text="Save", width=10, height=1, command =lambda:save(news_b[0]))
    b1.grid(row=0, column=1)
    b2= Button(frame, text="Save", width=10, height=1,command =lambda:save(news_b[1]))
    b2.grid(row=1, column=1)   
    b3= Button(frame, text="Save", width=10, height=1,command =lambda:save(news_b[2]))
    b3.grid(row=2, column=1)
    
    URL = "https://newsapi.org/v2/top-headlines?country=ie&category=sports&apiKey=c7e21cd081124ea28a1b9e011327d0a8"
    count1=int("3")
    r = requests.get(url=URL)
    data= r.json()
    news_s=[]
    global desc_sport
    desc_sport=[]
    for x in range(3):
        head= data['articles'][x]['title']
        date= data['articles'][x]['publishedAt']
        content= data['articles'][x]['content']
        count1=count1+1
        desc_sport.append(str(count1)+" - "+head +" - "+ date + '\n')
        news_s.append(str(count1)+" - "+head +" - "+ date + '\n')
        print(str(count1)+" - "+head, date, '\n')
    frame = LabelFrame(news_screen, text='Sport News')
    frame.pack(expand=YES, fill=BOTH)
    
    for y in range(3):
        sport_news= Label(frame, text=news_s[y])
        sport_news.grid(row=y, column =0) 
    b4= Button(frame, text="Save", width=10, height=1,command =lambda:save(news_s[0]))
    b4.grid(row=0, column=1)
    b5= Button(frame, text="Save", width=10, height=1,command =lambda:save(news_s[1]))
    b5.grid(row=1, column=1)   
    b6= Button(frame, text="Save", width=10, height=1,command =lambda:save(news_s[2]))
    b6.grid(row=2, column=1)
    
    URL = "https://newsapi.org/v2/top-headlines?country=ie&category=business&apiKey=c7e21cd081124ea28a1b9e011327d0a8"
    count2=int("6")
    r = requests.get(url=URL)
    data= r.json()
    news_f=[]
    global desc_financial
    desc_financial=[]
    for x in range(3):
        head= data['articles'][x]['title']
        date= data['articles'][x]['publishedAt']
        content= data['articles'][x]['content']
        count2=count2+1
        desc_financial.append(str(count2)+" - "+head +" - "+ date + '\n')
        news_f.append(str(count2)+" - "+head +" - "+ date + '\n')
        print(str(count2)+" - "+head, date, '\n')
        
    frame = LabelFrame(news_screen, text='financial News')
    frame.pack(expand=YES, fill=BOTH)
    
    for y in range(3):
        
        fin_news= Label(frame, text=news_f[y])
        fin_news.grid(row=y, column =0)  
        
    
    b4= Button(frame, text="Save", width=10, height=1,command =lambda:save(news_f[0]))
    b4.grid(row=0, column=1)
    b5= Button(frame, text="Save", width=10, height=1,command =lambda:save(news_f[1]))
    b5.grid(row=1, column=1)   
    b6= Button(frame, text="Save", width=10, height=1,command =lambda:save(news_f[2]))
    b6.grid(row=2, column=1)    
    
    frame = LabelFrame(news_screen, text='Your news')
    frame.pack(expand=YES, fill=BOTH)
    show_your_news= Button(frame, text="Your News", padx=10, pady=10,command =lambda:show_news())
    show_your_news.grid(row=0, column=0)
    
    
def show_news():
    global show_screen
    global delete_entry
    delete= int()
    show_screen = Toplevel(news_screen)
    show_screen.title("Your News")
    login_screen.geometry("300x250")
    Label(show_screen, text="Here is your news: ").pack()
    file = open('your_news','r')
    Label(show_screen, text=file.read()).pack()
    Label(show_screen, text="Would you like to delete any news? Enter the number.").pack()
    delete_entry = Entry(show_screen, textvariable=delete)
    delete_entry.pack()
    Label(show_screen, text="").pack()
    Button(show_screen, text="delete", width=10, height=1, command = delete_news).pack()
    
  
def delete_news():
    x= delete_entry.get()
    find= x+" - "
    f = open("your_news","r")
    lines = f.readlines()
    f.close()
    f = open("your_news","w")
    for line in lines:
        if find not in line:
            f.write(line)
    f.close()
   
    
    
def save(x):
    global save
    news_info = x
    
    
    file = open('your_news', "at")
    file.write(news_info)
    file.close()
    
 
    Label(news_screen, text="Saved Success", fg="green", font=("calibri", 11)).pack()
    
    
 
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    
    global main_screen
    now = datetime.now()
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Welcome! ", bg="green", width="300", height="1", font=("Calibri", 13)).pack()
    Label(text="Here you will keep track of different world events as they occur.", bg="green", width="300", height="1", font=("Calibri", 9)).pack()
    Label(text=today, bg="green", width="300", height="1", font=("Calibri", 9)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
 