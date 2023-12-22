import pandas

data_dict = {
    "students" : ["Kumar", "Arjun", "Karna"],
    "scores" : [75, 100, 99]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")