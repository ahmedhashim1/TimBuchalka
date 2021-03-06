avail_parts = ["Computer",
               "Monitor",
               "Keyboard",
               "Mouse",
               "Mouse Pad",
               "HDMI Cable",
               "DVD Drive"]

# advance code with list comprehnsion to be covered in later sections
# valid_choices = [str(i) for i in range(1, len(avail_parts) + 1)]
valid_choices = []
for i in range(1, len(avail_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in valid_choices:

        index = int(current_choice) - 1
        chosen_part = avail_parts[index]

        if chosen_part in computer_parts:
            print("Removing part {}".format(chosen_part))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))

    else:
        print("Please add this options from the list below:")
        for num, part in enumerate(avail_parts):
            print("{0} : {1}".format(num + 1, part))

    current_choice = input()

print(computer_parts)
