monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
annual_interest = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(projected_savings)