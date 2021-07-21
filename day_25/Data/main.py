
# To read CSV files
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

# To print only one coloumn
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(row[1])
    print(temperatures)

import pandas
# To convert data to dictionary
data = pandas.read_csv("weather_data.csv")
print(data['temp'])
data_dict = data.to_dict()
print(data_dict)
# To convert data to list
temp_list = data['temp'].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

print(data['temp'].mean())
print(data['temp'].max())

print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)