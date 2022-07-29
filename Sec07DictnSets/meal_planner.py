from Sec05ListTuples.mutable import shopping_list
from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tupple containing item and amount to the data dict"""
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    # below line is equivalent to above if statement with dict default method
    data[item] = data.setdefault(item, 0) + amount


# print(pantry)
# print(recipes)
display_dict = {}

for index, key in enumerate(recipes):
    # print(index + 1, key)
    display_dict[str(index + 1)] = key

shopping_list = {}
while True:
    print("Please choose your recipe:")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_qty in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_qty <= quantity_in_pantry:
                print(f"\t{food_item} OK.")
            else:
                quantity_to_buy = required_qty - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)
