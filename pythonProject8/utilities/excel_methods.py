import openpyxl
worksheet=openpyxl.load_workbook("../testdata/Book6.xlsx")
name=worksheet.sheetnames

sheet=worksheet["ppp"]
a_list=list(sheet.values)
b_list=list(sheet.values)[1:]
print(b_list)

