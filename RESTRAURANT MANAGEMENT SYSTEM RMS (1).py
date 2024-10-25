#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def order_button():
    class RMS:
        #RMS(RESTRAURANT MANAGEMENT SYSTEM)
        def __init__(self,restraurant_name,restraurant_menu):
            self.user_bill=0
            self.user_order=' '
            self.user_pay=0
            self.menu=restraurant_menu
            self.rest_name=restraurant_name
        def welcome_user(self):
            #WELCOME USER
            print('WELCOME TO',self.rest_name)
        def display_menu(self):
            #DISPLAY MENU
            for i in self.menu:
                print(i.title(),self.menu[i])
        def take_order(self):
            #TAKE ORDER
            self.user_order=input('PLEASE ENTER YOUR ORDER HERE')
        def prepare_order(self):
            import time
            print('PREPARING YOUR',self.user_order.title())
            time.sleep(0.5)
            self.user_bill=self.user_bill+self.menu[self.user_order]
        def serve_order(self):
            #serve order
            print('YOUR ORDER IS READY')
            print('PLEASE ENJOY YOUR',self.user_order.title())
        def display_bill(self):
            #DISPLAY BILL
            print('YOUR TOTAL BILL',self.user_bill)
        def verify_payment(self):
            #VERIFY PAYMENT
            self.user_pay=int(input('PLEASE PAY YOUR BILL HERE'))
            while self.user_pay<self.user_bill:
                print('INVALID PAYMENT')
                self.user_bill=self.use_bill-self.user_pay
                print('PLEASE PAY REMAINING',self.user_bill)
                self.user_pay=int(input('PLEASE PAY YOUR BILL HERE'))
            if self.user_pay>self.user_bill:
                print('PAYMENT SUCCESSFUL')
                print('HERE IS YOUR CHANGE',self.user_pay-self.user_bill)
            else:
                pass
        def thank_user(self):
            #THANK USER
            print('THANK YOU FOR VISITING',self.rest_name)
        def order_process(self):
            self.display_menu()
            self.take_order()
            if self.user_order.lower() in self.menu:
                self.prepare_order()
                self.serve_order()
                self.user_rep=input('DO YOU WANT TO ORDER AGAIN?')
                while self.user_rep.lower()=='YES':
                    self.repeat_order()
                    self.user_rep=input('DO YOU WANT TO ORDER AGAIN?')
    
                self.display_bill()
                self.verify_payment()
                self.thank_user()
            else:
                print('INVALID ORDER')
                self.repeat_order()
    
    rn='Moonlight Cafe'
    rm={'frappe':200,'cold coffee':100,'drip coffee':150,'chai':50}
    moonlight_cafe=RMS(rn,rm)
    
    moonlight_cafe.welcome_user()
    moonlight_cafe.order_process()


#import library
import tkinter as tk

#Create window
window=tk.Tk()

#change title of window
window.title('Moonlight Cafe')

#change window size
window.geometry('400x400')


tk.Label(window,text='WELCOME TO ',font=('Helvetica',9)).place(x=170,y=5)
tk.Label(window,text='Moonlight Cafe',font=('Helvetica',19)).place(x=120,y=20)
tk.Label(window,text='____________________',font=('Helvetica',9)).place(x=102,y=52)

tk.Button(window,text='Order',width=18,command=order_button).place(x=125,y=100)


#DISPLAY WINDOW
window.mainloop()


# In[ ]:




