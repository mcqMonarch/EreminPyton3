def isPalindrome(phrase):
    if len(phrase) <= 1:
        return True
    else:
        # if phrase[0] == phrase[-1]:
        #     return isPalindrome(phrase[1:-1])
        # else:
        #     return False
        return isPalindrome(phrase[1:-1]) and phrase[0] == phrase[-1]


print(isPalindrome('шалаш'))
print(isPalindrome('комп'))


def isPalindrome2(phrase):
    return phrase[0:len(phrase) // 2 + 1] == phrase[-1:(len(phrase) // 2 - 1):-1]


print(isPalindrome2('шалаш'))
print(isPalindrome2('искать такси'.replace(' ', '')))
