import random


def get_integer(prompt):
    """
    Get an integer from standard input (stdin)
    The function will continue looping, and prompting
    the user, until a valid `int` input receives

    :param prompt: The string that user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else: is not needed as the next line will execute once return fails
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
