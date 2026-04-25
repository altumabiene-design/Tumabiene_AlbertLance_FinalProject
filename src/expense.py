"""
expense.py
Defines the Expense class.
"""

class Expense:
    """Represents a single expense record."""
    def __init__(self, id, title, amount, category, date):
        """Initialize an Expense object."""
        self.id = id
        self.title = title
        self.amount = float(amount)
        self.category = category
        self.date = date

    def to_dict(self):
        """Convert the Expense object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        """Create an Expense object from a dictionary."""
        return Expense(
            data["id"],
            data["title"],
            data["amount"],
            data["category"],
            data["date"]
        )
