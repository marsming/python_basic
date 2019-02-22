import openpyxl

wb = openpyxl.load_workbook('./datas/example.xlsx')
print(wb.sheetnames)
wb['sheet1']


