import re
import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
from PIL import Image, ImageTk
import datetime

import Bussiness_Access_Library.SavingAccount as SBal
import Bussiness_Access_Library.CurrentAccount as CBal
import Bussiness_Access_Library.FD as FBal
import Bussiness_Access_Library.RecurringAccount as RBal
import Bussiness_Entities as Bent
obj_ent=Bent.AccountsEntities()
window=None
window1=None
window2=None
window3=None
main_window=None
def hide_current_window(window):
    window.withdraw()

def show_last_window2():
    window2.deiconify()

def show_last_window1():
    window.deiconify()

def show_last_window():
    window.deiconify()

def show_main_window():
    main_window.deiconify()

# EXISTING CUSTOMER
def cash_saving_acc_deposit():
    global window3
    window3 = tk.Toplevel()
    window3.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window3, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window3, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window3, text="Enter the account no. ", font=("Arial", 14))
    lbl_amount = tk.Label(window3, text="Enter the deposit amount ", font=("Arial", 14))
    en_accountno = tk.Entry(window3, font=("Roboto", 13, "bold"))
    en_amount = tk.Entry(window3, font=("Roboto", 13, "bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_amount.place(x=50, y=200)
    en_amount.place(x=530, y=200)
    obj_sbal=SBal.CSavingAccount()
    def submit_info():
        transactionid=obj_sbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno=en_accountno.get()
        obj_ent.setaccountno(accountno)
        transactiondate = datetime.datetime.now()
        obj_ent.settransaction_date(transactiondate)
        accounttype="saving"
        obj_ent.setacctype(accounttype)
        transactiontype="credit"
        obj_ent.settranstype(transactiontype)
        amount=en_amount.get()
        obj_ent.setamount(amount)
        obj_sbal.m_deposit(obj_ent)
        messagebox.showinfo(title="Bank Application", message="TRANSACTION IS SUCCESSFULL.")
    submit_button = tk.Button(window3, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window3, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_last_window2()], bg="orange", bd=5)
    Home_button = tk.Button(window3, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window3, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window3.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    submit_button.place(x=250, y=350)
    window3.mainloop()
def cash_saving_acc_withdraw():
    global window3
    window3 = tk.Toplevel()
    window3.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window3, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window3, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window3, text="Enter the account no. ", font=("Arial", 14))
    lbl_amount = tk.Label(window3, text="Enter the withdrawal amount ", font=("Arial", 14))
    en_accountno = tk.Entry(window3, font=("Roboto", 13, "bold"))
    en_amount = tk.Entry(window3, font=("Roboto", 13, "bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_amount.place(x=50, y=200)
    en_amount.place(x=530, y=200)
    obj_sbal=SBal.CSavingAccount()
    def submit_info():
        transactionid = obj_sbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = en_accountno.get()
        obj_ent.setaccountno(accountno)
        transactiondate = datetime.datetime.now()
        obj_ent.settransaction_date(transactiondate)
        accounttype = "saving"
        obj_ent.setacctype(accounttype)
        transactiontype = "debit"
        obj_ent.settranstype(transactiontype)
        amount = en_amount.get()
        obj_ent.setamount(amount)
        obj_sbal.m_withdrawal(obj_ent)
        messagebox.showinfo(title="Bank Application", message="TRANSACTION IS SUCCESSFULL.")
    submit_button = tk.Button(window3, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window3, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_last_window2()], bg="orange", bd=5)
    Home_button = tk.Button(window3, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window3, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window3.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    submit_button.place(x=250, y=350)
    window3.mainloop()
def cash_current_acc_deposit():
    global window3
    window3 = tk.Toplevel()
    window3.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window3, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window3, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window3, text="Enter the account no. ", font=("Arial", 14))
    lbl_amount = tk.Label(window3, text="Enter the deposit amount ", font=("Arial", 14))
    en_accountno = tk.Entry(window3, font=("Roboto", 13, "bold"))
    en_amount = tk.Entry(window3, font=("Roboto", 13, "bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_amount.place(x=50, y=200)
    en_amount.place(x=530, y=200)
    obj_cbal=CBal.CCurrentAccount()
    def submit_info():
        transactionid = obj_cbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = en_accountno.get()
        obj_ent.setaccountno(accountno)
        transactiondate = datetime.datetime.now()
        obj_ent.settransaction_date(transactiondate)
        accounttype = "current"
        obj_ent.setacctype(accounttype)
        transactiontype = "credit"
        obj_ent.settranstype(transactiontype)
        amount = en_amount.get()
        obj_ent.setamount(amount)
        obj_cbal.m_deposit(obj_ent)
        messagebox.showinfo(title="Bank Application", message="TRANSACTION IS SUCCESSFULL.")
    submit_button = tk.Button(window3, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window3, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_last_window2()], bg="orange", bd=5)
    Home_button = tk.Button(window3, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window3, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window3.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    submit_button.place(x=250, y=350)
    window3.mainloop()
def cash_current_acc_withdraw():
    global window3
    window3 = tk.Toplevel()
    window3.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window3, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window3, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window3, text="Enter the account no. ", font=("Arial", 14))
    lbl_amount = tk.Label(window3, text="Enter the withdrawal amount ", font=("Arial", 14))
    en_accountno = tk.Entry(window3, font=("Roboto", 13, "bold"))
    en_amount = tk.Entry(window3, font=("Roboto", 13, "bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_amount.place(x=50, y=200)
    en_amount.place(x=530, y=200)
    obj_cbal = CBal.CCurrentAccount()
    def submit_info():
        transactionid = obj_cbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = en_accountno.get()
        obj_ent.setaccountno(accountno)
        transactiondate = datetime.datetime.now()
        obj_ent.settransaction_date(transactiondate)
        accounttype = "current"
        obj_ent.setacctype(accounttype)
        transactiontype = "debit"
        obj_ent.settranstype(transactiontype)
        amount = en_amount.get()
        obj_ent.setamount(amount)
        obj_cbal.m_withdrawal(obj_ent)
        messagebox.showinfo(title="Bank Application", message="TRANSACTION IS SUCCESSFULL.")
    submit_button = tk.Button(window3, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window3, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_last_window2()], bg="orange", bd=5)
    Home_button = tk.Button(window3, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window3, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window3.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    submit_button.place(x=250, y=350)
    window3.mainloop()
def cash_fd_acc_deposit():
    global window3
    window3 = tk.Toplevel()
    window3.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window3, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window3, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window3, text="Enter the account no. ", font=("Arial", 14))
    lbl_amount = tk.Label(window3, text="Enter the deposit amount ", font=("Arial", 14))
    en_accountno = tk.Entry(window3, font=("Roboto", 13, "bold"))
    en_amount = tk.Entry(window3, font=("Roboto", 13, "bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_amount.place(x=50, y=200)
    en_amount.place(x=530, y=200)
    obj_fbal=FBal.CFDaccount()
    def submit_info():
        transactionid = obj_fbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = en_accountno.get()
        obj_ent.setaccountno(accountno)
        transactiondate = datetime.datetime.now()
        obj_ent.settransaction_date(transactiondate)
        accounttype = "fd"
        obj_ent.setacctype(accounttype)
        transactiontype = "credit"
        obj_ent.settranstype(transactiontype)
        amount = en_amount.get()
        obj_ent.setamount(amount)
        obj_fbal.m_deposit(obj_ent)
        messagebox.showinfo(title="Bank Application", message="TRANSACTION IS SUCCESSFULL.")
    submit_button = tk.Button(window3, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window3, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_last_window2()], bg="orange", bd=5)
    Home_button = tk.Button(window3, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window3, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window3.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    submit_button.place(x=250, y=350)
    window3.mainloop()
def cash_fd_acc_withdraw():
    global window3
    window3 = tk.Toplevel()
    window3.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window3, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window3, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window3, text="Enter the account no. ", font=("Arial", 14))
    lbl_amount = tk.Label(window3, text="Enter the withdrawal amount ", font=("Arial", 14))
    en_accountno = tk.Entry(window3, font=("Roboto", 13, "bold"))
    en_amount = tk.Entry(window3, font=("Roboto", 13, "bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_amount.place(x=50, y=200)
    en_amount.place(x=530, y=200)
    obj_fbal = FBal.CFDaccount()
    def submit_info():
        transactionid = obj_fbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = en_accountno.get()
        obj_ent.setaccountno(accountno)
        transactiondate = datetime.datetime.now()
        obj_ent.settransaction_date(transactiondate)
        accounttype = "fd"
        obj_ent.setacctype(accounttype)
        transactiontype = "debit"
        obj_ent.settranstype(transactiontype)
        amount = en_amount.get()
        obj_ent.setamount(amount)
        obj_fbal.m_withdrawal(obj_ent)
        messagebox.showinfo(title="Bank Application", message="TRANSACTION IS SUCCESSFULL.")
    submit_button = tk.Button(window3, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window3, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_last_window2()], bg="orange", bd=5)
    Home_button = tk.Button(window3, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window3, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window3.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    submit_button.place(x=250, y=350)
    window3.mainloop()
def cash_recurring_acc_deposit():
    global window3
    window3 = tk.Toplevel()
    window3.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window3, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window3, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window3, text="Enter the account no. ", font=("Arial", 14))
    lbl_amount = tk.Label(window3, text="Enter the deposit amount ", font=("Arial", 14))
    en_accountno = tk.Entry(window3, font=("Roboto", 13, "bold"))
    en_amount = tk.Entry(window3, font=("Roboto", 13, "bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_amount.place(x=50, y=200)
    en_amount.place(x=530, y=200)
    obj_rbal=RBal.CRecurringAccount()
    def submit_info():
        transactionid = obj_rbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = en_accountno.get()
        obj_ent.setaccountno(accountno)
        transactiondate = datetime.datetime.now()
        obj_ent.settransaction_date(transactiondate)
        accounttype = "recurring"
        obj_ent.setacctype(accounttype)
        transactiontype = "credit"
        obj_ent.settranstype(transactiontype)
        amount = en_amount.get()
        obj_ent.setamount(amount)
        obj_rbal.m_deposit(obj_ent)
        messagebox.showinfo(title="Bank Application", message="TRANSACTION IS SUCCESSFULL.")
    submit_button = tk.Button(window3, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window3, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_last_window2()], bg="orange", bd=5)
    Home_button = tk.Button(window3, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window3, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window3.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    submit_button.place(x=250, y=350)
    window3.mainloop()
def cash_recurring_acc_withdraw():
    global window3
    window3 = tk.Toplevel()
    window3.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window3, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window3, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window3, text="Enter the account no. ", font=("Arial", 14))
    lbl_amount = tk.Label(window3, text="Enter the withdrawal amount ", font=("Arial", 14))
    en_accountno = tk.Entry(window3, font=("Roboto", 13, "bold"))
    en_amount = tk.Entry(window3, font=("Roboto", 13, "bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_amount.place(x=50, y=200)
    en_amount.place(x=530, y=200)
    obj_rbal = RBal.CRecurringAccount()
    def submit_info():
        transactionid = obj_rbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = en_accountno.get()
        obj_ent.setaccountno(accountno)
        transactiondate = datetime.datetime.now()
        obj_ent.settransaction_date(transactiondate)
        accounttype = "recurring"
        obj_ent.setacctype(accounttype)
        transactiontype = "debit"
        obj_ent.settranstype(transactiontype)
        amount = en_amount.get()
        obj_ent.setamount(amount)
        obj_rbal.m_withdrawal(obj_ent)
        messagebox.showinfo(title="Bank Application", message="TRANSACTION IS SUCCESSFULL.")
    submit_button = tk.Button(window3, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window3, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_last_window2()], bg="orange", bd=5)
    Home_button = tk.Button(window3, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window3), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window3, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window3.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    submit_button.place(x=250, y=350)
    window3.mainloop()
def saving_account_details():
    global window2
    window2 = tk.Toplevel()
    window2.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window2, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window2, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    cash_deposit_button = tk.Button(window2, text="Cash Deposit", width=25, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), cash_saving_acc_deposit()], bg="aquamarine", bd=5)
    cash_withdraw_button = tk.Button(window2, text="Cash Withdraw", width=25, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), cash_saving_acc_withdraw()], bg="aquamarine", bd=5)
    Back_button = tk.Button(window2, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), show_last_window()], bg="orange", bd=5)
    Home_button = tk.Button(window2, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window2, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window2.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    cash_deposit_button.place(x=270, y=200)
    cash_withdraw_button.place(x=270, y=250)
    window2.mainloop()
def current_account_details():
    global window2
    window2 = tk.Toplevel()
    window2.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window2, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window2, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    cash_deposit_button = tk.Button(window2, text="Cash Deposit", width=25, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), cash_current_acc_deposit()], bg="aquamarine", bd=5)
    cash_withdraw_button = tk.Button(window2, text="Cash Withdraw", width=25, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), cash_current_acc_withdraw()], bg="aquamarine", bd=5)
    Back_button = tk.Button(window2, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), show_last_window()], bg="orange", bd=5)
    Home_button = tk.Button(window2, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window2, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window2.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    cash_deposit_button.place(x=270, y=200)
    cash_withdraw_button.place(x=270, y=250)
    window2.mainloop()
def fd_account_details():
    global window2
    window2 = tk.Toplevel()
    window2.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window2, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window2, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    cash_deposit_button = tk.Button(window2, text="Cash Deposit", width=25, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), cash_fd_acc_deposit()], bg="aquamarine", bd=5)
    cash_withdraw_button = tk.Button(window2, text="Cash Withdraw", width=25, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), cash_fd_acc_withdraw()], bg="aquamarine", bd=5)
    Back_button = tk.Button(window2, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), show_last_window()], bg="orange", bd=5)
    Home_button = tk.Button(window2, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window2, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window2.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    cash_deposit_button.place(x=270, y=200)
    cash_withdraw_button.place(x=270, y=250)
    window2.mainloop()
def recurring_account_details():
    global window2
    window2 = tk.Toplevel()
    window2.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window2, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window2, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    cash_deposit_button = tk.Button(window2, text="Cash Deposit", width=25, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), cash_recurring_acc_deposit()], bg="aquamarine", bd=5)
    cash_withdraw_button = tk.Button(window2, text="Cash Withdraw", width=25, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), cash_recurring_acc_withdraw()], bg="aquamarine", bd=5)
    Back_button = tk.Button(window2, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), show_last_window()], bg="orange", bd=5)
    Home_button = tk.Button(window2, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window2), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window2, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window2.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    cash_deposit_button.place(x=270, y=200)
    cash_withdraw_button.place(x=270, y=250)
    window2.mainloop()
