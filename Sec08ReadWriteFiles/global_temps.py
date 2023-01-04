import json
import urllib.request

# json_data_sourse = 'temperature_anoamaly.json'
json_data_sourse = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/11/1880-2022.json'
# with open(json_data_sourse, encoding='utf8') as data:
with urllib.request.urlopen(json_data_sourse) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year}...{value:6.2f}')

print("*" * 80)
print(anomalies['description'])
