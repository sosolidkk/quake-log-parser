def file_reader(filename: str):
    lines = None
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines
