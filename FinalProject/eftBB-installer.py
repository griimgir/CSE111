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

        s1 = open("output/weapons/scnumber.txt", "w")
        l = '{:<10} '.format('Subclass Number')
        print(l, file=s1)
        for row in rows:
            l = '{:<10} '.format(row[0])
            print(l, file=s1)

        s2 = open("output/weapons/name.txt", "w")
        l = '{:<10} '.format('Name')
        print(l, file=s2)
        for row in rows:
            l = '{:<10} '.format(row[1])
            print(l, file=s2)

        s3 = open("output/weapons/firingmodes.txt", "w")
        l = '{:<10} '.format('Fiiring Modes')
        print(l, file=s3)
        for row in rows:
            l = '{:<10} '.format(row[2])
            print(l, file=s3)

        s4 = open("output/weapons/firerate.txt", "w")
        l = '{:<10} '.format('Fire Rate (RPM)')
        print(l, file=s4)
        for row in rows:
            l = '{:<10} '.format(row[3])
            print(l, file=s4)

        s5 = open("output/weapons/caliber.txt", "w")
        l = '{:<10} '.format('Caliber')
        print(l, file=s5)
        for row in rows:
            l = '{:<10} '.format(row[4])
            print(l, file=s5)
        
        s1.close()
        s2.close()
        s3.close()
        s4.close()
        s5.close()
    except Error as e:
        print(e)
    return True

def selectAmmunition(_conn):
    try:
        sql = """select *
                from Ammunition"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/ammunition/scnumber.txt", "w")
        l = '{}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/ammunition/caliber.txt", "w")
        l = '{}'.format('Caliber')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/ammunition/name.txt", "w")
        l = '{}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample.close()
    except Error as e:
        print(e)
    return True

def selectArmorVest(_conn):
    try:
        sql = """select *
                from 'Armor Vest'"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/armorvest/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)
        
        sample = open("output/armorvest/name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/armorvest/penetration.txt", "w")
        l = '{:<10}'.format('Penetration Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/armorvest/armorzones.txt", "w")
        l = '{:<10}'.format('Armor Zones')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/armorvest/durability.txt", "w")
        l = '{:<10}'.format('Durability')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)

        sample = open("output/armorvest/movementspeed.txt", "w")
        l = '{:<10}'.format('Movement Speed (%)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[5])
            print(l, file=sample)

        sample = open("output/armorvest/turnspeed.txt", "w")
        l = '{:<10}'.format('Turn Speed (%)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[6])
            print(l, file=sample)

        sample = open("output/armorvest/ergo.txt", "w")
        l = '{:<10}'.format('Ergonomics')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[7])
            print(l, file=sample)

        sample.close()
    except Error as e:
        print(e)
    return True

def selectBackpacks(_conn):
    try:
        sql = """select *
                from Backpacks"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/backpacks/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/backpacks/name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)
            
        sample = open("output/backpacks/innergrid.txt", "w")
        l = '{:<10}'.format('Inner Grid')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/backpacks/outergrid.txt", "w")
        l = '{:<10}'.format('Outer Grid')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/backpacks/slots.txt", "w")
        l = '{:<10}'.format('Slots')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)

        sample = open("output/backpacks/storageeff.txt", "w")
        l = '{:<10}'.format('Storage Efficiency')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[5])
            print(l, file=sample)

        sample = open("output/backpacks/weight.txt", "w")
        l = '{:<10}'.format('Weight (kg)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[6])
            print(l, file=sample)

        sample.close()
    except Error as e:
        print(e)
    return True

def selectBuffs(_conn):
    try:
        sql = """select *
                from Buffs"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/buffs/scclass.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/buffs/Name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)
        
        sample = open("output/buffs/type.txt", "w")
        l = '{:<10}'.format('Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/buffs/buffinfo.txt", "w")
        l = '{:<10}'.format('Buff Info')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/buffs/debuffinfo.txt", "w")
        l = '{:<10}'.format('Debuff Info')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)

        sample = open("output/buffs/uses.txt", "w")
        l = '{:<10}'.format('Uses')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[5])
            print(l, file=sample)

        sample.close()
    except Error as e:
        print(e)
    return True

