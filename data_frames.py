import pandas

data = pandas.read_csv('weather_data.csv')
# type(data)   -- >  DataFrames is the whole table.
# type(data['temp'])    -- >   Series represents individual columns.
print(data)

data_dict = data.to_dict()

# Series to list.
temp_list = data['temp'].tolist()
print(temp_list)

# aver = sum(temp_list)/len(temp_list)
# print(aver)

# print(data['temp'].mean())        --> average

# Get Data in columns
print(data['temp'])

# Get Data in row
print(data(data['day' == 'Monday']))


# Get that row when temp was max
print(data[data.temp == data.temp.max()])

# Condition for that particular day
monday = data[data.day == 'Monday']
print(monday.condition)