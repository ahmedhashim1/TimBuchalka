age = int(input("How old are you? "))

if 16 <= age <= 65:
    print("Have a good day")
else:
    print("Enjoy your free time.")
print("-" * 80)

if age < 16 or age > 65:
    print("Have a good day")
else:
    print("Enjoy your free time.")
