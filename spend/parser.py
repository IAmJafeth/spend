import argparse
from datetime import date


def build_parser() -> argparse.ArgumentParser:

    # Main Parser
    parser = argparse.ArgumentParser(
        description="Spend is a command-line tool for tracking and managing your expenses.",
        prog="spend",
        epilog="A project from @Roadmap.sh",
    )

    # Command Subparser
    subparser = parser.add_subparsers(
        title="Commands", dest="command", required=True, help="Available commands"
    )

    # Command Subparser - Add
    add_subparser = subparser.add_parser("add", help="Add a new Expense")
    add_subparser.add_argument(
        "-d",
        "--description",
        help="Expense description *REQUIRED",
        type=str,
        required=True,
    )
    add_subparser.add_argument(
        "-a", "--amount", help="Expense amount *REQUIRED", type=float, required=True
    )
    add_subparser.add_argument(
        "-t", "--date", help="Date of the expense YYYY-mm-dd", type=date.fromisoformat
    )

    # Command Subparser - Update
    update_subparser = subparser.add_parser("update", help="Update an Expense data")
    update_subparser.add_argument(
        "-i",
        "--id",
        help="ID of the expense to udpate *REQUIRED",
        type=int,
        required=True,
    )

    # Command Subparser - Update - Expense Data Argument Group
    expense_data_ag = update_subparser.add_argument_group(
        title="Expense Update Data", description="Information to update on the expense | AT LEAST ONE ARGUMENT IS REQUIRED"
    )
    expense_data_ag.add_argument(
        "-d", "--description", help="New Expense description", type=str, default=None
    )
    expense_data_ag.add_argument(
        "-a", "--amount", help="New Expense amount", type=float, default=None
    )
    expense_data_ag.add_argument(
        "-t", "--date", help="New Date amount", type=date.fromisoformat, default=None
    )

    return parser
