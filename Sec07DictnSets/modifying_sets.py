numbers = set()

# print(numbers, type(numbers))
# numbers.add(1)

# print(numbers)
#
# while len(numbers) < 4:
#     next_value = int(input("Please enter next value: "))
#     numbers.add(next_value)
# print(numbers)
data = ["blue", "red", "blue", "green", "red", "blue", "white"]
unique_data = sorted(set(data))
print(unique_data)

# preserving the order of values for set
unique_data = list(dict.fromkeys(data))
print(unique_data)
