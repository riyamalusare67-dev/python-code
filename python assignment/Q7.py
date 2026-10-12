def analyze_marks(*args):

    total = 0
    highest = 0
    passing_count = 0

    for i in args:
        total = total + i

        if i > highest:
            highest = i

        if i >= 40:
            passing_count = passing_count + 1

    average = total / len(args)

    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
    print("Passing count:", passing_count)


analyze_marks(35, 72, 80, 45, 90, 30)
