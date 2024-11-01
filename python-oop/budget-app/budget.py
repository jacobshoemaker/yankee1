class Budget:
    def __init__(self, budget_amount):
        self.budget_amount = budget_amount
        self.remaining_balance = budget_amount
        self.expenses = []
    
    def add_expense(self, amount, category):
        if amount > self.remaining_balance:
            print("Expense exceeds remaining balance! Cannot add this expense.")
        else:
            expense = {"amount": amount, "category": category}
            self.expenses.append(expense)
            self.remaining_balance -= amount
    
    def view_balance(self):
        return self.remaining_balance

# my_budget = Budget(5000)
 
# my_budget.add_expense(2000, "bills")

# print(my_budget.view_balance())
    