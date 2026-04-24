class Expense:
  def __init__(self, title: str, amount: float, category: str):
    self.title = title
    self.amount = amount
    self.category = category

  def to_dict(self):
    return {
      "title: self.title",
      "amount: self.amount",
      "category: self.category
    }

@staticmethod
def from_dict(data: dict):
  return Expense(data["title"], data["amount"], data["category"])
