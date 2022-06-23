shopping = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping:
#     if item != "spam":
#         print("Buy " + item)
for item in shopping:
    if item == "spam":
        break

    print("Buy " + item)
