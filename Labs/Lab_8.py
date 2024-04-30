import csv

companies = []
sales = []

# Read data from the CSV file
with open("output.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        companies.append(row[0])
        # Append sales data (convert to integers and remove commas)
        sales.append([int(s.replace(",", "")) for s in row[1:]]) # casting strings to ints and relacing commas


# doing the sums now
# Calculate monthly sales totals
monthly_sum = [sum(month_sales) for month_sales in zip(*sales)]

# Calculate yearly sales totals for each company
yearly_sum = {}
for company, company_sales in zip(companies, sales):
    yearly_sum[company] = sum(company_sales)

# Print monthly sales totals
print("Monthly Sales Totals:")
for month, total in zip(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'], monthly_sum):
    print(f"{month}: {total}")

# Print yearly sales totals for each company
print("\nYearly Sales Totals by Manufacturer:")
for company, total in yearly_sum.items():
    print(f"{company}: {total}")
