import argparse


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
        "-d", "--description", help="Expense description", type=str, required=True
    )
    add_subparser.add_argument("-a", "--amount", help="Expense amount", type=float, required=True)
    
    # Command Subparser - Update
    update_subparser = subparser.add_parser("update", help="Update an Expense data")
    update_subparser.add_argument("-i", "--id", help="ID of the expense to udpate *REQUIRED", type=int, required=True)
    
    # Command Subparser - Update - Expense Data Argument Group
    expense_data_ag = update_subparser.add_argument_group(title="Expense data", description="Information to update on the expense")
    expense_data_ag.add_argument("-d", "--description", help="New Expense description", type=str)
    expense_data_ag.add_argument("-a", "--amount", help="New Expense amount", type=float)
    
    

    return parser
