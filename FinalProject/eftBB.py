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

def clearTable(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [' ' for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [' ', *[' ' for i in range(num_cols - 1)]]
    return data


#################################  TABLE UPDATE LOGIC  ####################################################
def ammunitionTable(num_rows, num_cols):

    output1 = open('output/ammunition/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/ammunition/caliber.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/ammunition/name.txt', 'r')
    o3 = output3.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i]]
        # print(data[i])
        i = i + 1
    
    return data

def armorTable(num_rows, num_cols):

    output1 = open('output/armorvest/armorzones.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/armorvest/durability.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/armorvest/ergo.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/armorvest/movementspeed.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/armorvest/name.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/armorvest/penetration.txt', 'r')
    o6 = output6.readlines()

    output7 = open('output/armorvest/scnumber.txt', 'r')
    o7 = output7.readlines()

    output8 = open('output/armorvest/turnspeed.txt', 'r')
    o8 = output8.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i], o6[i], o7[i], o8[i]]
        # print(data[i])
        i = i + 1
    return data

def backpacksTable(num_rows, num_cols):

    output1 = open('output/backpacks/innergrid.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/backpacks/name.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/backpacks/outergrid.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/backpacks/scnumber.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/backpacks/slots.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/backpacks/storageeff.txt', 'r')
    o6 = output6.readlines()

    output7 = open('output/backpacks/weight.txt', 'r')
    o7 = output7.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i], o6[i], o7[i]]
        # print(data[i])
        i = i + 1
    return data

def buffsTable(num_rows, num_cols):

    output1 = open('output/buffs/scclass.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/buffs/Name.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/buffs/type.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/buffs/buffinfo.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/buffs/debuffinfo.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/buffs/uses.txt', 'r')
    o6 = output6.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i]]
        # print(data[i])
        i = i + 1
    return data

def classesTable(num_rows, num_cols):

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
        data[i] = [o1[i], o2[i], o3[i]]
        # print(data[i])
        i = i + 1
    return data

def gearmodsTable(num_rows, num_cols):

    output1 = open('output/gearmods/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/gearmods/name.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/gearmods/recoil.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/gearmods/ergo.txt', 'r')
    o4 = output4.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i]]
        # print(data[i])
        i = i + 1
    return data

def healthTable(num_rows, num_cols):

    output1 = open('output/health/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/health/name.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/health/type.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/health/effects.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/health/useTime.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/health/uses.txt', 'r')
    o6 = output6.readlines()

    output7 = open('output/health/hpPool.txt', 'r')
    o7 = output7.readlines()

    output8 = open('output/health/HPperUse.txt', 'r')
    o8 = output8.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i], o6[i], o7[i], o8[i]]
        # print(data[i])
        i = i + 1
    return data

def magazinesTable(num_rows, num_cols):

    output1 = open('output/magazines/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/magazines/name.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/magazines/caliber.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/magazines/capacity.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/magazines/recoil.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/magazines/checkSpeed.txt', 'r')
    o6 = output6.readlines()

    output7 = open('output/magazines/ergonomics.txt', 'r')
    o7 = output7.readlines()

    output8 = open('output/magazines/LUspeed.txt', 'r')
    o8 = output8.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i], o6[i], o7[i], o8[i]]
        # print(data[i])
        i = i + 1
    return data

def npcTable(num_rows, num_cols):

    output1 = open('output/npc/fullname.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/npc/nickname.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/npc/currency', 'r')
    o3 = output3.readlines()

    output4 = open('output/npc/tradeables.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/npc/location.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/npc/origin.txt', 'r')
    o6 = output6.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i], o6[i]]
        # print(data[i])
        i = i + 1
    return data

def sightsTable(num_rows, num_cols):

    output1 = open('output/sights/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/sights/name.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/sights/magnification.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/sights/accuracy.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/sights/range.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/sights/recoil.txt', 'r')
    o6 = output6.readlines()

    output7 = open('output/sights/ergonomics.txt', 'r')
    o7 = output7.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i], o6[i], o7[i]]
        # print(data[i])
        i = i + 1
    return data

def schbTable(num_rows, num_cols):

    output1 = open('output/schb/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/schb/type.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/schb/cnumber.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/schb/total.txt', 'r')
    o4 = output4.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i]]
        # print(data[i])
        i = i + 1
    return data

def scwmTable(num_rows, num_cols):

    output1 = open('output/scwm/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/scwm/cnumber.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/scwm/total.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/scwm/type.txt', 'r')
    o4 = output4.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i]]
        # print(data[i])
        i = i + 1
    return data

