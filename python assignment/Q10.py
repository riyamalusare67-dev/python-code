def last(numbers):
    total=0
    count=0
    largest=0

    for n in numbers:
        if n>=0 and n % 2==0:   #checks if num is not negative and is even 
            n=n*n 
            total=total+n
            count=count+1

            if n>largest:
                largest=n

    print("total:",total)
    print("count:",count)
    print("largest:",largest)

numbers = [-2 ,1, 2, 4, -8]
last(numbers)
