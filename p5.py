"""stats(nums) returns min, max and average as a tuple
Unpack the result into lo, hi, avg and print them
grade(marks, passing=50) returns "Pass" or "Fail"
Call grade(55), then grade(55, passing=60)"""

numbers = [4, 8, 15, 16, 23, 42]

def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

def grade(marks, passing=50):
    return "Pass" if marks >= passing else "Fail"

lo, hi, avg = stats(numbers)
print(f"{lo} {hi} {avg}")

print(grade(55), grade(55, passing=60))