def scwTable(num_rows, num_cols):

    output1 = open('output/scw/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/scw/cnumber.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/scw/total.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/scw/type.txt', 'r')
    o4 = output4.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i]]
        # print(data[i])
        i = i + 1
    return data

def scweTable(num_rows, num_cols):

    output1 = open('output/scwe/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/scwe/cnumber.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/scwe/total.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/scwe/type.txt', 'r')
    o4 = output4.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i]]
        # print(data[i])
        i = i + 1
    return data

def vitalpartsTable(num_rows, num_cols):

    output1 = open('output/vitalParts/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/vitalParts/name.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/vitalParts/recoil.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/vitalParts/muzzleVelocity.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/vitalParts/ergonomics.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/vitalParts/accuracy.txt', 'r')
    o6 = output6.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i], o6[i]]
        # print(data[i])
        i = i + 1
    return data

def weaponsTable(num_rows, num_cols):

    output1 = open('output/weapons/scnumber.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/weapons/name.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/weapons/caliber.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/weapons/firerate.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/weapons/firingmodes.txt', 'r')
    o5 = output5.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i]]
        # print(data[i])
        i = i + 1
    return data

#################################  END OF TABLE UPDATE LOGIC  ####################################################


def q2Table(num_rows, num_cols):

    output1 = open('output/q2/sc.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q2/class.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/q2/total.txt', 'r')
    o3 = output3.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i]]
        # print(data[i])
        i = i + 1
    return data

def q3Table(num_rows, num_cols):

    output1 = open('output/q3/ar.txt', 'r')
    o1 = output1.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i]]
        # print(data[i])
        i = i + 1
    return data

def q4Table(num_rows, num_cols):

    output1 = open('output/q4/weaponName.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q4/totAmmot.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

def q5Table(num_rows, num_cols):

    output1 = open('output/q5/backpack.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q5/iventoryspace.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

def q6Table(num_rows, num_cols):

    output1 = open('output/q6/armor.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q6/protects.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

def q7Table(num_rows, num_cols):

    output1 = open('output/q7/weapontype.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q7/avgFR.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data
    
def q8Table(num_rows, num_cols):

    output1 = open('output/q8/healthitem.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q8/effect.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

def q9Table(num_rows, num_cols):

    output1 = open('output/q9/trader.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q9/tradeables.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

def q10Table(num_rows, num_cols):

    output1 = open('output/q10/gm.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q10/recoil.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

def q11Table(num_rows, num_cols):

    output1 = open('output/q11/attachments.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q11/type.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

    
def q12Table(num_rows, num_cols):

    output1 = open('output/q12/magazines.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q12/capacity.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/q12/caliber.txt', 'r')
    o3 = output3.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i]]
        # print(data[i])
        i = i + 1
    return data

def q13Table(num_rows, num_cols):

    output1 = open('output/q13/name.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q13/type.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/q13/effect.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/q13/usetime.txt', 'r')
    o4 = output4.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i]]
        # print(data[i])
        i = i + 1
    return data

def q14Table(num_rows, num_cols):

    output1 = open('output/q14/weapons.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q14/magazines.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/q14/ammunition.txt', 'r')
    o3 = output3.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i]]
        # print(data[i])
        i = i + 1
    return data

def q15Table(num_rows, num_cols):

    output1 = open('output/q15/wearables.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q15/type.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

def q16Table(num_rows, num_cols):

    output1 = open('output/q16/name.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q16/pentype.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/q16/armzones.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/q16/durability.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/q16/movespeed.txt', 'r')
    o5 = output5.readlines()

    output6 = open('output/q16/turnspeed.txt', 'r')
    o6 = output6.readlines()

    output7 = open('output/q16/ergo.txt', 'r')
    o7 = output7.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i], o6[i], o7[i]]
        # print(data[i])
        i = i + 1
    return data

def q17Table(num_rows, num_cols):

    output1 = open('output/q17/avgrangem.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q17/avgrangenm.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

def q18Table(num_rows, num_cols):

    output1 = open('output/q18/name.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q18/recoil.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/q18/ergo.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/q18/acc.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/q18/muzzlev.txt', 'r')
    o5 = output5.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i]]
        # print(data[i])
        i = i + 1
    return data

def q19Table(num_rows, num_cols):

    output1 = open('output/q19/weapon.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q19/gm.txt', 'r')
    o2 = output2.readlines()

    output3 = open('output/q19/vp.txt', 'r')
    o3 = output3.readlines()

    output4 = open('output/q19/sights.txt', 'r')
    o4 = output4.readlines()

    output5 = open('output/q19/mags.txt', 'r')
    o5 = output5.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i], o3[i], o4[i], o5[i]]
        # print(data[i])
        i = i + 1
    return data

