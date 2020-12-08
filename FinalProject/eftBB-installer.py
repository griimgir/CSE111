import sqlite3
from sqlite3 import Error
import PySimpleGUI as gui
import mysql.connector
import random
import string



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

def selectAmmunition(_conn):
    try:
        sql = """select *
                from Ammuntion"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/ammunition.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectArmorVest(_conn):
    try:
        sql = """select *
                from Armor_Vest"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/armorVest.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29} {:>35} {:>29} {:>29} {:>29} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectBackpacks(_conn):
    try:
        sql = """select *
                from Backpacks"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/Backpacks.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectBuffs(_conn):
    try:
        sql = """select *
                from Buffs"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/buffs.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectClasses(_conn):
    try:
        sql = """select *
                from Classes"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/classes.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectGearMods(_conn):
    try:
        sql = """select *
                from Gear_Mods"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/gearmods.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectHealth(_conn):
    try:
        sql = """select *
                from Health"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/health.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectMagazines(_conn):
    try:
        sql = """select *
                from Magazines"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/magazines.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectNpcTraders(_conn):
    try:
        sql = """select *
                from NPC_Traders"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/npcTraders.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectSubClassHealthBuffs(_conn):
    try:
        sql = """select *
                from SubClass_Health_Buffs"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/scHeakthBuffs.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectSubClassWeaponModifications(_conn):
    try:
        sql = """select *
                from SubClass_WeaponModifications"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/scWeaponModifications.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectSubClassWeapons(_conn):
    try:
        sql = """select *
                from SubClass_Weapons"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/scWeapons.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectSubClassWearables(_conn):
    try:
        sql = """select *
                from SubClass_Wearables"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/scWearables.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

def selectVitalParts(_conn):
    try:
        sql = """select *
                from Vital_Parts"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/vitalParts.txt", "w")
        l = '{:<10} {:>16} {:>23} {:>29}'.format('Class', 'Sub Class Number', 'Caliber', 'Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10} {:>16} {:>23} {:>29}'.format(row[0], row[1], row[2], row[3])
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

    selectArmorVest(conn)
    selectBackpacks(conn)
    selectBuffs(conn)
    selectClasses(conn)
    selectGearMods(conn)
    selectHealth(conn)
    selectMagazines(conn)
    selectNpcTraders(conn)
    # selectSights(conn)
    selectSubClassHealthBuffs(conn)
    selectSubClassWeaponModifications(conn)
    selectSubClassWeapons(conn)
    selectSubClassWearables(conn)
    selectVitalParts(conn)
    selectWeapons(conn)

def main():
    gui.theme('DarkAmber')   # color
    # inside window
    layout = [  [gui.Text('You must install the data pre-requisites for eftBB to work!')],
                [gui.Text('')],
                [gui.Text('Would you like to install data pre-requisites for Escape From Tarkov Battle Buddy?')],
                [gui.Button('Install')] 
                ]

    # Create the Window
    window = gui.Window('EFT Battle Buddy data Installer', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == 'Install':
            install()

        if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        # print('Displaying ', values[0])

    window.close()
main()