# for i in range(1,13):
#     print("No. {} square is {} and cubed is {:<4}".format(i, i**2, i**3))
# print("*" * 80)
name = input("Please enter your name: ")
age = int(input("How old are you {0}? :  ".format(name)))
print(age)

# if age >= 18:
#     print("You are eligible for voting")
# else:
#     print("Sorry you are underage, please come back in {} years ".format(18 - age))


if age < 18:
    print("Sorry you are underage, please come back in {} years ".format(18 - age))
elif age == 900:
    print("Sorry, yoda, you die in return of the jedi")
else:
    print("You are eligible for voting")
