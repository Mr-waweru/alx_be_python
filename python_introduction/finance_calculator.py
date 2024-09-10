monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)

annual_interest_rate = 0.05
annual_savings = monthly_savings * 12
annual_interest = annual_savings * annual_interest_rate
projected_savings = annual_savings + annual_interest

print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
