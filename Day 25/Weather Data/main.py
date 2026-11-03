# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as csvfile:
#     data = csv.reader(csvfile)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(data["temp"].max())

# Get Data in Row
print(data[data.day == "Monday"])

