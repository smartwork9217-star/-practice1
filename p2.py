"""Print the word reversed using slicing
Print the first 3 and last 3 characters on one line
Count how many times "m" appears
Write is_palindrome(s); test it on "level" and "python"""

word = "Programming"
print(word[::-1])
print(f"{word[:3]} {word[-3:]}")
print(word.count("m"))
def is_palindrome(s: str) -> bool:
    return s == s[::-1]
print(is_palindrome("level"), is_palindrome("python"))