def Existing_customer():
    global window
    window = tk.Toplevel()
    window.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    Saving_acc_button = tk.Button(window, text="Saving Account", width=25, font=("Roboto", 15, "bold"),
                          command=lambda: [hide_current_window(window), saving_account_details()], bg="aquamarine", bd=5)
    Current_acc_button = tk.Button(window, text="Current Account", width=25, font=("Roboto", 15, "bold"),
                          command=lambda: [hide_current_window(window), current_account_details()], bg="aquamarine", bd=5)
    FD_button = tk.Button(window, text="FD Account", width=25, font=("Roboto", 15, "bold"),
                          command=lambda: [hide_current_window(window), fd_account_details()], bg="aquamarine", bd=5)
    Demat_acc = tk.Button(window, text="Recurring Account", width=25, font=("Roboto", 15, "bold"),
                          command=lambda: [hide_current_window(window), recurring_account_details()], bg="aquamarine", bd=5)
    Exit_button = tk.Button(window, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                          command=window.destroy, bg="orange", bd=5)
    Home_button = tk.Button(window, text="HOME", width=10, font=("Roboto", 15, "bold"),
                          command=lambda: [hide_current_window(window), show_main_window()], bg="orange", bd=5)
    Saving_acc_button.place(x=270, y=150)
    Current_acc_button.place(x=270, y=200)
    FD_button.place(x=270, y=250)
    Demat_acc.place(x=270, y=300)
    Home_button.place(x=10, y=450)
    Exit_button.place(x=660, y=450)
    window.mainloop()


