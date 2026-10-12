
def move(num):
    list= []

    for i in num:
        if i != 0:
            list.append(i)

    for i in num:
        if i == 0:
            list.append(i)

    return list


num = [0, 1, 0, 3, 12, 0, 5]
print(move(num))
