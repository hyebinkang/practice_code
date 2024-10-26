def palindrome(word):
    result = True
    for i in range(len(word)//2):
        if word[i] == word[len(word)-i-1]:
            continue
        else:
            result = False
            break

    return result
print(palindrome('radar'))
palindrome('python')
