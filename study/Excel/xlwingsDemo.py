import xlwings as xw

wb = xw.Book('./datas/example.xlsx')
print(wb.sheets['sheet1'])