# import requests
#
# response = requests.get("https://euler.jakumo.org/problems/view/3.html")
# print(response.text)

from openpyxl import load_workbook

wb = load_workbook("info.xlsx")
page = wb["Лист1"]
page["F3"] = "ранен"
page["E6"] = "убит"
wb.save("info.xlsx")

# print(page["A1"].value)
# print(page["B1"].value)
# print(page["A2"].value)
# print(page["B2"].value)


