# csv_practice.py
#Reflection questions: 1.) Python is pretty good for ETL because it is able to automatically read, change and write big amounts of data. Excel is easier for viewing data and making quick manual changes but python is the better option for repeating tasks.
# question 2.) A business could use a append-mode log file to help keep track of daily sales. Append mode is useful bc new entries are added without deleting older ones, which creates a history thta is able to be reviewed later.

# Exercise 2:
print("Exercise 2")
import csv

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
      
#Exercise 3:
print("Exercise 3")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("Header:", header)

    for row in reader:
        print(row)

#Exercise 4: 
print("Exercise 4")

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

# Exercise 5:
print("Exercise 5")
total_rows = 0
written_rows = 0

with open("data/sales.csv", "r") as infile:
    reader = csv.reader(infile)

    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            total_rows += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_rows += 1

print("Rows in original file:", total_rows)
print("Rows written to cleaned.csv:", written_rows)

# Exercise 6:
print("Exercise 6")
total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        total_revenue += total

print("Total Revenue:", round(total_revenue, 2))

# csv reader is better when you know the column positions, 
# dictreader is easier because you can use the column names.

# Exercise 7:
print("Exercise 7")
summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])

        if product in summary:
            summary[product] += revenue
        else:
            summary[product] = revenue

for product in sorted(summary):
    print(product, ":", round(summary[product], 2))


# Exercise 8:
print("Exercise 8")

import csv
from datetime import datetime
timestamp = datetime.now()

with open("data/run_log.txt", "a") as file:
    file.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")

print("Log updated.")
