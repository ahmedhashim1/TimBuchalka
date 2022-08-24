small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)
small_ints.discard(10)
print(small_ints)
small_ints.remove(11)
print(small_ints)

small_ints.discard(22)  # this line do not generate errors
small_ints.remove(23)  # this line generates error
