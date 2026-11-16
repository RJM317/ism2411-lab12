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

# Exercise 5:
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

