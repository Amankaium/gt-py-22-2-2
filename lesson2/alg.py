lst = [6, 2, 7, 26, 24, 23, 52] #... n
# c = lst[0]


for num in lst: # O(n ** 2)
    is_max = True
    for k in lst:
        if num < k:
            is_max = False
            break
    if is_max:
        print(num, " is maximal")


# for num in lst: O(n)
#     if c < num:
#         c = num