def selectClasses(_conn):
    try:
        sql = """select *
                from Classes"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/classes/class.txt", "w")
        l = '{:<10}'.format('Class')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/classes/total.txt", "w")
        l = '{:<10}'.format('Total')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/classes/classnumber.txt", "w")
        l = '{:<10}'.format('Class Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample.close()
    except Error as e:
        print(e)
    return True

def selectGearMods(_conn):
    try:
        sql = """select *
                from 'Gear Mods'"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/gearmods/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/gearmods/name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/gearmods/recoil.txt", "w")
        l = '{:<10}'.format('Recoil %')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/gearmods/ergo.txt", "w")
        l = '{:<10}'.format('Ergonomics')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)
        

        sample.close()
    except Error as e:
        print(e)
    return True

def selectHealth(_conn):
    try:
        sql = """select *
                from Health"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/health/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/health/name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/health/type.txt", "w")
        l = '{:<10}'.format('Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/health/effects.txt", "w")
        l = '{:<10}'.format('Effects')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/health/useTime.txt", "w")
        l = '{:<10}'.format('Use Time')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)

        sample = open("output/health/uses.txt", "w")
        l = '{:<10}'.format('Uses')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[5])
            print(l, file=sample)

        sample = open("output/health/hpPool.txt", "w")
        l = '{:<10}'.format('HP Pool')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[6])
            print(l, file=sample)

        sample = open("output/health/HPperUse.txt", "w")
        l = '{:<10}'.format('Heal/Use')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[7])
            print(l, file=sample)
        

        sample.close()
    except Error as e:
        print(e)
    return True

def selectMagazines(_conn):
    try:
        sql = """select *
                from Magazines"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/magazines/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/magazines/name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/magazines/recoil.txt", "w")
        l = '{:<10}'.format('Recoil (%)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/magazines/ergonomics.txt", "w")
        l = '{:<10}'.format('Ergonomics')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/magazines/checkSpeed.txt", "w")
        l = '{:<10}'.format('Check Speed')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)

        sample = open("output/magazines/LUspeed.txt", "w")
        l = '{:<10}'.format('Load/Unload Speed')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[5])
            print(l, file=sample)

        sample = open("output/magazines/capacity.txt", "w")
        l = '{:<10}'.format('Capacity')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[6])
            print(l, file=sample)

        sample = open("output/magazines/caliber.txt", "w")
        l = '{:<10}'.format('Caliber')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[7])
            print(l, file=sample)
        

        sample.close()
    except Error as e:
        print(e)
    return True

