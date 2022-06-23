albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for (name, artist, year) in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Cofee", 200, 100, 75, 34.5)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)
