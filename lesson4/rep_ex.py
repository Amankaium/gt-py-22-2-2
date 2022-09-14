from openpyxl import load_workbook
from openpyxl.cell.cell import Cell


book = load_workbook("python_22.xlsx")
page = book["ДЗ 2 мес"]
lst = page["C3:C13"]
marks = []

for row in lst:
    cell = row[0]
    value = cell.value
    if value is not None:
        mark = value
    else:
        mark = 0
    marks.append(mark)

print("AVG: ", sum(marks) / len(marks))




