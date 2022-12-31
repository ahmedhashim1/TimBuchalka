input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_zone': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict

print(countries)

while True:
    user_input = input("Please type name of country: ")
    chosen_country = user_input.casefold()
    if chosen_country in countries:
        print(
            f'The capital of {countries[chosen_country]["name"]} {countries[chosen_country]["country_code"]} is: {countries[chosen_country]["capital"]}')
    elif user_input == 'quit':
        break
    else:
        print("Chosen country not found")
