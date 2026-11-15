# csv_practice.py
# Exercise 2:
import csv

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
      
