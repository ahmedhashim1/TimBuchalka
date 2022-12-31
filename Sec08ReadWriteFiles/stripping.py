filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)
chars = " 'Twasebv"
# no_opostrophe = first.strip(chars)
# print(no_opostrophe)
for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print("*" * 80)

for character in first[::-1]:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break