# NEW CUSTOMERS
def open_saving_account():
    global window1
    window1 = tk.Toplevel()
    window1.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window1, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window1, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_name = tk.Label(window1, text="Enter the Account Holder Name ", font=("Arial", 14))
    #lbl_acc_opening_date = tk.Label(window, text="Enter the Account Opening Date(DD-MM-YYYY) ", font=("Arial", 14))
    lbl_phone_no = tk.Label(window1, text="Enter the Phone Number ", font=("Arial", 14))
    lbl_email_id = tk.Label(window1, text="Enter the Email id ", font=("Arial", 14))
    lbl_initial_amount = tk.Label(window1, text="Enter the Initial Amount (Rs. 2500) ", font=("Arial", 14))

    en_name = tk.Entry(window1, font=("Roboto", 13, "bold"), placeholder="Alphabets are allowed.")
    #en_acc_opening_date = tk.Entry(window, font=("Roboto", 13, "bold"))
    en_initial_amount = tk.Entry(window1, font=("Roboto", 13, "bold"))
    en_phone_no = tk.Entry(window1, font=("Roboto", 13, "bold"))
    en_email_id = tk.Entry(window1, font=("Roboto", 13, "bold"))

    lbl_name.place(x=50, y=100)
    en_name.place(x=530, y=100)
    #lbl_acc_opening_date.place(x=50, y=150)
    #en_acc_opening_date.place(x=530, y=150)
    lbl_phone_no.place(x=50, y=150)
    en_phone_no.place(x=530, y=150)
    lbl_email_id.place(x=50, y=200)
    en_email_id.place(x=530, y=200)
    lbl_initial_amount.place(x=50, y=250)
    en_initial_amount.place(x=530, y=250)
    obj_sbal=SBal.CSavingAccount()
    def submit_info():
        transactionid = obj_sbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno=obj_sbal.m_automatic_account_id() #set account number
        obj_ent.setaccountno(accountno)
        accholdername=en_name.get().title() #set account holder name
        if re.match(r"^[a-zA-z\s]+$", accholdername):
            obj_ent.setaccholdername(accholdername)
        else:
            messagebox.showerror(title="Error", message="PLEASE ENTER THE CORRECT ACCOUNT HOLDER NAME.\nOnly letters and spaces are allowed.")
        openingdate=datetime.datetime.now() #set system current date and time
        obj_ent.set_acc_opening_date(openingdate)
        acctype="saving" #set account type as saving
        obj_ent.setacctype(acctype)
        phoneno=en_phone_no.get() #set phone number
        if len(phoneno) != 10:
            messagebox.showerror(title="Error", message="PLEASE ENTER THE CORRECT PHONE NUMBER."
                                                        "\nTHE PHONE NUMBER ONLY CONTAINS NUMBERS AND HAVING LENGTH OF 10 DIGITS.")
            pass
        else:
            obj_ent.set_phone_no(phoneno)
        emailid=en_email_id.get() #set emailid
        obj_ent.set_email_id(emailid)
        initialamount=float(en_initial_amount.get()) #set initial amount
        if initialamount != 2500:
            messagebox.showerror(title="Error", message="PLEASE ENTER THE CORRECT OPENING AMOUNT RS.2500/-.")
            pass
        else:
            obj_ent.set_initial_amount(initialamount)

        obj_sbal.m_insert_account_info(obj_ent) #calling saving account method

        obj_ent.settransaction_date(openingdate) #set transaction date for saving transaction table
        transactiontype = "credit"
        obj_ent.settranstype(transactiontype) #set transaction type
        obj_ent.setamount(initialamount) #set amount for saving account
        obj_sbal.m_deposit(obj_ent) #deposit amount then calling to store all the objects in the transaction account
        messagebox.showinfo(title="Bank Application", message="SAVING ACCOUNT OPEN SUCCESSFULLY.")
    amount_submit_button = tk.Button(window1, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                                     command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window1, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_last_window1()], bg="orange", bd=5)
    Home_button = tk.Button(window1, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window1, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window1.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    amount_submit_button.place(x=250, y=300)
    window1.mainloop()
def open_current_account():
    global window1
    window1 = tk.Toplevel()
    window1.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window1, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window1, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)

    lbl_name = tk.Label(window1, text="Enter the Account Holder Name ", font=("Arial", 14))
    #lbl_acc_opening_date = tk.Label(window, text="Enter the Account Opening Date(YYYY-MM-DD) ", font=("Arial", 14))
    lbl_phone_no = tk.Label(window1, text="Enter the Phone Number ", font=("Arial", 14))
    lbl_email_id = tk.Label(window1, text="Enter the Email id ", font=("Arial", 14))

    en_name = tk.Entry(window1, font=("Roboto", 13, "bold"))
    #en_acc_opening_date = tk.Entry(window, font=("Roboto", 13, "bold"))
    en_phone_no = tk.Entry(window1, font=("Roboto", 13, "bold"))
    en_email_id = tk.Entry(window1, font=("Roboto", 13, "bold"))

    lbl_name.place(x=50, y=100)
    en_name.place(x=530, y=100)
    #lbl_acc_opening_date.place(x=50, y=150)
    #en_acc_opening_date.place(x=530, y=150)
    lbl_phone_no.place(x=50, y=150)
    en_phone_no.place(x=530, y=150)
    lbl_email_id.place(x=50, y=200)
    en_email_id.place(x=530, y=200)

    obj_cbal=CBal.CCurrentAccount()
    def submit_info():
        transactionid = obj_cbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = obj_cbal.m_automatic_account_id()  # set account number
        obj_ent.setaccountno(accountno)
        accholdername = en_name.get().title()  # set account holder name
        if re.match(r"^[a-zA-z\s]+$", accholdername):
            obj_ent.setaccholdername(accholdername)
        else:
            messagebox.showerror(title="Error",
                                 message="PLEASE ENTER THE CORRECT ACCOUNT HOLDER NAME.\nOnly letters and spaces are allowed.")
        openingdate = datetime.datetime.now()  # set system current date and time
        obj_ent.set_acc_opening_date(openingdate)
        acctype = "current"  # set account type as current
        obj_ent.setacctype(acctype)
        phoneno = en_phone_no.get()  # set phone number
        if len(phoneno) != 10:
            messagebox.showerror(title="Error", message="PLEASE ENTER THE CORRECT PHONE NUMBER."
                                                        "\nTHE PHONE NUMBER ONLY CONTAINS NUMBERS AND HAVING LENGTH OF 10 DIGITS.")
            pass
        else:
            obj_ent.set_phone_no(phoneno)
        emailid = en_email_id.get()  #set emailid
        obj_ent.set_email_id(emailid)
        obj_cbal.m_insert_account_info(obj_ent)  #calling saving account method
        obj_ent.settransaction_date(openingdate)#set transaction date for saving transaction table
        initialamount=0.00
        obj_ent.set_initial_amount(initialamount)
        transactiontype = "credit"
        obj_ent.settranstype(transactiontype)  #set transaction type
        obj_cbal.m_deposit(obj_ent)  #deposit amount then calling to store all the objects in the transaction account
        messagebox.showinfo(title="Bank Application", message="CURRENT ACCOUNT OPEN SUCCESSFULLY.")
    amount_submit_button = tk.Button(window1, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                                     command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window1, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_last_window1()], bg="orange", bd=5)
    Home_button = tk.Button(window1, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window1, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window1.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    amount_submit_button.place(x=250, y=250)
    window1.mainloop()
def open_fd_account():
    global window1
    window1 = tk.Toplevel()
    window1.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window1, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window1, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)

    lbl_name = tk.Label(window1, text="Enter the Account Holder Name ", font=("Arial", 14))
    #lbl_acc_opening_date = tk.Label(window, text="Enter the Account Opening Date(YYYY-MM-DD) ", font=("Arial", 14))
    lbl_phone_no = tk.Label(window1, text="Enter the Phone Number ", font=("Arial", 14))
    lbl_email_id = tk.Label(window1, text="Enter the Email id ", font=("Arial", 14))
    lbl_initial_amount = tk.Label(window1, text="Enter the Initial Amount (Rs. 1000) ", font=("Arial", 14))

    en_name = tk.Entry(window1, font=("Roboto", 13, "bold"))
    #en_acc_opening_date = tk.Entry(window, font=("Roboto", 13, "bold"))
    en_initial_amount = tk.Entry(window1, font=("Roboto", 13, "bold"))
    en_phone_no = tk.Entry(window1, font=("Roboto", 13, "bold"))
    en_email_id = tk.Entry(window1, font=("Roboto", 13, "bold"))

    lbl_name.place(x=50, y=100)
    en_name.place(x=530, y=100)
    #lbl_acc_opening_date.place(x=50, y=150)
    #en_acc_opening_date.place(x=530, y=150)
    lbl_phone_no.place(x=50, y=150)
    en_phone_no.place(x=530, y=150)
    lbl_email_id.place(x=50, y=200)
    en_email_id.place(x=530, y=200)
    lbl_initial_amount.place(x=50, y=250)
    en_initial_amount.place(x=530, y=250)

    obj_fbal = FBal.CFDaccount()

    def submit_info():
        transactionid = obj_fbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = obj_fbal.m_automatic_account_id()
        obj_ent.setaccountno(accountno)
        accholdername = en_name.get().title()
        if re.match(r"^[a-zA-z\s]+$", accholdername):
            obj_ent.setaccholdername(accholdername)
        else:
            messagebox.showerror(title="Error", message="PLEASE ENTER THE CORRECT ACCOUNT HOLDER NAME.\nOnly letters and spaces are allowed.")
        openingdate = datetime.datetime.now()
        obj_ent.set_acc_opening_date(openingdate)
        obj_ent.settransaction_date(openingdate)
        acctype = "fd"
        obj_ent.setacctype(acctype)
        phoneno = en_phone_no.get()
        if len(phoneno) != 10:
            messagebox.showerror(title="Error", message="PLEASE ENTER THE CORRECT PHONE NUMBER."
                                                        "\nTHE PHONE NUMBER ONLY CONTAINS NUMBERS AND HAVING LENGTH OF 10 DIGITS.")
            pass
        else:
            obj_ent.set_phone_no(phoneno)
        emailid = en_email_id.get()
        obj_ent.set_email_id(emailid)
        initialamount = float(en_initial_amount.get())
        if initialamount != 1000:
            messagebox.showerror(title="Error", message="PLEASE ENTER THE CORRECT OPENING AMOUNT RS.1000/-.")
            pass
        else:
            obj_ent.set_initial_amount(initialamount)
        obj_fbal.m_insert_account_info(obj_ent)
        obj_ent.settransaction_date(openingdate)
        transactiontype = "credit"
        obj_ent.settranstype(transactiontype)
        obj_ent.setamount(initialamount)
        obj_fbal.m_deposit(obj_ent)
        messagebox.showinfo(title="Bank Application", message="FD ACCOUNT OPEN SUCCESSFULLY.")

    amount_submit_button = tk.Button(window1, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                           command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window1, text="BACK", width=10, font=("Roboto", 15, "bold"),
                           command=lambda: [hide_current_window(window1), show_last_window1()], bg="orange", bd=5)
    Home_button = tk.Button(window1, text="HOME", width=10, font=("Roboto", 15, "bold"),
                           command=lambda: [hide_current_window(window1), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window1, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                           command=window1.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    amount_submit_button.place(x=250, y=300)
    window1.mainloop()
def open_recurring_account():
    global window1
    window1 = tk.Toplevel()
    window1.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window1, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window1, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)

    lbl_name = tk.Label(window1, text="Enter the Account Holder Name ", font=("Arial", 14))
    #lbl_acc_opening_date = tk.Label(window, text="Enter the Account Opening Date(YYYY-MM-DD) ", font=("Arial", 14))
    lbl_phone_no = tk.Label(window1, text="Enter the Phone Number ", font=("Arial", 14))
    lbl_email_id = tk.Label(window1, text="Enter the Email id ", font=("Arial", 14))
    lbl_initial_amount=tk.Label(window1, text="Enter the Initial Amount (Rs.100/-) ", font=("Arial", 14))

    en_name = tk.Entry(window1, font=("Roboto", 13, "bold"))
    #en_acc_opening_date = tk.Entry(window, font=("Roboto", 13, "bold"))
    en_phone_no = tk.Entry(window1, font=("Roboto", 13, "bold"))
    en_email_id = tk.Entry(window1, font=("Roboto", 13, "bold"))
    en_intial_amount= tk.Entry(window1, font=("Roboto", 13, "bold"))

    lbl_name.place(x=50, y=100)
    en_name.place(x=530, y=100)
    #lbl_acc_opening_date.place(x=50, y=150)
    #en_acc_opening_date.place(x=530, y=150)
    lbl_phone_no.place(x=50, y=150)
    en_phone_no.place(x=530, y=150)
    lbl_email_id.place(x=50, y=200)
    en_email_id.place(x=530, y=200)
    lbl_initial_amount.place(x=50, y=250)
    en_intial_amount.place(x=530, y=250)
    obj_rbal = RBal.CRecurringAccount()

    def submit_info():
        transactionid = obj_rbal.m_transaction_id()
        obj_ent.set_transaction_id(transactionid)
        accountno = obj_rbal.m_automatic_account_id()
        obj_ent.setaccountno(accountno)
        accholdername = en_name.get().title()
        if re.match(r"^[a-zA-z\s]+$", accholdername):
            obj_ent.setaccholdername(accholdername)
        else:
            messagebox.showerror(title="Error",
                                 message="PLEASE ENTER THE CORRECT ACCOUNT HOLDER NAME.\nOnly letters and spaces are allowed.")
        openingdate = datetime.datetime.now()
        obj_ent.set_acc_opening_date(openingdate)
        acctype = "recurring"
        obj_ent.setacctype(acctype)
        phoneno = en_phone_no.get()
        if len(phoneno) != 10 and phoneno.isdigit():
            messagebox.showerror(title="Error", message="PLEASE ENTER THE CORRECT PHONE NUMBER."
                                                        "\nTHE PHONE NUMBER ONLY CONTAINS NUMBERS AND HAVING LENGTH OF 10 DIGITS.")
            pass
        else:
            obj_ent.set_phone_no(phoneno)
        emailid = en_email_id.get()
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", emailid):
            obj_ent.set_email_id(emailid)
        else:
            messagebox.showerror(title="Error", message="PLEASE ENTER THE CORRECT EMAIL ID. Example: example@domain.com")
        initialamount = en_intial_amount.get()
        obj_ent.set_initial_amount(initialamount)
        obj_rbal.m_insert_account_info(obj_ent)
        obj_ent.settransaction_date(openingdate)
        transactiontype = "credit"
        obj_ent.settranstype(transactiontype)
        obj_ent.setamount(initialamount)
        obj_rbal.m_deposit(obj_ent)
        messagebox.showinfo(title="Bank Application", message="DEMAT ACCOUNT OPEN SUCCESSFULLY.")

    amount_submit_button = tk.Button(window1, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                           command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window1, text="BACK", width=10, font=("Roboto", 15, "bold"),
                           command=lambda: [hide_current_window(window1), show_last_window1()], bg="orange", bd=5)
    Home_button = tk.Button(window1, text="HOME", width=10, font=("Roboto", 15, "bold"),
                           command=lambda: [hide_current_window(window1), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window1, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                           command=window1.destroy, bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    amount_submit_button.place(x=250, y=300)
    window1.mainloop()
def New_customer():
    response=messagebox.askyesno(title="WARNING", message="Do you want to open a new account in ANMOL BANK?")
    if response:
        global window
        window = tk.Toplevel()
        window.title("Bank Application")
        image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
        image = image.resize((800, 500), )
        bg_image = ImageTk.PhotoImage(image)
        canvas = tk.Canvas(window, width=image.width, height=image.height)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        canvas.image = bg_image
        lbl_bank_name = tk.Label(window, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                                 bg="gold", bd=5)
        lbl_bank_name.place(x=0, y=0)
        # Buttons
        Saving_acc_button = tk.Button(window, text="Saving Account", width=25, font=("Roboto", 15, "bold"),
                        command=lambda: [hide_current_window(window), open_saving_account()], bg="aquamarine", bd=5)
        Current_acc_button = tk.Button(window, text="Current Account", width=25, font=("Roboto", 15, "bold"),
                        command=lambda: [hide_current_window(window), open_current_account()], bg="aquamarine", bd=5)
        FD_button = tk.Button(window, text="FD Account", width=25, font=("Roboto", 15, "bold"),
                        command=lambda: [hide_current_window(window), open_fd_account()], bg="aquamarine", bd=5)
        Demat_acc = tk.Button(window, text="Recurring Account", width=25, font=("Roboto", 15, "bold"),
                        command=lambda: [hide_current_window(window), open_recurring_account()], bg="aquamarine", bd=5)
        Home_button = tk.Button(window, text="HOME", width=10, font=("Roboto", 15, "bold"),
                        command=lambda: [hide_current_window(window), show_main_window()], bg="orange", bd=5)
        Exit_button = tk.Button(window, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                        command=window.destroy, bg="orange", bd=5)
        Saving_acc_button.place(x=270, y=150)
        Current_acc_button.place(x=270, y=200)
        FD_button.place(x=270, y=250)
        Demat_acc.place(x=270, y=300)
        Home_button.place(x=10, y=450)
        Exit_button.place(x=660, y=450)
        window.mainloop()
    else:
        messagebox.showerror(title="Warning", text="HAULTED!!!!")

# OTHER SERVICES
def show_about_user_details(obj_ent, Comboboxvalue):
    global window
    window = tk.Toplevel()
    window.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    if Comboboxvalue=="Saving":
        obj_bal=SBal.CSavingAccount()
        data=obj_bal.m_fetch_all_saving_acc_details(obj_ent)
    elif Comboboxvalue=="Current":
        obj_bal=CBal.CCurrentAccount()
        data=obj_bal.m_fetch_all_current_acc_details(obj_ent)
    elif Comboboxvalue=="FD":
        obj_bal=FBal.CFDaccount()
        data=obj_bal.m_fetch_all_fd_acc_details(obj_ent)
    elif Comboboxvalue=="Recurring":
        obj_bal = RBal.CRecurringAccount()
        data=obj_bal.m_fetch_all_recurring_acc_details(obj_ent)
    listbox=tk.Listbox(window, width=50, height=8, font=("Arial", 14))
    for item in data:
        listbox.insert(tk.END, f"Account Number: {item[0]}")
        listbox.insert(tk.END, f"Account Holder Name: {item[1]}")
        listbox.insert(tk.END, f"Account Opening Date: {item[2]}")
        listbox.insert(tk.END, f"Account Type: {item[3]}")
        listbox.insert(tk.END, f"Phone Number: {item[4]}")
        listbox.insert(tk.END, f"Email ID: {item[5]}")
        listbox.insert(tk.END, f"Initial Account Opening Amount: {item[6]}")
    listbox.place(x=150, y=150)
    window.mainloop()
def about_user(obj_ent=Bent.AccountsEntities()):
    global window1
    window1 = tk.Toplevel()
    window1.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window1, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window1, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window1, text="Enter the Account No. ", font=("Arial", 14))
    lbl_accounttype=tk.Label(window1, text="Enter the Account Type", font=("Arial", 14))
    en_accountno= tk.Entry(window1, font=("Arial", 14,"bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_accounttype.place(x=50, y=200)
    # Dropdown/Combobox for selecting Account_type
    option3=['Saving', 'Current', 'FD', 'Recurring']
    combobox= ttk.Combobox(window1, values=option3, width=18, font=("Arial", 14, "bold"))
    combobox.set("select an option") #Default Value
    combobox.place(x=530, y=200)
    global comboboxvalue
    def submit_info():
        accountno=en_accountno.get()
        obj_ent.setaccountno(accountno)
        comboboxvalue=combobox.get()
        show_about_user_details(obj_ent, comboboxvalue)
    amount_submit_button = tk.Button(window1, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                                     command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window1, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_last_window1()], bg="orange", bd=5)
    Home_button = tk.Button(window1, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window1, text="EXIT", width=10, font=("Roboto", 15, "bold"), command=window1.destroy,
                            bg="orange", bd=5)
    amount_submit_button.place(x=250, y=300)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    window1.mainloop()

def show_transaction_history_data(obj_ent, comboboxvalue):
    global window, data
    window = tk.Toplevel()
    window.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    if comboboxvalue=="Saving":
        obj_bal=SBal.CSavingAccount()
        data = obj_bal.m_fetch_all_account_transactions(obj_ent)
    elif comboboxvalue=="Current":
        obj_bal=CBal.CCurrentAccount()
        data = obj_bal.m_fetch_all_account_transactions(obj_ent)
    elif comboboxvalue=="FD":
        obj_bal=FBal.CFDaccount()
        data=obj_bal.m_fetch_all_account_transactions(obj_ent)
    elif comboboxvalue=="Recurring":
        obj_bal=RBal.CRecurringAccount()
        data=obj_bal.m_fetch_all_account_transactions(obj_ent)
    listbox = tk.Listbox(window, width=68, height=19, font=("Arial", 14))
    listbox.place(x=21, y=45)
    scrollbar=tk.Scrollbar(window, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.place(x=758, y=50, height=430)  # Positioning it on the right of the listbox
    # Configure the Listbox to work with the scrollbar
    listbox.config(yscrollcommand=scrollbar.set)
    for item in data:
        listbox.insert(tk.END, f"Transaction ID: {item[0]}")
        listbox.insert(tk.END, f"Transaction Date: {item[1]}")
        listbox.insert(tk.END, f"Transaction Type: {item[2]}")
        listbox.insert(tk.END, f"Transaction Amount: {item[3]}")
        listbox.insert(tk.END,"<------------------------------------------------------------->")
    Back_button = tk.Button(window, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window), show_last_window()], bg="orange", bd=5)
    Home_button = tk.Button(window, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window, text="EXIT", width=10, font=("Roboto", 15, "bold"), command=window.destroy,
                            bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    window.mainloop()

def user_transaction_History():
    global window1
    window1 = tk.Toplevel()
    window1.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window1, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window1, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    lbl_accountno = tk.Label(window1, text="Enter the Account No. ", font=("Arial", 14))
    lbl_accounttype=tk.Label(window1, text="Choose the Account Type ", font=("Arial", 14))
    options=['Saving', 'Current', 'FD', 'Recurring']
    combobox=ttk.Combobox(window1, values=options, font=("Arial", 14), width=19)
    combobox.set("Select an option")
    en_accountno = tk.Entry(window1, font=("Roboto", 13, "bold"))
    lbl_accountno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_accounttype.place(x=50, y=200)
    combobox.place(x=530, y=200)
    global comboboxvalue
    def submit_info():
        accountno=en_accountno.get()
        obj_ent.setaccountno(accountno)
        comboboxvalue = combobox.get()
        show_transaction_history_data(obj_ent, comboboxvalue)
    submit_button = tk.Button(window1, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                                     command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window1, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_last_window1()], bg="orange", bd=5)
    Home_button = tk.Button(window1, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window1, text="EXIT", width=10, font=("Roboto", 15, "bold"), command=window1.destroy,
                            bg="orange", bd=5)
    submit_button.place(x=250, y=300)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    window1.mainloop()
def data_updation():
    global window1
    window1 = tk.Toplevel()
    window1.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window1, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window1, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    global comboboxvalue1, comboboxvalue2, obj_bal
    lbl_acctype=tk.Label(window1, text='Choose the account type', font=("Arial", 14))
    option3=["Saving", "Current", "FD", "Recurring"]
    combobox1=ttk.Combobox(window1, values=option3, font=("Arial", 14), width=19)
    lbl_accontno = tk.Label(window1, text="Enter the account no.", font=("Arial", 14))
    en_accountno = tk.Entry(window1, font=("Arial", 14))
    lbl_choice=tk.Label(window1, text="Choose Detail for updation", font=("Arial", 14))
    option4=["Account_Holder_Name", "Phone_Number", "Email_ID"]
    combobox2=ttk.Combobox(window1, values=option4, font=("Arial", 14), width=19)
    lbl_columnvalue=tk.Label(window1, text="Enter the value for updation", font=("Arial", 14))
    en_columnvalue=tk.Entry(window1, font=("Arial", 14))
    lbl_acctype.place(x=50, y=100)
    combobox1.place(x=530, y=100)
    lbl_accontno.place(x=50, y=150)
    en_accountno.place(x=530, y=150)
    lbl_choice.place(x=50, y=200)
    combobox2.place(x=530, y=200)
    lbl_columnvalue.place(x=50, y=250)
    en_columnvalue.place(x=530, y=250)
    def submit_info():
        comboboxvalue2 = combobox2.get()
        obj_ent.set_column_name(comboboxvalue2)
        accountno = en_accountno.get()
        obj_ent.setaccountno(accountno)
        column_value = en_columnvalue.get()
        obj_ent.set_column_value(column_value)

        comboboxvalue1 = combobox1.get()
        if comboboxvalue1 == "Saving":
            obj_bal = SBal.CSavingAccount()
            obj_bal.m_data_updation(obj_ent)
        elif comboboxvalue1 == "Current":
            obj_bal = CBal.CCurrentAccount()
            obj_bal.m_data_updation(obj_ent)
        elif comboboxvalue1 == "FD":
            obj_bal=FBal.CFDaccount()
            obj_bal.m_data_updation(obj_ent)
        elif comboboxvalue1 == "Recurring":
            obj_bal=RBal.CRecurringAccount()
            obj_bal.m_data_updation(obj_ent)
        messagebox.showinfo(title='Bank Application', message='DATA UPDATED SUCCESSFULLY')

    submit_button = tk.Button(window1, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window1, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_last_window1()], bg="orange", bd=5)
    Home_button = tk.Button(window1, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window1, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window1.destroy, bg="orange", bd=5)
    submit_button.place(x=250, y=300)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    window1.mainloop()
def data_deletion():
    global window1
    window1 = tk.Toplevel()
    window1.title("Bank Application")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window1, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window1, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)

    lbl_accontno = tk.Label(window1, text="Enter the account no.", font=("Arial", 14))
    en_accountno = tk.Entry(window1, font=("Arial", 14))

    lbl_acctype = tk.Label(window1, text='Choose the account type', font=("Arial", 14))
    option3 = ["Saving", "Current", "FD", "Recurring"]
    combobox1 = ttk.Combobox(window1, values=option3, font=("Arial", 14), width=19)
    lbl_acctype.place(x=50, y=150)
    combobox1.place(x=530, y=150)
    lbl_accontno.place(x=50, y=200)
    en_accountno.place(x=530, y=200)

    def submit_info():
        messagebox.askyesnocancel(title='Bank Application', message='Do you really want to delete this data?')
        if messagebox.YES:
            accountno=en_accountno.get()
            obj_ent.setaccountno(accountno)
            if combobox1.get()=="Saving":
                obj_bal=SBal.CSavingAccount()
                obj_bal.m_delete_data(obj_ent)
            elif combobox1.get()=="Current":
                obj_bal=CBal.CCurrentAccount()
                obj_bal.m_delete_data(obj_ent)
            elif combobox1.get()=="FD":
                obj_bal=FBal.CFDaccount()
                obj_bal.m_delete_data(obj_ent)
            elif combobox1.get()=="Recurring":
                obj_bal=RBal.CRecurringAccount()
                obj_bal.m_delete_data(obj_ent)
            messagebox.showinfo(title='Bank Application', message='DATA DELETION SUCCESSFULLY')
        else:
            pass
    submit_button = tk.Button(window1, text='SUBMIT', width=25, font=("Roboto", 15, "bold"),
                            command=submit_info, bg="aquamarine", bd=5)
    Back_button = tk.Button(window1, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_last_window1()], bg="orange", bd=5)
    Home_button = tk.Button(window1, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window1, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=window1.destroy, bg="orange", bd=5)
    submit_button.place(x=250, y=250)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    window1.mainloop()
