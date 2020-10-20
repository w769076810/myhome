import xlrd
import os


excel = xlrd.open_workbook("./static_finance_data/基本信息.xlsx")

sheet = excel.sheets()[0]


rows = sheet.nrows
cols = sheet.ncols
arr = []
for i in range(1, 4):
    arr_col = []
    for j in range(cols):
        arr_col.append(sheet.cell_value(i, j))
    arr.append(arr_col)
print(arr)
