name = input("Please enter name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("{}, Enjoy your holiday...".format(name))
else:
    print("Sorry {}, you are not eligible.".format(name))
