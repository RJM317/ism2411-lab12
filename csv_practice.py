# csv_practice.py
# Exercise 2:
import csv

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
      
#Exercise 3:
import csv

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("Header:", header)

    for row in reader:
        print(row)

#Exercise 4: 
import csv

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("Header:", header)
    print()

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print()
print(f"Total Revenue: ${total_revenue:.2f}")

