import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a valid number".format(temp))


highest = 100
answer = random.randint(1, highest)
print(answer)
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:

    guess = get_integer(": ")
    if guess == 0:
        print("Exiting the game now......!!!")
        break

    if guess == answer:
        print("Well done, you've guess it.")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you've guess it.")
        # else:
        #     print("Sorry Incorrect answer")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guess it.")
#     else:
#         print("Sorry incorrect answer.")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guess it.")
#     else:
#         print("Sorry incorrect answer.")
# else:
#     print("Sorry incorrect answer.")
