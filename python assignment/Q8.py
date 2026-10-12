def palindrome(word, start, end):
    if start >= end:
        return True

    if word[start] != word[end]:
        return False

    return palindrome(word, start + 1, end - 1)


word = "racecarr"
print(palindrome(word, 0, len(word) - 1))
