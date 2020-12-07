import tkinter as tk
from tkinter import *
import mysql.connector

bb = Tk()

# frm1 = Frame(win)
# frm1.pack(side=tk.LEFT, padx=20)

w1 = LabelFrame(bb, text="EFT information tables")
w2 = LabelFrame(bb, text="Interface")

w1.pack(fill="both", expand="yes", padx=28, pady=10)
w2.pack(fill="both", expand="yes", padx=28, pady=10)

bb.title("Escape From Tarkov battle buddy")
bb.geometry("800x700")
bb.resizable(True, True)
bb.mainloop()
