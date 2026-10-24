import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
print(list_of_numbers)
target_number = 3728

list_of_numbers_qualified = [nums for nums in list_of_numbers if nums <= target_number]

pairs=[]
num_used=[]
for num in list_of_numbers_qualified:
    if (target_number - num) in list_of_numbers_qualified:
        pairs.append((num,target_number - num))
        num_used.append(num)
        num_used.append(target_number - num)
        list_of_numbers_qualified.remove(num)
        list_of_numbers_qualified.remove(target_number - num)
        # print(pairs[:-1])
        # print(f"{num} + {target_number-num} = {num+target_number-num}")

print(f"a total of {len(pairs)} pairs summing up to {target_number}")