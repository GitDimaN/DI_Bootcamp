import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
# print(list_of_numbers)
target_number = 3728

list_of_numbers_qualified = [nums for nums in list_of_numbers if nums <= target_number]

if target_number % 2 == 0 and len([v for v in list_of_numbers_qualified if v==target_number/2])>1:
    print(f"{(target_number/2)} and {int(target_number/2)} sums to the target_number {target_number}")

list_of_numbers_qualified = set(list_of_numbers_qualified)
list_of_numbers_qualified.remove(target_number/2)

pairs=[]
num_used=[]

for num in (list_of_numbers_qualified):
    if (target_number - num) in list_of_numbers_qualified and (num,target_number - num) not in pairs and (target_number - num, num) not in pairs:
        pairs.append((num,target_number - num))
        # list_of_numbers_qualified[:] = [item for item in list_of_numbers_qualified if (item !=num and item!=target_number-num)]
        # print(pairs[:-1])
        print(f"{num} and {target_number-num} sums to the target_number {num+target_number-num}")

print(f"a total of {len(pairs)} pairs summing up to {target_number}")