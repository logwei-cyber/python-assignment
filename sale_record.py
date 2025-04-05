salesmen_count = 10
items_count = 5

sales_data = []

print("Enter sales data:")
for i in range(salesmen_count):
    print(f"Salesman {i+1}:")
    salesman_name = input("Enter the name of the salesman: ")
    sales = []
    for j in range(items_count):
        item_sales = int(input(f"Enter sales for Item {j+1}: "))
        sales.append(item_sales)
    total_sales = sum(sales)
    sales_data.append((salesman_name, sales, total_sales))

grand_total = sum(salesman[2] for salesman in sales_data)


print("\nSales Report")
print("Name".ljust(10), "Item1 Item2 Item3 Item4 Item5 TotalSales")
print("_" * 50)

for salesman in sales_data:
    name = salesman[0]
    sales = " ".join(str(x).ljust(5) for x in salesman[1])
    total_sales = salesman[2]
    print(f"{name.ljust(10)} {sales} {total_sales}")

print("_" * 50)
print(f"GrandTotal: {grand_total}")
