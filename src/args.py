from argparse import ArgumentParser


def cli_args() -> ArgumentParser:
    description = "Program to parse a QUAKE log file"
    args = ArgumentParser(description=description)

    args.add_argument(
        "--file", "-f", help="Log filename", type=str, required=True,
    )

    return args
