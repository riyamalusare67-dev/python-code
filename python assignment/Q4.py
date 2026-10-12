
def duplicate(numbers):
    count=0
    largest=0

    for i in range(0,len(numbers)):
        if numbers[i]==numbers[i-1]:
            count=count + 1
        else:
            count=1

        if count>largest:
            largest=count

    return largest

numbers=[5,4,9,9,2,3,3,1,1, 1]
print(duplicate(numbers))
