class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.savings_goal = 0

    def set_income(self, income):
        self.income = income

    def add_expense(self, category, amount):
        self.expenses.append({'category': category, 'amount': amount})

    def set_savings_goal(self, goal):
        self.savings_goal = goal

    def calculate_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def calculate_savings(self):
        return self.income - self.calculate_total_expenses()

    def provide_budgeting_advice(self):
        savings = self.calculate_savings()
        if savings < self.savings_goal:
            return f"You need to save {self.savings_goal - savings} more to reach your savings goal."
        else:
            return "You are on track with your savings!"

# Example usage
budget = BudgetTracker()
budget.set_income(4000)
budget.add_expense("Groceries", 1000)
budget.add_expense("Utilities", 500)
budget.set_savings_goal(1000)

print(f"Total Expenses: {budget.calculate_total_expenses()}")
print(f"Savings: {budget.calculate_savings()}")
print(budget.provide_budgeting_advice())
