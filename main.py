import csv
import sys
import pandas as pd


def heading():
    f = open("bank.csv", "a", newline='')
    results = pd.read_csv('bank.csv')
    row = len(results)
    # print(row)
    if row > 0:
        print("Already a Heading is there ")
        f.close()
        app()


    else:
        w = csv.writer(f)
        l = [" ACCOUNT NO ", " NAME ", " BALANCE "]
        w.writerow(l)
        f.close()


def data():
    f = open("bank.csv", "a", newline='')
    w = csv.writer(f)
    n = int(input("Enter the number of account holder you want to add : "))
    for x in range(n):
        a = int(input("Enter the acct no : "))
        n = input("Enter the name : ")
        b = int(input("Enter the balance amt. : "))
        l = [a, n, b]
        w.writerow(l)
    f.close()


def display():
    f = open("bank.csv", "r", newline='')
    acct = csv.reader(f)
    for i in acct:
        print(i)
    f.close()
    app()


def app():
    # main program

    print("WELCOME " + name.upper() + " BANK MANAGEMENT SYSTEM")
    print("\n MENU \n")
    print("1-FIELDNAMES (Don't Run Multiple Times just For heading )")
    print("2-Input & Write Data")
    print("3-DISPLAY")
    print("4-EXIT")
    print("\n This App is Developed By Ashish Singh")
    ch = int(input("\nEnter Your Choice : "))
    if ch == 1:
        heading()
    elif ch == 2:
        data()
    elif ch == 3:
        display()
    elif ch == 4:
        print("THANK YOU " + name + " For using This App \n Regards Ashish Singh")
        sys.exit()


while True:
    name = input("Enter Your Name : ")
    app()
