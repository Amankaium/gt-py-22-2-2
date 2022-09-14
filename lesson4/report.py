# Получить средний балл по группе

with open("students.txt", mode="r", encoding="utf-8") as my_file:
    output_text = my_file.readlines()

marks = []
for txt in output_text:
    txt_lst = txt.strip().split()
    print(txt_lst)
    if txt_lst[-1].isdigit():
        mark = int(txt_lst[-1])
    else:
        mark = 0
    marks.append(mark)

print(sum(marks) / len(marks))

