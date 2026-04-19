from dataclasses import dataclass
from datetime import date as d

@dataclass
class Expense: 
    id: int 
    description: str
    amount: float
    date: d
    