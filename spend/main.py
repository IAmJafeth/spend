from argparse import ArgumentParser
from typing import TextIO
from typing import Sequence
from parser import build_parser
import sys

from expense_log import ExpenseLog

def run(
    argv: Sequence[str] | None = None,
    out: TextIO | None = None,
    err: TextIO | None = None
) -> int:
    out = out or sys.stdout
    err = err or sys.stderr

    parser: ArgumentParser
    subparsers: dict
    parser, subparsers = build_parser()
    args = parser.parse_args(argv)

    expense_log = ExpenseLog()
    expense_log.add_expense("Test Expense", 9.99)

    match(args.command):
        case "add":
            expense = expense_log.add_expense(args.description, args.amount)
            print(f"Expense added succesfully({expense.id})", file=out)
            return 0

        case "update":
            try:
                expense = expense_log.update_expense(args.id, args.description, args.amount, args.date)
                print(f"Expense updated: {expense}", file=out)
                return 0
            except ValueError as e:
                subparsers[args.command].error(str(e))
            except IndexError as e:
                print("error: ", e, file=out)
                return 2
        
        case "delete":
            try:
                expense = expense_log.delete_expense(args.id)
                print(f"Expense deleted: {expense}")
                return 0
            except IndexError as e:
                print("error: ", e, file=out)
                return 2 
    
    return 0



def main():
    return run()


if __name__ == "__main__":
    SystemExit(main())
