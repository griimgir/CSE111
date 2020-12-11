import sqlite3
from sqlite3 import Error
import PySimpleGUI as gui
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

def selectWeapon(_conn):
    try:
        sql = """select *
                from Classes"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/2.out", "w")
    except Error as e:
        print(e)
    return sample

def selectWeaponRows(_conn):
    try:
        sql = """select *
                from Classes"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        sample = open("output/2.out", "w")
    except Error as e:
        print(e)
    return rows


def main():
    gui.theme('DarkAmber')

    frame_layout = [
        [gui.Button('Ammunition'), gui.Button('Armor Vest'), gui.Button('Backpacks'), gui.Button('Buffs')],
            [gui.Button('Classes'), gui.Button('GearMods'), gui.Button('Health'), gui.Button('Magazines')],
            [gui.Button('NPC Traders'), gui.Button('Sights'), gui.Button('SubClass Health Buffs'), gui.Button('SubClass WeaponModifications')],
            [gui.Button('SubClass Weapons'), gui.Button('SubClass Wearables'), gui.Button('Vital Parts'), gui.Button('Weapons')]
    ]

    layout = [  
        [gui.Text('Escape From Tarkov Battle Buddy')], [gui.Output(size=(100, 50))], [gui.Frame('Interface', frame_layout, title_color='#ffb84d')]
    ]

    # Create the Window
    window = gui.Window('EFT info', layout, default_element_size=(100, 50), resizable=True)

    while True:
        event, value = window.read()
        if event == 'Ammunition':
            print('Printing Ammunition')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Ammunition"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            # print('--------------------------------------------------------')
            # print('')
            # print('')
            # print(str(rows))
            # print('')
            # print('')
            # print('--------------------------------------------------------')
            # print('')
            # print('')
            continue

        if event == 'Armor Vest':
            print('Printing Armor Vest')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Armor_Vest"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')

            continue

        if event == 'Backpacks':
            print('Printing Backpacks')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Backpacks"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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


            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')

            continue

        if event == 'Buffs':
            print('Printing Buffs')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Buffs"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue
        
        if event == 'Classes':
            print('Prionting Classes')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Classes"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue

        if event == 'GearMods':
            print('Printing GearMods')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from GearMods"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            # print('--------------------------------------------------------')
            # print('')
            # print('')
            # print(str(rows))
            # print('')
            # print('')
            # print('--------------------------------------------------------')
            # print('')
            # print('')
            continue

        if event == 'Health':
            print('Printing Health')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Health"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue

        if event == 'Magazines':
            print('Printing Magazines')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Magazines"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue
        
        if event == 'NPC Traders':
            print('Printing NPC Traders')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from NPC_Traders"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue

        if event == 'Sights':
            print('Printing Sights')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Sights"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue

        if event == 'SubClass Health Buffs':
            print('Printing SubClass Health Buffs')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from SubClass_Health_Buffs"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue
        
        if event == 'SubClass WeaponModifications':
            print('Printing SubClass WeaponModifications')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from SubClass_WeaponModifications"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue
        
        if event == 'SubClass Weapons':
            print('Printing SubClass Weapons')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from SubClass_Weapons"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue

        if event == 'SubClass Wearables':
            print('Printing SubClass Wearables')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from SubClass_Wearables"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue

        if event == 'Vital Parts':
            print('Vital Parts')
            database = r"database/eft.sqlite"
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Vital_Parts"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')
            continue
        
        if event == 'Weapons':
            print('Weapons')
            database = r"database/eft.sqlite"
            # conn = openConnection(database)
            conn = sqlite3.connect(database)

            try:
                sql = """select *
                        from Weapons"""

                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
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

            print('--------------------------------------------------------')
            print('')
            print('')
            print(str(rows))
            print('')
            print('')
            print('--------------------------------------------------------')
            print('')
            print('')

            # sample = selectWeapon(conn)
            # rows = selectWeaponRows(conn)
            
            # l = '{:<10} {:>16} {:>23} {:>29} {:>35}'.format('Class', 'Name', 'Firing Mode', 'Fire Rate', 'Caliber')
            # print(l, file=sample)
            # for row in rows:
            #     l = '{:<10} {:>16} {:>23} {:>29} {:>35}'.format(row[0], row[1], row[2], row[4], row[5])
            #     print(l, file=sample)
            # sample.close()
            continue

            #print(value)
        
        if event == gui.WIN_CLOSED: # if user closes window or clicks cancel
            break
    window.close()
main()

# print=gui.Print
# for i in range(100):
#     print(i)

# gui.theme('DarkAmber')   # color
# # inside window
# layout = [  [gui.Text('Tables')],
#             [gui.Text('Search'), gui.InputText()],
#             [gui.Text('Command'), gui.InputText()],
#             [gui.Button('Ok'), gui.Button('Cancel')] ]

# # Create the Window
# window = gui.Window('EFT info', layout)
# # Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#     if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
#         break
#     print('Displaying ', values[0])

# window.close()



        # database = r"database/eft.sqlite"
        # conn = openConnection(database)
        # with conn:


        #     closeConnection(conn, database)
