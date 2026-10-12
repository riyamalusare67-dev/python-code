
def anagram(first,second):
    if len(first)!=len(second):
        return False

    for i in first:
        if first.count(i)!=second.count(i):
            return False

    return True

first="listen"
second="slime"

print(anagram(first,second))
