from src.args import cli_args

if __name__ == "__main__":
    args = vars(cli_args().parse_args())

    filename = args.get("filename")
