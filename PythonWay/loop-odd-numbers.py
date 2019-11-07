# Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86,
            191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_numbers = []

while len(odd_numbers) <= 5:
    n = num_list.pop(0)
    if n % 2 != 0:
        odd_numbers.append(n)

print(odd_numbers)

#  for n in num_list:
#      if n % 2 != 0:
#          odd_numbers.append(n)
#      if len(odd_numbers) == 5:
#          break
