import openpyxl

worksheet = openpyxl.load_workbook("C:\\Users\\nikub\\PycharmProjects\\pythonProject5\\testdata\\Book6.xlsx")
sheet=worksheet["shubham"]
parametrize_list = list(sheet.values)[1:]
print(parametrize_list)
