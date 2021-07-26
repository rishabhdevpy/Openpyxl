import openpyxl as op
wb = op.load_workbook(input("Enter the path to excel sheet : "))
page = input("Enter the page you want to make changes to : ")
page = wb[page]
o = input("Press 1 to insert columns, 0 for inserting rows : ")
m = int(input("Enter the number at which insertions have to be made : "))
n = int(input("Enter the number of insertions : "))
if o == "1":
    page.insert_cols(m, n)
else:
    page.insert_rows(m, n)
wb.save("/Users/rishabh.kapoor/Desktop/Modified.xlsx")