a = [25, 63, 23, [6, 4, [6, 2, 45, [[[[[[[[6]]]]]]]]]], 6]
b = [25, 63, 23, 6, 4, 6, 2, 45, 6]
r = []

def num_list(lst):
    for element in lst:
        if isinstance(element, int):
            r.append(element)
        else:
            num_list(element)

num_list(a)
print(r)

def a(n):
    print(n)
    if n <= 0:
        return "stop"
    else:
        return a(n-1)

