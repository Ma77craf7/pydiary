import json
from os import system
from tkinter import messagebox
from datetime import date

def graphinterface():
    retry=messagebox.askretrycancel("", "This feature is under development")
    print(retry)
    while retry:
        retry=messagebox.askretrycancel("", "This feature is under development")

def clear():
    try:
        system('cls')
    except:
        system('clear')

def commandline_interface():
    global data

    def older_entries_line():
        global data

        #select year
        i = 1
        for key in data.keys():     #show years
            print(i+" - "+key)
            i+=1
        decision=(input("which year you want to view?"))
        while decision < 1 or decision >i:
            decision=int(input("which year you want to view"))
        year = data[decision-1]

        #select month
        i = 1
        for key in data.keys():     #show months
            print(i+" - "+key)
            i+=1
        decision=(input("which month you want to view?"))
        while decision < 1 or decision >i:
            decision=int(input("which month you want to view"))
        month=year[decision-1]

        #select the day
        i = 1
        for key in data.keys():     #show days
            print(i+" - "+key)
            i+=1
        decision=(input("which day you want to view?"))
        while decision < 1 or decision >i:
            decision=int(input("which day you want to view"))
        day=month[decision-1]

        print(day)

    def addNewEntry():
        clear()
        global data
        today=date.today("%d")
        todayMonth=date.today("%m")
        todayYear=date.today("%y")
        year=data[todayYear]
        month=data[todayMonth]
        check=True
        clear()
        if today in month.keys():
            print("There is already an entry for today, the new entry will be append to the older one")
            old=True
        else:
            old=False
        entry = ""
        while check:
            clear()
            print(entry)
            newline=input()+"\n"
            entry=newline
            clear()
            print(entry)
            check=bool("Do you want to add a new line? 1=yes 0=no")
        clear()
        if old:
            newEntry=month[today]+"\n\n--------------------------------------------------------------------------\n\n"+entry
            month[today]=newEntry
        else:
            month[today]=newEntry

        print("goodBye!")
        exit()


    check = False
    while not check:
        viewOlderEntries=input("do you want view your older entries? Y/n")
        if viewOlderEntries not in "YyNn":
            if viewOlderEntries == "":
                check=True
                view=True
        else:
            if len(viewOlderEntries) == 0:
                check=True
                if viewOlderEntries in "Yy":
                    view=True
                else:
                    view=False
    if view:
        older_entries_line()


    addEntry = input("Do you wanto to add another entry? Y/n")
    check = False
    while not check:
        addEntry=input("do you want view your older entries? Y/n")
        if addEntry not in "YyNn":
            if addEntry == "":
                check=True
                view=True
        else:
            if len(addEntry) == 0:
                check=True
                if addEntry in "Yy":
                    add=True
                else:
                    add=False
    if add:
        addNewEntry()


try:
    file = open("diary.json", "r")
except:
    file= open("diary.json", "x")

data=json.load(file)

gui = messagebox.askquestion("","Do you want a stupid GUI?")
if gui:
    graphinterface()
else:
    commandline_interface()