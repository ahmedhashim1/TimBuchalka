shopping_list = ["milk", "pasta", "eggs", "spams", "bread", "rice"]
another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]

print(shopping_list)
print(id(shopping_list))
print(another_list)
print(id(another_list))

a = b = c = d = e = f = another_list
print(a)
print("Adding cream")
b.append("cream")
print(b)
print(c)
print(f)
