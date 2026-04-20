from dataclasses import dataclass, field
from datetime import date as d

from expense import Expense


@dataclass
class ExpenseLog:
    id_counter: int = field(default=1)
    expenses: dict[int, Expense] = field(default_factory=dict)

    def add_expense(
        self,
        description: str = "Not specified",
        amount: float = 0.0,
        date: d | None = None,
    ) -> Expense:
        date = date or d.today()
        expense = Expense(self.id_counter, description, amount, date)
        self.expenses[expense.id] = expense
        self.id_counter += 1
        return expense

    def udpate_expense(
        self,
        id: int,
        description: str | None = None,
        amount: float | None = None,
        date: d | None = None,
    ) -> Expense:
        if not any((description, amount, date)):
            raise ValueError("Required input data to modify Expense")

        expense = self.expenses.get(id)

        if not expense:
            raise ValueError(f"Expense ({id}) not found")

        if description:
            expense.description = description
        if amount:
            expense.amount = amount
        if date:
            expense.date = date

        return expense

    def delete_expense(self, id: int) -> Expense:
        expense = self.expenses.pop(id, None)

        if not expense:
            raise ValueError(f"Expense ({id}) not found")

        return expense
