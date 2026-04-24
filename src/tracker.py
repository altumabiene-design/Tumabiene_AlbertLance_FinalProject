import json
from expense import Expense

class ExpenseTracker:
  def __init__(self, file_path="data/expenses.json"):
    self.file_path = file_path
    self.expenses = []
    self.load_data()

  def add_expenses(self, title, amount, category):
    self.expenses.append(Expense(title, amount, category))
    print("Expense added!")

  def view_expenses(self):
    if not self.expenses:
      print("No expenses found.")
      return

    for i, exp in enumerate(self.expenses, 1):
      print(f"{i}. {exp.title} | ₱{exp.amount:.2f} | {exp.category}")

  def search_expense(self, keyword):
        results = [e for e in self.expenses if keyword.lower() in e.title.lower()]

        if results:
            for e in results:
                print(f"{e.title} | ₱{e.amount:.2f} | {e.category}")
        else:
            print("No matching expenses.")

    def delete_expense(self, title):
        before = len(self.expenses)
        self.expenses = [e for e in self.expenses if e.title.lower() != title.lower()]
        after = len(self.expenses)

        if before == after:
            print("Expense not found.")
        else:
            print("Expense deleted.")

    def sort_expenses(self):
        self.expenses.sort(key=lambda e: e.amount, reverse=True)
        print("Expenses sorted by amount.")

    def total_expense(self):
        total = sum(e.amount for e in self.expenses)
        print(f"Total Expenses: ₱{total:.2f}")

    def category_summary(self):
        summary = {}

        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount

        print("\nCategory Summary:")
        for cat, total in summary.items():
            print(f"{cat}: ₱{total:.2f}")

    def save_data(self):
        with open(self.file_path, "w") as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=4)
        print("Data saved.")

    def load_data(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(d) for d in data]
        except FileNotFoundError:
            self.expenses = []
      
