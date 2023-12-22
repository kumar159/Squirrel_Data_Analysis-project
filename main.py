# with open('weather_data.csv', 'r') as data_file:
#     data = data_file.readlines()
#     print(data)                           -- >         prints as list format

import csv

with open('weather_data.csv', 'r') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        # print(row[1])
    #     if row[1] != 'temp':
        temperatures.append(row)
    print(temperatures)
# int(row[1])
# import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(data)
# print(data["temp"])