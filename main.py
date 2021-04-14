from src.args import cli_args
from src.reader import file_reader

if __name__ == "__main__":
    args = vars(cli_args().parse_args())

    filename = args.get("file")
    file_content = file_reader(filename)
    # Parse content
    # Print values
