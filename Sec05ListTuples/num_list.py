empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
# print(numbers)

for num_list in numbers:
    print(num_list)
    for value in num_list:
        print(value)

# numbers = even + odd
# print(numbers)
#
# sorted_num = sorted(numbers)
# print(sorted_num)
# print(numbers)
#
# digits = list("432985617")
# print(digits)
#
# # more_numbers = list(numbers)
# # more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
#
# print(id(more_numbers))
# print(id(numbers))
