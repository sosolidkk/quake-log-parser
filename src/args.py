import argparse


def cli_args():
    description = "Program to parse a QUAKE log file"
    args = argparse.ArgumentParser(description=description)

    args.add_argument(
        "--file", "-f", help="Log filename", type=str, required=True,
    )

    return args