def Other_services():
    global window
    window = tk.Toplevel()
    window.title("Bank Application")
    logo = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solutions\\logo.ico")
    logo = ImageTk.PhotoImage(logo)
    window.iconphoto(True, logo)
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black",
                             bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    About_user_button = tk.Button(window, text="About User", width=25, font=("Roboto", 15, "bold"),
                    command=lambda: [hide_current_window(window), about_user()], bg="aquamarine", bd=5)
    User_Transaction_button = tk.Button(window, text="Transaction History", width=25, font=("Roboto", 15, "bold"),
                    command=lambda: [hide_current_window(window), user_transaction_History()], bg="aquamarine", bd=5)
    Data_Updation_button = tk.Button(window, text="Data Updation", width=25, font=("Roboto", 15, "bold"),
                    command=lambda: [hide_current_window(window), data_updation()], bg="aquamarine", bd=5)
    Data_Deletion_button = tk.Button(window, text="Data Deletion", width=25, font=("Roboto", 15, "bold"),
                    command=lambda: [hide_current_window(window), data_deletion()], bg="aquamarine", bd=5)
    Exit_button = tk.Button(window, text="EXIT", width=10, font=("Roboto", 15, "bold"), command=window.destroy,
                        bg="orange", bd=5)
    Home_button = tk.Button(window, text="HOME", width=10, font=("Roboto", 15, "bold"),
                    command=lambda: [hide_current_window(window), show_main_window()], bg="orange", bd=5)
    About_user_button.place(x=270, y=100)
    User_Transaction_button.place(x=270, y=150)
    Data_Updation_button.place(x=270, y=200)
    Data_Deletion_button.place(x=270, y=250)
    Home_button.place(x=10, y=450)
    Exit_button.place(x=660, y=450)
    window.mainloop()

