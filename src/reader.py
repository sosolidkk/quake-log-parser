from typing import List, AnyStr


def file_reader(filename: str) -> List[AnyStr]:
    lines = None

    with open(filename, "r") as file:
        lines = file.readlines()
    return lines
