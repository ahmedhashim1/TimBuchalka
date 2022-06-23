# day = "Friday"
# temperature = 30
# raining = False
#
# if (day == "Saturday" and temperature > 27) or not raining:
#     print("Go swimming")
# else:
#     print("Learning Python")
if 0:
    print("True")
else:
    print("False")

name = input("Please enter name: ")
if name:  # is equivalent to if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
