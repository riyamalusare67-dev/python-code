
def missing_num(numbers, n):
    total = n * (n + 1) // 2

    for i in numbers:
        total = total - i

    return total

numbers = [1,3,4,5,6,7]
n = 7

print(missing_num(numbers, n))
