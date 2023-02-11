import pytz
import datetime

country = 'Europe/Moscow'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# for printing all time zones pytz module have
# for x in pytz.all_timezones:
#     print(x)

# for printing of all country names within pytz module
# for y in pytz.country_names:
#     print(y + ": " + pytz.country_names[y])

# for z in pytz.country_names:
#     print("{}: {}: {}".format(z, pytz.country_names[z], pytz.country_timezones.get(z)))

for z in pytz.country_names:
    print("{}: {}".format(z, pytz.country_names[z]), end=': ')
    if z in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[z]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo timezones defined")
