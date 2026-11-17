import os
import csv
from datetime import datetime
if os.path.exists('../data/expenses.csv'):
    print ("expenses.csv found." )
    with open('../data/expenses.csv', 'r') as file:
        reader = csv.DictReader(file)
        total = 0 
        today = datetime.today().strftime("%B %d, %Y")
        expenses = []  
        for row in reader:
            if row['category']=='Food':
                row["amount"] = float(row["amount"])
                expenses.append(row)           
                total +=  float(row["amount"])   
        with open("food_report.txt", "w") as report:
            report.write(f"Food Expense Report — generated {today}\n")
            for expense in expenses:
                report.write(f"{expense['date']}: ${expense['amount']:.2f}\n")
            report.write(f"Total: ${total:.2f}\n")
else:
    print("expenses.csv not found.") 
