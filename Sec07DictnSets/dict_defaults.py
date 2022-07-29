from contents import pantry

chicken_quality = pantry.setdefault("chicken", 0)
print(f"Chicken: {chicken_quality}")

beans_quantity = pantry.setdefault("beans", 1)
print(f"Beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"Ketchup: {ketchup_quantity}")

print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)
