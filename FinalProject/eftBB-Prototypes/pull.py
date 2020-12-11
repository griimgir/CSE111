# import xlrd

# loc = ("file destination")
 
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
 
# # For row 0 and column 0 example
# print(sheet.cell_value(0, 0))


# Python code to 
# demonstrate readlines() 
  
L = ["Geeks\n", "for\n", "Geeks\n"] 
  
# writing to file 
file1 = open('myfile.txt', 'w') 
file1.writelines(L) 
file1.close() 
  
# Using readlines() 
file1 = open('myfile.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    print("Line{}: {}".format(count, line.strip())) 
