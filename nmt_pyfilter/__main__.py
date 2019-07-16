from argparse import ArgumentParser

def run():
    parser = ArgumentParser()
    parser.add_argument('--fn', required=True, type=str)
    args, remaining_args = parser.parse_known_args()


if __name__ == "__main__":
    run()
