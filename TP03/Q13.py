def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


if __name__ == "__main__":
    print("Is 'radar' a palindrome?:", is_palindrome("radar"))
    print("Is 'hello' a palindrome?:", is_palindrome("hello"))
