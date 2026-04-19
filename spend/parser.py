import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Spend is a command-line tool for tracking and managing your expenses.",
        prog="spend",
        epilog="A project from @Roadmap.sh",
    )

    subparser = parser.add_subparsers(
        title="Commands", dest="command", required=True, help="Available commands"
    )

    add_subparser = subparser.add_parser("add", help="Add a new Expense")
    add_subparser.add_argument(
        "-d", "--description", help="Expense description", type=str, required=True
    )
    add_subparser.add_argument("-a", "--amount", help="Expense amount", type=str, required=True)

    return parser
