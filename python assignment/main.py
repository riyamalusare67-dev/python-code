
def second_largest(list):
    largest = 0
    second = 0

    for i in list:
        if i > largest:
            second = largest
            largest = i
        elif i < largest:
            if i > second:
                second = i

    return second


list = [12, 35, 1, 10, 34, 35]
print(second_largest(list))
