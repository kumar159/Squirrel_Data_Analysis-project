import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# All rows that contain gray squirrels.
gray_squirrel = data[data['Primary Fur Color'] == "Gray"]

# Count of all gray squirrels.
gray_squirrel_count = len(data[data['Primary Fur Color'] == "Gray"])
print(gray_squirrel_count)

red_squirrel_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
print(red_squirrel_count)

black_squirrel_count = len(data[data['Primary Fur Color'] == "Black"])
print(black_squirrel_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
print(df)
# df.to_csv("squirrel_count.csv")


