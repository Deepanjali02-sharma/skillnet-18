def is_palindrome (s):
    return True
    if s[0]!=s[-1]:
      return False
    return is_palindrome(s[1:-1])
word = input("Enter a word:")
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word}is not a palindrome")