# MAIN PAGE
def main_page():
    global main_window
    main_window = tk.Tk()
    main_window.title("Bank Application")
    logo= Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solutions\\logo.ico")
    logo = ImageTk.PhotoImage(logo)
    main_window.iconphoto(True, logo)
    image = Image.open("C:\\Users\\Anmol\\Desktop\\Banking_Solution\\bg.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_bank_name = tk.Label(window, text="ANMOL BANK OF INDIA", width=66, font=("Roboto", 15, "bold"), fg="black", bg="gold", bd=5)
    lbl_bank_name.place(x=0, y=0)
    button1 = tk.Button(window, text="Existing Customer", width=25, font=("Roboto", 15, "bold"), command=lambda: [hide_current_window(main_window), Existing_customer()], bg="aquamarine", bd=5)
    button2 = tk.Button(window, text="New Customer", width=25, font=("Roboto", 15, "bold"), command=lambda: [hide_current_window(main_window), New_customer()], bg="aquamarine", bd=5)
    button3 = tk.Button(window, text="Other Services", width=25, font=("Roboto", 15, "bold"), command=lambda: [hide_current_window(main_window), Other_services()], bg="aquamarine", bd=5)
    button4 = tk.Button(window, text="EXIT", compound="left", width=10, font=("Roboto", 15, "bold"), command=main_window.destroy, bg="orange", bd=5)
    button1.place(x=270, y=150)
    button2.place(x=270, y=220)
    button3.place(x=270, y=290)
    button4.place(x=660, y=450)
    main_window.mainloop()

if __name__=="__main__":
    main_page()