def q20Table(num_rows, num_cols):

    output1 = open('output/q20/weapon.txt', 'r')
    o1 = output1.readlines()

    output2 = open('output/q20/fr.txt', 'r')
    o2 = output2.readlines()

    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [o1[1] for __ in range(num_cols)]
    i=0
    for line in range(1, num_rows):
        data[i] = [o1[i], o2[i]]
        # print(data[i])
        i = i + 1
    return data

#################################  END OF QUARIES LOGIC ################################################################## 











def main():
    gui.theme('DarkBlue')

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
            [gui.Button('Classes'), gui.Button('Gear Mods'), gui.Button('Health'), gui.Button('Magazines')],
            [gui.Button('NPC Traders'), gui.Button('Sights'), gui.Button('Subclass Health Buffs'), gui.Button('Subclass Weapon Modifications')],
            [gui.Button('Subclass Weapons'), gui.Button('Subclass Wearables'), gui.Button('Vital Parts'), gui.Button('Weapons')],
            [gui.Text(' ')],
            [gui.Button('Clear')]
    ]

    frame_quarry = [
        [gui.Button('Q1'), gui.Button('Q2'), gui.Button('Q3'), gui.Button('Q4')],
            [gui.Button('Q5'), gui.Button('Q6'), gui.Button('Q7'), gui.Button('Q8')],
            [gui.Button('Q9'), gui.Button('Q10'), gui.Button('Q11'), gui.Button('Q12')],
            [gui.Button('Q13'), gui.Button('Q14'), gui.Button('Q15'), gui.Button('Q16')],
            [gui.Button('Q17'), gui.Button('Q18'), gui.Button('Q19'), gui.Button('Q20')],
            [gui.Text(' ')],
            [gui.Button('Clear')]
    ]

    frame_layout2 = [
        [gui.Table(values=data[1:][:], headings=headings, max_col_width=25,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='#000000',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='This is a table')],
    ]
    #---------FRAME LAYOUTS---------#

    #-----------WINDOW SETTINGS-----------#

    layout = [  
        [gui.Text('Escape From Tarkov Battle Buddy')], [gui.Frame('Tables', frame_layout2, title_color='#000000')], [gui.Frame('Interface', frame_layout, title_color='#ffb84d'), gui.Frame('Search', search, title_color='#ffb84d'),
        gui.Frame('Quarry Interface', frame_quarry, title_color='#ffb84d')]
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

#-------------------------SELECT BUTTONS-------------------------------------#
        if event == 'Ammunition':
            data = ammunitionTable(num_rows=204, num_cols=3)
            window['-TABLE-'].update(values=data)
        
        if event == 'Armor Vest':
            data = armorTable(num_rows=24, num_cols=8)
            window['-TABLE-'].update(values=data)
        
        if event == 'Backpacks':
            data = backpacksTable(num_rows=23, num_cols=7)
            window['-TABLE-'].update(values=data)

        if event == 'Buffs':
            data = buffsTable(num_rows=15, num_cols=6)
            window['-TABLE-'].update(values=data)

        if event == 'Classes':
            data = classesTable(num_rows=6, num_cols=3)
            window['-TABLE-'].update(values=data)

        if event == 'Gear Mods':
            data = gearmodsTable(num_rows=268, num_cols=4)
            window['-TABLE-'].update(values=data)

        if event == 'Health':
            data = healthTable(num_rows=21, num_cols=8)
            window['-TABLE-'].update(values=data)

        if event == 'Magazines':
            data = magazinesTable(num_rows=136, num_cols=8)
            window['-TABLE-'].update(values=data)

        if event == 'NPC Traders':
            data = npcTable(num_rows=10, num_cols=6)
            window['-TABLE-'].update(values=data)

        if event == 'Sights':
            data = sightsTable(num_rows=126, num_cols=7)
            window['-TABLE-'].update(values=data)

        if event == 'Subclass Health Buffs':
            data = schbTable(num_rows=4, num_cols=4)
            window['-TABLE-'].update(values=data)

        if event == 'Subclass Weapon Modifications':
            data = scwmTable(num_rows=18, num_cols=3)
            window['-TABLE-'].update(values=data)

        if event == 'Subclass Weapons':
            data = scwTable(num_rows=11, num_cols=4)
            window['-TABLE-'].update(values=data)

        if event == 'Subclass Wearables':
            data = scweTable(num_rows=4, num_cols=4)
            window['-TABLE-'].update(values=data)

        if event == 'Vital Parts':
            data = vitalpartsTable(num_rows=329, num_cols=6)
            window['-TABLE-'].update(values=data)

        if event == 'Weapons':
            data = weaponsTable(num_rows=85, num_cols=5)
            window['-TABLE-'].update(values=data)

        if event == 'Clear':
            data = clearTable(num_rows=15, num_cols=6)
            window['-TABLE-'].update(values=data)

#-------------------------SELECT BUTTONS-------------------------------------#


#--------------------------Quarry LOGICS-----------------------------------#
        if event == 'Q2':
            data = q2Table(num_rows=31, num_cols=3)
            window['-TABLE-'].update(values=data)

        if event == 'Q3':
            data = q3Table(num_rows=30, num_cols=1)
            window['-TABLE-'].update(values=data)

        if event == 'Q4':
            data = q4Table(num_rows=80, num_cols=2)
            window['-TABLE-'].update(values=data)

        if event == 'Q5':
            data = q5Table(num_rows=13, num_cols=2)
            window['-TABLE-'].update(values=data)
        
        if event == 'Q6':
            data = q6Table(num_rows=8, num_cols=2)
            window['-TABLE-'].update(values=data)

        if event == 'Q7':
            data = q7Table(num_rows=11, num_cols=2)
            window['-TABLE-'].update(values=data)

        if event == 'Q8':
            data = q8Table(num_rows=4, num_cols=2)
            window['-TABLE-'].update(values=data)
            
        if event == 'Q9':
            data = q9Table(num_rows=10, num_cols=2)
            window['-TABLE-'].update(values=data)

        if event == 'Q10':
            data = q10Table(num_rows=123, num_cols=2)
            window['-TABLE-'].update(values=data)

        if event == 'Q11':
            data = q11Table(num_rows=18, num_cols=2)
            window['-TABLE-'].update(values=data)

        if event == 'Q12':
            data = q12Table(num_rows=123, num_cols=3)
            window['-TABLE-'].update(values=data)

        if event == 'Q13':
            data = q13Table(num_rows=4, num_cols=4)
            window['-TABLE-'].update(values=data)

        if event == 'Q14':
            data = q14Table(num_rows=65, num_cols=3)
            window['-TABLE-'].update(values=data)

        if event == 'Q15':
            data = q15Table(num_rows=45, num_cols=2)
            window['-TABLE-'].update(values=data)

        if event == 'Q16':
            data = q16Table(num_rows=4, num_cols=7)
            window['-TABLE-'].update(values=data)

        if event == 'Q17':
            data = q17Table(num_rows=3, num_cols=3)
            window['-TABLE-'].update(values=data)

        if event == 'Q18':
            data = q18Table(num_rows=32, num_cols=5)
            window['-TABLE-'].update(values=data)

        if event == 'Q19':
            data = q19Table(num_rows=6, num_cols=5)
            window['-TABLE-'].update(values=data)

        if event == 'Q20':
            data = q20Table(num_rows=31, num_cols=2)
            window['-TABLE-'].update(values=data)

#--------------------------Quarry LOGICS-----------------------------------#






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







        
        # if event == 'New Dataset':
        #     data = make_table(num_rows=15, num_cols=6)
        #     # headers = createHeader(num_cols=6)
        #     window['-TABLE-'].update(values=data)
        #     # window['-TABLE-'].update(headings=headers)


        # if event == 'Double':
        #     for i in range(len(data)):
        #         data.append(data[i])
        #     window['-TABLE-'].update(values=data)
        
        # if event == 'Test 1':
        #     data = clearTable(num_rows=15, num_cols=6)
            
        #     data = make_table(num_rows=15, num_cols=6)
        #     # for i in range(len(data)):
        #     #     data.append(data[i])
        #     window['-TABLE-'].update(values=data)

        # if event == 'Test 2':
        #     data = clearTable(num_rows=15, num_cols=6)
            
        #     data = make_table(num_rows=15, num_cols=6)
        #     # for i in range(len(data)):
        #     #     data.append(data[i])
        #     window['-TABLE-'].update(values=data)

        # if event == 'Test 3':
        #     data = clearTable(num_rows=15, num_cols=6)
            
        #     data = make_table(num_rows=15, num_cols=6)
        #     # for i in range(len(data)):
        #     #     data.append(data[i])
        #     window['-TABLE-'].update(values=data)
