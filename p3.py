"""A list of squares of the even numbers from 1 to 10
A dict mapping each word to its length
The unique letters of "banana", sorted, using a set"""

words = ["ai", "python", "data"]

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)

word_lengths = {w: len(w) for w in words}
print(word_lengths)

unique_letters = sorted({c for c in "banana"})
print(unique_letters)