# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:28:12 2023

@author: HP

check balc
with draw
deposiy cash
deposit check
"""
import time
import random
import dbm
import os.path

def switch(lang,ac_bal):
    if lang == 1:
        print("Your account balance is",ac_bal)

    elif lang == 2:
        while True:
            try:
                withdraw=int(input("Input the amount you want to withdraw "))
                ac_bal=ac_bal-withdraw
                break
            except:
                print("Wrong input")

    elif lang == 3:
        while True:
            try:
                cash_d=int(input("Insert the cash amount to be deposit "))
                print("validating your cash")
                print("PLEASE WAIT")
                time.sleep(random.randint(7, 27))
                print("Your cash is valid\n")
                print(cash_d, "is been deposited")
                ac_bal=ac_bal+cash_d
                break
            except:
                print("Wrong input")
    elif lang==4:
        while True:
            try:
                check_d=int(input("Input the amount on your check to deposit"))
                print("validating your check")
                print("PLEASE WAIT")
                time.sleep(random.randint(7,15))
                print("Your check has been approved")
                print(check_d, "is been deposited")
                ac_bal=ac_bal+check_d
                break
            except:
                print("Wrong input")
    else:
        print("Input not between 1 and 4")

    return ac_bal


if not os.path.exists('money.dat'):
    db= dbm.open("money","c")
    db['balance']='10000'
else:
    db = dbm.open('Money', 'w')



while True:
    print("welcome to ATM")
    option =input("MENU\nPRESS 1: TO CHECK BALANCE\nPRESS 2: TO WITHDRAW CASH\nPRESS 3: TO DEPOSIT CASH\nPRESS 4: TO DEPOSIT CHECK\n")
    bal=int(db['balance'])
    ac_bal=switch(int(option),bal)
    db['balance']=str(ac_bal)
    c=input("Do you want to continue Y for yes or N for no ")
    if "N" in c:
        db.close()
        break