def selectNpcTraders(_conn):
    try:
        sql = """select *
                from NPC_Traders"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/npc/nickname.txt", "w")
        l = '{:<10}'.format('Nickname')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/npc/fullname.txt", "w")
        l = '{:<10}'.format('Fullname')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/npc/origin.txt", "w")
        l = '{:<10}'.format('Origin')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/npc/location.txt", "w")
        l = '{:<10}'.format('Location')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/npc/tradeables.txt", "w")
        l = '{:<10}'.format('Tradeables')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)

        sample = open("output/npc/currency", "w")
        l = '{:<10}'.format('Currency')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[5])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def selectSights(_conn):
    try:
        sql = """select *
                from Sights"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/sights/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/sights/name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/sights/recoil.txt", "w")
        l = '{:<10}'.format('Recoil (%)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/sights/ergonomics.txt", "w")
        l = '{:<10}'.format('Ergonomics')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/sights/accuracy.txt", "w")
        l = '{:<10}'.format('Accuracy (%)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)

        sample = open("output/sights/range.txt", "w")
        l = '{:<10}'.format('Range')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[5])
            print(l, file=sample)

        sample = open("output/sights/magnification.txt", "w")
        l = '{:<10}'.format('magnification')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[6])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def selectSubClassHealthBuffs(_conn):
    try:
        sql = """select *
                from SubClass_Health_Buffs"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/schb/cnumber.txt", "w")
        l = '{:<10}'.format('Class Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/schb/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/schb/type.txt", "w")
        l = '{:<10}'.format('Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/schb/total.txt", "w")
        l = '{:<10}'.format('Total')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def selectSubClassWeaponModifications(_conn):
    try:
        sql = """select *
                from SubClass_WeaponModifications"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/scwm/cnumber.txt", "w")
        l = '{:<10}'.format('Class Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/scwm/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/scwm/type.txt", "w")
        l = '{:<10}'.format('Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/scwm/total.txt", "w")
        l = '{:<10}'.format('Total')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def selectSubClassWeapons(_conn):
    try:
        sql = """select *
                from SubClass_Weapons"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/scw/cnumber.txt", "w")
        l = '{:<10}'.format('Class Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/scw/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/scw/type.txt", "w")
        l = '{:<10}'.format('Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/scw/total.txt", "w")
        l = '{:<10}'.format('Total')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def selectSubClassWearables(_conn):
    try:
        sql = """select *
                from SubClass_Wearables"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/scwe/cnumber.txt", "w")
        l = '{:<10}'.format('Class Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/scwe/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/scwe/type.txt", "w")
        l = '{:<10}'.format('Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/scwe/total.txt", "w")
        l = '{:<10}'.format('Total')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def selectVitalParts(_conn):
    try:
        sql = """select *
                from 'Vital Parts'"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/vitalParts/scnumber.txt", "w")
        l = '{:<10}'.format('Subclass Number')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/vitalParts/name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/vitalParts/recoil.txt", "w")
        l = '{:<10}'.format('Recoil (%)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/vitalParts/ergonomics.txt", "w")
        l = '{:<10}'.format('Ergonomics')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/vitalParts/accuracy.txt", "w")
        l = '{:<10}'.format('Accuracy (%)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)

        sample = open("output/vitalParts/muzzleVelocity.txt", "w")
        l = '{:<10}'.format('Muzzle Velocity')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[5])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q2(_conn):
    try:
        sql = """select Class, Type as Subclass, SubClass_Weapons.Total as Total
                    from Classes, SubClass_Weapons
                    where Classes.Class_Number = SubClass_Weapons.Class_Number
                    union
                    select Class, Type as Subclass, SubClass_Wearables.Total as Total
                    from Classes, SubClass_Wearables
                    where Classes.Class_Number = SubClass_Wearables.Class_Number
                    union
                    select Class, Type as Subclass, SubClass_WeaponModifications.Total as Total
                    from Classes, SubClass_WeaponModifications
                    where Classes.Class_Number = SubClass_WeaponModifications.Class_Number
                    union
                    select Class, Type as Subclass, SubClass_Health_Buffs.Total as Total
                    from Classes, SubClass_Health_Buffs
                    where Classes.Class_Number = SubClass_Health_Buffs.Class_Number"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q2/class.txt", "w")
        l = '{:<10}'.format('Class')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q2/sc.txt", "w")
        l = '{:<10}'.format('Subclass')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/q2/total.txt", "w")
        l = '{:<10}'.format('total')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        
        sample.close()
    except Error as e:
        print(e)
    return True

def Q3(_conn):
    try:
        sql = """select Name as 'Assault Rifles'
                    from Weapons, SubClass_Weapons
                    where Weapons.SC_Number = SubClass_Weapons.SC_number AND
                            SubClass_Weapons.SC_number = 1"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q3/ar.txt", "w")
        l = '{:<10}'.format('Assault Rifles')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        
        sample.close()
    except Error as e:
        print(e)
    return True

def Q4(_conn):
    try:
        sql = """select Weapons.Name as 'Weapon Name', count(Ammunition.name) as 'Total # of Ammo Types'
                    from Weapons, Ammunition
                    where Weapons.Caliber = Ammunition.Caliber
                    group by Weapons.Name
                    order by 'Total # of Ammo Types' desc"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q4/weaponName.txt", "w")
        l = '{:<10}'.format('Weapon Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q4/totAmmot.txt", "w")
        l = '{:<10}'.format('Total # of Ammo Types')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        
        sample.close()
    except Error as e:
        print(e)
    return True

def Q5(_conn):
    try:
        sql = """select Name as 'Backpack Name', slots as 'Inventory Space'
                    from Backpacks
                    group by Name
                    having slots > 20"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q5/backpack.txt", "w")
        l = '{:<10}'.format('Backpack Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q5/iventoryspace.txt", "w")
        l = '{:<10}'.format('Inventory Space')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q6(_conn):
    try:
        sql = """select Name as 'Armor Name', armorZones as Protects
                    from "Armor Vest"
                    where Protects <> 'Thorax and Stomach'"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q6/armor.txt", "w")
        l = '{:<10}'.format('Armor Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q6/protects.txt", "w")
        l = '{:<10}'.format('Protects')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q7(_conn):
    try:
        sql = """select SubClass_Weapons.Type as 'Weapon Type', avg(FireRate) as 'Average Fire Rate'
                    from SubClass_Weapons, Weapons
                    where SubClass_Weapons.SC_number = Weapons.SC_Number
                    group by SubClass_Weapons.Type"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q7/weapontype.txt", "w")
        l = '{:<10}'.format('Weapon Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q7/avgFR.txt", "w")
        l = '{:<10}'.format('Average Fire Rate (RPM)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q8(_conn):
    try:
        sql = """select Name as 'Health Item', effect as Effect
                    from Health
                    where Type = 'Injury Treatment' AND
                            effect LIKE '%Light Bleeding%'"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q8/healthitem.txt", "w")
        l = '{:<10}'.format('Health Item')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q8/effect.txt", "w")
        l = '{:<10}'.format('Effect')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q9(_conn):
    try:
        sql = """select NPC_Traders.Nickname as Trader, group_concat(Classes.Class, ', ') as Tradeables
                    from NPC_Traders, Classes
                    where Tradeables IN (select npc.Tradeables
                                            from NPC_Traders npc 
                                            where npc.Tradeables LIKE '%1%' OR
                                                    npc.Tradeables LIKE '%2%' OR
                                                    npc.Tradeables LIKE '%3%' OR
                                                    npc.Tradeables LIKE '%4%')
                    group by Trader"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q9/trader.txt", "w")
        l = '{:<10}'.format('Trader')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q9/tradeables.txt", "w")
        l = '{:<10}'.format('Tradeables')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q10(_conn):
    try:
        sql = """select Name as 'Gear Mods', recoil as Recoil
                    from "Gear Mods"
                    where Recoil <> 0
                    order by Recoil asc"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q10/gm.txt", "w")
        l = '{:<10}'.format('Gear Mods')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q10/recoil.txt", "w")
        l = '{:<10}'.format('Recoil')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q11(_conn):
    try:
        sql = """select distinct Name as Attachments, Type
                    from "Gear Mods" gm, SubClass_WeaponModifications
                    where gm.SC_Number = SubClass_WeaponModifications.SC_Number AND
                            Name LIKE '%AK-74%'
                    group by Attachments
                    union 
                    select distinct Name as Attachments, Type
                    from "Vital Parts" vp, SubClass_WeaponModifications
                    where vp.SC_Number = SubClass_WeaponModifications.SC_Number AND
                            Name LIKE '%AK-74%'
                    group by Attachments
                    union
                    select distinct Name as Attachments, Type
                    from Sights, SubClass_WeaponModifications
                    where Sights.SC_Number = SubClass_WeaponModifications.SC_Number AND
                            Name LIKE '%AK-74%'
                    group by Attachments
                    union 
                    select distinct Magazines.Name as Attachments, Type
                    from Magazines, Weapons, SubClass_WeaponModifications
                    where Magazines.Caliber = Weapons.Caliber AND
                            Magazines.SC_Number = SubClass_WeaponModifications.SC_Number AND
                            Weapons.Name = '%AK-74%'
                    group by Attachments"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q11/attachments.txt", "w")
        l = '{:<10}'.format('Attachments')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q11/type.txt", "w")
        l = '{:<10}'.format('Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q12(_conn):
    try:
        sql = """select Name as Magazines, capacity, Caliber
                    from Magazines
                    except 
                    select Name as Magazines, capacity, Caliber
                    from Magazines 
                    where Caliber LIKE '%12x70 mm%'"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q12/magazines.txt", "w")
        l = '{:<10}'.format('Magazines')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q12/capacity.txt", "w")
        l = '{:<10}'.format('Capacity')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/q12/caliber.txt", "w")
        l = '{:<10}'.format('Caliber')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q13(_conn):
    try:
        sql = """Select Name, Type, effect, useTime
                    from Health
                    where useTime between 2 and 3 AND
                            effect LIKE '%Removes:%' AND
                            effect LIKE '%Heavy Bleeding%'"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q13/name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q13/type.txt", "w")
        l = '{:<10}'.format('Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/q13/effect.txt", "w")
        l = '{:<10}'.format('Effect')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/q13/usetime.txt", "w")
        l = '{:<10}'.format('Use Time')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q14(_conn):
    try:
        sql = """select Weapons.Name as Weapons, Magazines.Name as Magazines, Ammunition.Name as Ammunition
                    from ((Weapons
                    inner join Magazines on Weapons.Caliber = Magazines.Caliber)
                    inner join Ammunition on Weapons.Caliber = Ammunition.Caliber) 
                    where Weapons.Caliber = '7.62x25 mm'"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q14/weapons.txt", "w")
        l = '{:<10}'.format('Weapons')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q14/magazines.txt", "w")
        l = '{:<10}'.format('Magazines')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/q14/ammunition.txt", "w")
        l = '{:<10}'.format('Ammunition')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q15(_conn):
    try:
        sql = """select Name as Wearables, Type
                    from "Armor Vest" av, SubClass_Wearables
                    where av.SC_Number = SubClass_Wearables.SC_Number
                    union all
                    select Name as Wearables, Type
                    from Backpacks, SubClass_Wearables
                    where Backpacks.SC_Number = SubClass_Wearables.SC_Number"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q15/wearables.txt", "w")
        l = '{:<10}'.format('Wearables')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q15/type.txt", "w")
        l = '{:<10}'.format('Type')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q16(_conn):
    try:
        sql = """select Name as 'Armor Vest', penType as 'Pen Type', armorZones as 'Armor Zones', max(Durability) as Durability,
                            movementspeed as 'Movement Speed', turnSpeed as 'Turn Speed', ergonomics as Ergonomics
                    from "Armor Vest"
                    union 
                    select Name as 'Armor Vest', penType as 'Pen Type', armorZones as 'Armor Zones', min(Durability) as Durability,
                            movementspeed as 'Movement Speed', turnSpeed as 'Turn Speed', ergonomics as Ergonomics
                    from 'Armor Vest'"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q16/name.txt", "w")
        l = '{:<10}'.format('Armor Vest')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q16/pentype.txt", "w")
        l = '{:<10}'.format('PenType')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/q16/armzones.txt", "w")
        l = '{:<10}'.format('Armor Zones')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/q16/durability.txt", "w")
        l = '{:<10}'.format('Durabilty')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/q16/movespeed.txt", "w")
        l = '{:<10}'.format('Movement Speed')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)

        sample = open("output/q16/turnspeed.txt", "w")
        l = '{:<10}'.format('Turn Speed')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[5])
            print(l, file=sample)

        sample = open("output/q16/ergo.txt", "w")
        l = '{:<10}'.format('Ergonomics')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[6])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q17(_conn):
    try:
        sql = """select avg(s1.range) as 'Average Range: Magnified Sights', avg(s2.range) as 'Average Range: non-Magnified Sights'
                    from Sights s1, Sights s2 
                    where s1.magnification <> 0 AND
                            s2.magnification = 0"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q17/avgrangem.txt", "w")
        l = '{:<10}'.format('Average Range: Magnified Sights')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q17/avgrangenm.txt", "w")
        l = '{:<10}'.format('Average Range: non-Magnified Sights')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q18(_conn):
    try:
        sql = """select Name, recoil as Recoil, ergonomics as Ergonomics, accuracy as Accuracy, muzzleVelocity as 'Muzzle Velocity'
                    from "Vital Parts" v1
                    where v1.muzzleVelocity <> 0 AND
                            v1.muzzleVelocity > (select avg(v2.muzzleVelocity)
                                                from "Vital Parts" v2
                                                where v2.muzzleVelocity <> 0)
                    order by v1.muzzleVelocity desc"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q18/name.txt", "w")
        l = '{:<10}'.format('Name')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q18/recoil.txt", "w")
        l = '{:<10}'.format('Recoil')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/q18/ergo.txt", "w")
        l = '{:<10}'.format('Ergonomics')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/q18/acc.txt", "w")
        l = '{:<10}'.format('Accuracy')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/q18/muzzlev.txt", "w")
        l = '{:<10}'.format('Muzzle velocity')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q19(_conn):
    try:
        sql = """select distinct Weapons.Name as Weapon, group_concat(gm.Name, ', ') as 'Gear Mods', group_concat(vp.Name, ', ') as 'Vital Parts', group_concat(Sights.Name, ', ') as Sights, group_concat(Magazines.name, ', ') as Magazines
                    from SubClass_Weapons scw, Weapons, "Gear Mods" gm , "Vital Parts" vp, Sights, Magazines
                    where scw.SC_Number = Weapons.SC_Number AND 
                            Weapons.Caliber = Magazines.Caliber AND 
                            Weapons.SC_Number = 2 AND
                            gm.Name IN (select distinct gm2.Name
                                        from "Gear Mods" gm2
                                        where gm2.Name LIKE '%AS VAL%' OR
                                                gm2.Name LIKE '%OP-SKS%' OR
                                                gm2.Name LIKE '%SKS%' OR
                                                gm2.Name LIKE '%Vepr Hunter/VP0-101%') AND
                            vp.Name IN (select distinct vp2.Name
                                        from "Vital Parts" vp2
                                        where vp2.Name LIKE '%AS VAL%' OR
                                                vp2.Name LIKE '%OP-SKS%' OR
                                                vp2.Name LIKE '%SKS%' OR
                                                vp2.Name LIKE '%Vepr Hunter/VP0-101%') AND
                            Sights.Name IN (select distinct s2.Name
                                        from Sights s2
                                        where s2.Name LIKE '%AS VAL%' OR
                                                s2.Name LIKE '%OP-SKS%' OR
                                                s2.Name LIKE '%SKS%' OR
                                                s2.Name LIKE '%Vepr Hunter/VP0-101%')
                    group by Weapon"""

        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q19/weapon.txt", "w")
        l = '{:<10}'.format('Weapon')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q19/gm.txt", "w")
        l = '{:<10}'.format('Gear Mods')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)

        sample = open("output/q19/vp.txt", "w")
        l = '{:<10}'.format('Vital Parts')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[2])
            print(l, file=sample)

        sample = open("output/q19/sights.txt", "w")
        l = '{:<10}'.format('Sights')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[3])
            print(l, file=sample)

        sample = open("output/q19/mags.txt", "w")
        l = '{:<10}'.format('Magazines')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[4])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def Q20(_conn):
    try:
        sql = """select Name as Weapon, FireRate as 'Fire Rate'
                    from Weapons
                    where FiringModes = 'Single'
                    order by FireRate desc"""

        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        sample = open("output/q20/weapon.txt", "w")
        l = '{:<10}'.format('Wepaon')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[0])
            print(l, file=sample)

        sample = open("output/q20/fr.txt", "w")
        l = '{:<10}'.format('Fire Rate (RPM)')
        print(l, file=sample)

        for row in rows:
            l = '{:<10}'.format(row[1])
            print(l, file=sample)


        sample.close()
    except Error as e:
        print(e)
    return True

def install():
    database = r"database/eft.sqlite"
    # conn = openConnection(database)
    conn = sqlite3.connect(database)

    selectWeapons(conn)
    selectAmmunition(conn)
    selectArmorVest(conn)
    selectBackpacks(conn)
    selectBuffs(conn)
    selectClasses(conn)
    selectGearMods(conn)
    selectHealth(conn)
    selectMagazines(conn)
    selectNpcTraders(conn)
    selectSights(conn)
    selectSubClassHealthBuffs(conn)
    selectSubClassWeaponModifications(conn)
    selectSubClassWeapons(conn)
    selectSubClassWearables(conn)
    selectVitalParts(conn)
    Q2(conn)
    Q3(conn)
    Q4(conn)
    Q5(conn)
    Q6(conn)
    Q7(conn)
    Q8(conn)
    Q9(conn)
    Q10(conn)
    Q11(conn)
    Q12(conn)
    Q13(conn)
    Q14(conn)
    Q15(conn)
    Q16(conn)
    Q17(conn)
    Q18(conn)
    Q19(conn)
    Q20(conn)

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