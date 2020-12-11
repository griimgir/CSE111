import sqlite3
from sqlite3 import Error
import PySimpleGUI as gui
import mysql.connector
import random
import string

def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    # test = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'right', 'nine', 'ten', '11', '12', '13', '15', '15', '15', '15', '15', '15']
    for i in range(1, num_rows):
            data[i] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            # data[i] = [word(), *[insert for i in range(num_cols - 1)]]
    return data

#################################  TABLE UPDATE LOGIC  ####################################################

def createClassHeader():
    header = ['Class', 'Class Number', 'Total']
    return header

# def classesTable(num_rows, num_cols):
#     # data = open('output/classes/')

#     output1 = open('output/classes/class.txt', 'r')
#     o1 = output1.readlines()

#     output2 = open('output/classes/classnumber.txt', 'r')
#     o2 = output2.readlines()

#     output3 = open('output/classes/total.txt', 'r')
#     o3 = output3.readlines()

#     data = [[j for j in range(num_cols)] for i in range(num_rows)]
#     data[0] = [o1[1] for __ in range(num_cols)]
#     i=0
#     for line in range(1, num_rows):
#         data[i] = [o1[i+1], o2[i+1], o3[i+1]]
#         # print(data[i])
    
#     return True

#################################  TABLE UPDATE LOGIC  ####################################################

def clearTable(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [' ' for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [' ', *[' ' for i in range(num_cols - 1)]]
    return data

def classesTable(num_rows, num_cols):
    # data = open('output/classes/')

    output1 = open('output/classes/class.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/classes/classnumber.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/classes/total.txt', 'r')
    o3 = output3.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i+1], o2[i+1], o3[i+1]]
        # print(data[i])
        i = i + 1
    
    return data

def main():
    gui.theme('DarkAmber')

    #--------LOGIC FOR FRAMES--------#

    test = ['ADAR 2-15', 'AK-101', 'AKS-74', 'M4A1', 
            'SA-58', 'MP5', 'MPX', 'SKS'
            ]

    data = make_table(num_rows=15, num_cols=18)
    headings = [str(data[0][x])+'     ' for x in range(len(data[0]))]

    search = [
        [gui.Input(size=(20, 1), enable_events=True, key='-INPUT-') ,gui.Listbox(test, size=(20, 4), enable_events=True, key='-LIST-')]
    ]

    searchInTab = [
        [gui.Input(size=(20, 1), enable_events=True, key='-INPUT-') ,gui.Listbox(test, size=(20, 4), enable_events=True, key='-LIST-')]
    ]

    #--------LOGIC FOR FRAMES--------#



    #---------TABS---------*
    tab_armorVest = [
        [gui.Text("Search"), searchInTab]
    ]
    tab_backpacks = [
        [gui.Text("Search"), searchInTab]
    ]
    tab_weapons = [
        [gui.Text("Search"), searchInTab]
    ]

    #---------TABS---------*


    #---------FRAME LAYOUTS---------#
    frame_layout = [
        [gui.Button('Ammunition'), gui.Button('Armor Vest'), gui.Button('Backpacks'), gui.Button('Buffs')],
            [gui.Button('Classes'), gui.Button('GearMods'), gui.Button('Health'), gui.Button('Magazines')],
            [gui.Button('NPC Traders'), gui.Button('Sights'), gui.Button('SubClass Health Buffs'), gui.Button('SubClass WeaponModifications')],
            [gui.Button('SubClass Weapons'), gui.Button('SubClass Wearables'), gui.Button('Vital Parts'), gui.Button('Weapons')]
    ]

    frame_layout2 = [
        [gui.Table(values=data[1:][:], headings=headings, max_col_width=25,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='This is a table')],
              [gui.Button('New Dataset'), gui.Button('Classes'), gui.Button('Double'), gui.Button('Clear')],[gui.Button('Test 1'), gui.Button('Test 2'), gui.Button('Test 3')]
    ]
    #---------FRAME LAYOUTS---------#

    #-----------WINDOW SETTINGS-----------#

    layout = [  
        [gui.Text('Escape From Tarkov Battle Buddy')], [gui.Output(size=(81, 20)), gui.Frame('Tables', frame_layout2, title_color='#ffb84d'), gui.Output(size=(81, 20))], [gui.Frame('Interface', frame_layout, title_color='#ffb84d'), gui.Frame('Search', search, title_color='#ffb84d')]
    ]

    # Create the Window
    window = gui.Window('EFT info', layout, default_element_size=(80, 20), resizable=True)

    #-----------WINDOW SETTINGS-----------#

    while True:
        event, value = window.read()

        if value['-INPUT-'] != '':                          # if a keystroke entered in search field
            search = value['-INPUT-']
            new_values = [x for x in test if search in x]   # do the filtering
            window['-LIST-'].update(new_values)             # display in the listbox

        else:
            # display original unfiltered list
            window['-LIST-'].update(test)
            # if a list item is chosen
        if event == '-LIST-' and len(value['-LIST-']):
            gui.popup('Selected ', value['-LIST-'])


        
##########################PROTOTYPE BUTTONS###########################################
        
        if event == 'Clear':
            data = clearTable(num_rows=15, num_cols=6)
            window['-TABLE-'].update(values=data)

        if event == 'New Dataset':
            data = make_table(num_rows=15, num_cols=6)
            # headers = createHeader(num_cols=6)
            window['-TABLE-'].update(values=data)
            # window['-TABLE-'].update(headings=headers)

        if event == 'Classes':
            data = classesTable(num_rows=5, num_cols=3)
            # headers = createClassHeader()
            window['-TABLE-'].update(values=data)
            # window['-TABLE-'].update(headings=headings)

        if event == 'Double':
            for i in range(len(data)):
                data.append(data[i])
            window['-TABLE-'].update(values=data)
        
        if event == 'Test 1':
            data = clearTable(num_rows=15, num_cols=6)
            
            data = make_table(num_rows=15, num_cols=6)
            # for i in range(len(data)):
            #     data.append(data[i])
            window['-TABLE-'].update(values=data)

        if event == 'Test 2':
            data = clearTable(num_rows=15, num_cols=6)
            
            data = make_table(num_rows=15, num_cols=6)
            # for i in range(len(data)):
            #     data.append(data[i])
            window['-TABLE-'].update(values=data)

        if event == 'Test 3':
            data = clearTable(num_rows=15, num_cols=6)
            
            data = make_table(num_rows=15, num_cols=6)
            # for i in range(len(data)):
            #     data.append(data[i])
            window['-TABLE-'].update(values=data)

##########################PROTOTYPE BUTTONS###########################################
        

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

# if event == 'Ammunition':
            

        # if event == 'Armor Vest':


        # if event == 'Backpacks':


        # if event == 'Buffs':

        
        # if event == 'Classes':



        # if event == 'GearMods':


        # if event == 'Health':


        # if event == 'Magazines':

        
        # if event == 'NPC Traders':


        # if event == 'Sights':


        # if event == 'SubClass Health Buffs':

        
        # if event == 'SubClass WeaponModifications':

        
        # if event == 'SubClass Weapons':


        # if event == 'SubClass Wearables':


        # if event == 'Vital Parts':

        
        # if event == 'Weapons':
