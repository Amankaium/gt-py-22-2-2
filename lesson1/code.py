a = [5, 27, 42, 10, 200, 40, 24]
b = [] # делятся на 3
c = [] # делятся на 4

for num in a:
    if num % 4 == 0:
        c.append(num)

    if num % 3 == 0:
        b.append(num)


print(b) # [27, 42]
print(c) # [200, 40]
