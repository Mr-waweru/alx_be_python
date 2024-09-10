income = (input("Enter your monthly income: "))
expenses = (input("Enter your total monthly expenses: "))

savings = float(income) - float(expenses)
monthly_savings = savings
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.0f}.")

