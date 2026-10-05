# O(n)

def is_palindrome(word):
    if not word:
        return True

    if word[0] != word[-1]:
        return False

    return is_palindrome(word[1:-1])


print(is_palindrome("minecraft"))
