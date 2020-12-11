import tkinter as tk
from tkinter import *
import sqlite3
from sqlite3 import Error
import mysql.connector

def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("opened connection to eft database")
    except Error as e:
        print(e)
    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("closed connection to eft database")
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def selectWeapons(_conn):
    try:
        sql = """select *
                from Weapons"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/weapons.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29} {:>35}'.format('Class', 'Name', 'Firing Mode', 'Fire Rate', 'Caliber')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29} {:>35}'.format(row[0], row[1], row[2], row[4], row[5])
            print(l, file=sample)
        sample.close()
    except Error as e:
        print('--------------------------------------------------------')
        print('')
        print('')
        print(e)
        print('')
        print('')
        print('--------------------------------------------------------')
        print('')
        print('')
    return sample

def selectSights(_conn):
    try:
        sql = """select *
                from Sights"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/sights.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29} {:>35} {:>41} {:>47} {:>53}'.format('Class', 'SC Number', 'Names', 'Recoil', 'Ergonomics', 'Accuracy', 'Range', 'Magnification')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29} {:>37} {:>43} {:>50} {:>56}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            print(l, file=sample)
        sample.close()
    except Error as e:
        print('--------------------------------------------------------')
        print('')
        print('')
        print(e)
        print('')
        print('')
        print('--------------------------------------------------------')
        print('')
        print('')
    return sample

    
def install():
    database = r"database/eft.sqlite"
    # conn = openConnection(database)
    conn = sqlite3.connect(database)

    selectWeapons(conn)
    selectSights(conn)
    print('success')

def main():
    bb = Tk()

    fr1 = Frame(bb)
    fr1.pack(pady=30, padx=20)

    var1 = StringVar()
    
    prompt = Label(fr1, textvariable=var1)
    var1.set('EFT Battle Buddy data Installer, you must install the data pre-requisites for eftBB to work!')
    prompt.grid(row=0, column=2)
    
    btn = Button(fr1, text='Install', command=install)
    btn.grid(row=1, column=2)

    bb.title("Escape From Tarkov Battle Buddy Installer")
    bb.geometry("800x140")
    bb.resizable(False, False)
    bb.mainloop()

main()