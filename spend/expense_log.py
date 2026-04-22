import datetime
from dataclasses import dataclass, field

from expense import Expense
from exceptions import ExpenseDataInvalid, ExpenseNotFound


@dataclass
class ExpenseLog:
    id_counter: int = field(default=1)
    expenses: dict[int, Expense] = field(default_factory=dict)

    def add_expense(
        self,
        description: str | None = None,
        amount: float | None = None,
        date: datetime.date | None = None,
    ) -> Expense:
        if description is None or amount is None:
            raise ExpenseDataInvalid("A description and amount is required to create an Expense")
        if amount < 0:
            raise ExpenseDataInvalid("Expense amount can not be lower than 0")
        
        date = date or datetime.date.today()
        expense = Expense(self.id_counter, description, amount, date)
        
        self.expenses[expense.id] = expense
        self.id_counter += 1
        
        return expense

    def update_expense(
        self,
        id: int,
        description: str | None = None,
        amount: float | None = None,
        date: datetime.date | None = None,
    ) -> Expense:
        if description is None and amount is None and date is None:
            raise ExpenseDataInvalid("Required input data to modify Expense")
            
        expense = self.expenses.get(id)

        if not expense:
            raise ExpenseNotFound(f"Expense ({id}) not found")
        
        if amount is not None:
            if amount < 0: 
                raise ExpenseDataInvalid("Expense amount can not be lower than 0")
            expense.amount = amount
        if description is not None:
            expense.description = description
        if date is not None:
            expense.date = date

        return expense

    def delete_expense(self, id: int) -> Expense:
        expense = self.expenses.pop(id, None)

        if not expense:
            raise IndexError(f"Expense ({id}) not found")

        return expense
