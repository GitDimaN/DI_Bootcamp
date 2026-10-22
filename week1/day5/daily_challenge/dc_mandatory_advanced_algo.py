import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
print(list_of_numbers)
target_number = 3728

from itertools import combinations
pairs = list(combinations([nums for nums in list_of_numbers if nums >= target_number], 2))


for pair in pairs:
    if sum(pair) == target_number:
        print(f"{pair[0]} and {pair[1]} sums to the target_number {target_number}")