import sqlite3
from sqlite3 import Error
import PySimpleGUI as gui
import mysql.connector

database = r"database/eft.sqlite"
conn = openConnection(database)
    with conn:

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